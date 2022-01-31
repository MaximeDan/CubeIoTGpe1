from flask import Flask
from flask_restx import Resource, Api, fields, reqparse
from secrets import token_urlsafe
import mysql.connector
import datetime

app = Flask(__name__)

api = Api(app=app, version="0.1", doc="/api", title="Mon API", description="ceci est une description de l'api de test",
          default="mon api", default_label='ceci est une api de test', validate=True)

# # Config Flask Namespace Definition
# namespace_temperature = api.namespace(name='temperature', description="Fonctions API gestion de la température",
#                                       path="/",
#                                       validate=True)
# namespace_users = api.namespace(name='users', description="Fonctions API d'affichage des utilisateurs", path="/",
#                                 validate=True)
# namespace_post = api.namespace(name='article', description="Fonctions API gestion des articles", path="/",
#                                validate=True)
# namespace_posts = api.namespace(name='articles', description="Fonctions API d'affichage de tous les articles", path="/",
#                                 validate=True)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="****",
        db="Weather_station_test"
    )
except mysql.connector.Error as e:
    print("La DB n'existe pas elle va etre cree")
    print(repr(e))
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="****",
    )
    sql = ["CREATE DATABASE weather_station_test;",
           "use weather_station_test;"]
    with db.cursor() as cursor:
        for query in sql:
            cursor.execute(query)


def get_sql_from_file(filename):
    """
    Get the SQL instruction from a file
    :return: a list of each SQL query without the trailing ";"
    """
    from os import path
    # File did not exists
    if path.isfile(filename) is False:
        print("File load error : {}".format(filename))
        return False
    else:
        with open(filename, "r") as sql_file:
            # Split file in list
            ret = sql_file.read().split(';')
            # drop last empty entry
            ret.pop()
            return ret


try:
    with db.cursor() as cursor:
        sql = "SELECT `id` FROM `sonde1` WHERE `id`=%s"
        cursor.execute(sql, (1))
        result = cursor.fetchone()
        print("Il existe au moins un article dans la DB")
        if result is None:
            print("Les tables de la DB sont vides on importe un peu de contenu")
            import_sql_filename = "./db_with_sampledata.sql"
            request_list = get_sql_from_file(import_sql_filename)
            if request_list is not False:
                for idx, sql_request in enumerate(request_list):
                    with db.cursor() as cursor:
                        print(sql_request)
                        cursor.execute(sql_request + ';')
                        db.commit()
except mysql.connector.Error():
    print("La DB est vide")
    import_sql_filename = "./db_schema.sql"
    request_list = get_sql_from_file(import_sql_filename)
    if request_list is not False:
        for idx, sql_request in enumerate(request_list):
            with db.cursor() as cursor:
                cursor.execute(sql_request + ';')



# # Définition modèles des données
# posts_resource_fields = api.model('ArticleResource', {
#     'title': fields.String(description='Le Titre de l\'article', default='Titre par défaut', example='This is a title',
#                            required=True),
#     'description': fields.String(description='La description de l\'article', default='Description par défaut',
#                                  example='This is a description', required=True),
#     'content': fields.String(description='Le Contenu de l\'article', required=True),
#     'author_firstname': fields.String(description='Le Prenom de l\'auteur', required=True),
#     'api_key': fields.String(description='Clé API de l\'utilisateur autorisé à éditer des articles', required=True)
# })
# posts_arguments = reqparse.RequestParser()
# posts_arguments.add_argument('title')
# posts_arguments.add_argument('description')
# posts_arguments.add_argument('content')
# posts_arguments.add_argument('author_firstname')
# users_resource_fields = api.model('UserResource', {
#     'first_name': fields.String(description='Le Prénom de l\'auteur', default='Prénom', example='Julien',
#                                 required=True),
#     'last_name': fields.String(description='Le Nom de l\'auteur', default='Nom', example='Toutain', required=True),
#     'email': fields.String(description='L\'email de l\'auteur', default='Email', example='toutainj@gmail.com',
#                            required=True),
#     'birthdate': fields.String(description='La date de naissance de l\'auteur', default='Date de naissance',
#                                example='2020-01-01', required=True)
# })
# users_arguments = reqparse.RequestParser()
# users_arguments.add_argument('first_name')
# users_arguments.add_argument('last_name')
# users_arguments.add_argument('email')
# users_arguments.add_argument('birthdate')


### DEMO with simple api function via HTTP GET in default namespace
@api.route("/api/v1/ping")
class Ping(Resource):
    @api.response(200, 'API Ping : Success')
    @api.response(400, 'API Ping: Error')
    @api.response(403, 'API Ping: Ceci n\'est pas autorisé')
    def get(self):
        """
        Test de l'API avec un simple ping
        """
        return {'response': 'pong'}, 200

    @api.response(400, 'API Ping: This is a custom 400 error code')
    def delete(self):
        """
        Test de l'API avec erreur 400
        """
        return {'response': 'bad pong'}, 400

    def post(self):
        """
        Test de l'API avec erreur 403
        """
        return {'response': 'pong'}, 200


@api.route("/api/v1/temperature/<int:id>")
class temperature(Resource):
    @api.doc(params={'id': 'ID de l\'utilisateur à récupérer'})
    def get(self, id):
        """
        Retourner un utilisateur pour un ID donné
        """
        sql = "SELECT `id`, CAST(`temperature` as double) as temperature, CAST(`humidity` as double) as humidity, CAST(`added` as CHAR) as added FROM `sonde1` WHERE `id`=%s;"
        with db.cursor(mysql.connector.di) as cursor:
            cursor.execute(sql, id)
            result = cursor.fetchone()
        return result

    @api.doc(params={'id': 'ID de l\'utilisateur à supprimer'})
    @api.response(200, 'API User : Deleted with Success')
    @api.response(204, 'API User : User not found cant be deleted')
    def delete(self, id):
        """
        Supprimer un utilisateur pour un ID donné
        """
        sql = "DELETE from authors WHERE id=%s RETURNING id"
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            result = cursor.execute(sql, id)
            db.commit()
        if int(result) > 0:
            return {'user_deleted_with_success': str(result)}, 200
        else:
            return {'error': 'no user found to delete'}, 204


#
#
# # POST new user without specifying an ID in route (use autoincrement from mariadb)
# @namespace_user.route("/api/v1/user")
# class User(Resource):
#     @api.expect(users_resource_fields, validate=True)
#     @api.response(200, 'API User : Created with Success')
#     def post(self):
#         """
#         Créer un utilisateur
#         """
#         sql = "INSERT INTO authors (first_name, last_name, email, birthdate, api_key) VALUES (%s, %s, %s, %s, %s);"
#         with db.cursor() as cursor:
#             author_api_key = token_urlsafe(32)
#             cursor.execute(sql, (
#                 api.payload['first_name'], api.payload['last_name'], api.payload['email'], api.payload['birthdate'],
#                 author_api_key))
#             db.commit()
#             last_id = cursor.lastrowid
#         return {'user created with id': str(last_id)}, 200
#
#
# @namespace_users.route("/api/v1/users")
# class Users(Resource):
#     def get(self):
#         sql = "SELECT `id`, `first_name`, `last_name`, `email`, CAST(`birthdate` as CHAR) as birthdate, CAST(`added` AS CHAR) as added FROM `authors`;"
#         with db.cursor(pymysql.cursors.DictCursor) as cursor:
#             cursor.execute(sql)
#             result = cursor.fetchall()
#         return result
#
#
# @namespace_posts.route("/api/v1/articles")
# class Articles(Resource):
#     @api.expect(posts_arguments)
#     def get(self):
#         data = posts_arguments.parse_args(api.payload)
#         if data.get('title'):
#             sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts` \
#                     WHERE `title` LIKE '%" + str(data.get('title')) + "%';"
#         elif data.get('description'):
#             sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts` \
#                     WHERE `description` LIKE '%" + str(data.get('description')) + "%';"
#         elif data.get('content'):
#             sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts` \
#                     WHERE `content` LIKE '%" + str(data.get('content')) + "%';"
#         elif data.get('author_firstname'):
#             sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts` \
#                     WHERE `author_id`=(SELECT id from authors WHERE first_name LIKE '%" + str(
#                 data.get('author_firstname')) + "%');"
#         else:
#             # sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts`"
#             sql = "SELECT `id`, `title`, `description`, `content`, `author_id`, CAST(`date` AS CHAR) as date FROM `posts` order by `id` DESC"
#         with db.cursor(pymysql.cursors.DictCursor) as cursor:
#             try:
#                 cursor.execute(sql)
#                 result = cursor.fetchall()
#             except Exception as e:
#                 result = "Pas OU trop de résultat \nError:" + str(e)
#         return result
#
#
# # GET / DELETE an article
# @namespace_post.route("/api/v1/article/<int:id>")
# class Article(Resource):
#     @api.doc(params={'id': 'ID de l\'article à récupérer'})
#     def get(self, id):
#         # Retourner un article
#         sql = "SELECT `id`, `title`, `description`, `content`, (SELECT first_name FROM authors WHERE id=author_id) as author, CAST(`date` AS CHAR) as date FROM `posts` WHERE `id`=%s"
#         with db.cursor(pymysql.cursors.DictCursor) as cursor:
#             cursor.execute(sql, id)
#             result = cursor.fetchone()
#         return result
#
#     @api.doc(params={'id': 'ID de l\'article à supprimer'})
#     def delete(self, id):
#         # Supprimer un article
#         sql = "DELETE from posts WHERE id=%s"
#         with db.cursor(pymysql.cursors.DictCursor) as cursor:
#             cursor.execute(sql, id)
#             db.commit()
#
#     @api.expect(posts_resource_fields, validate=True)
#     @api.doc(params={'id': 'ID de l\'article à mettre à jour'})
#     def put(self, id):
#         sql_authorid = "SELECT id from authors WHERE first_name=%s"
#         sql = "UPDATE posts SET title = %s, description = %s, content = %s, author_id = %s WHERE id=%s"
#         with db.cursor() as cursor:
#             cursor.execute(sql_authorid, (api.payload['author_firstname']))
#             author_id = cursor.fetchone()
#             cursor.execute(sql,
#                            (api.payload['title'], api.payload['description'], api.payload['content'], author_id, id))
#             db.commit()
#
#
# # POST new article without specifying an ID (use autoincrement from mariadb) REQUIRE API_KEY !!
# @namespace_post.route("/api/v1/article")
# class Article(Resource):
#     @api.expect(posts_resource_fields, validate=True)
#     def post(self):
#         sql_authorid = "SELECT id from authors WHERE first_name=%s ;"
#         sql_authorkey = "SELECT api_key from authors WHERE id=%s ;"
#         sql = "INSERT INTO posts (title, description, content, author_id) VALUES (%s, %s, %s, %s);"
#         with db.cursor() as cursor:
#             cursor.execute(sql_authorid, (api.payload['author_firstname']))
#             author_id = cursor.fetchone()
#             cursor.execute(sql_authorkey, author_id)
#             author_key = cursor.fetchone()[0]
#             if str(author_key) == str(api.payload['api_key']):
#                 cursor.execute(sql,
#                                (api.payload['title'], api.payload['description'], api.payload['content'], author_id))
#                 db.commit()
#                 last_id = cursor.lastrowid
#                 return last_id
#             else:
#                 return {'Error': 'Check your API Key'}

#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
#
# @app.route("/hello/<n>")
# def hello_name(n):
#     return render_template("hello.html", name=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
