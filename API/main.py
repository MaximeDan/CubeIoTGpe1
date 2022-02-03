from flask import Flask, request, redirect, url_for, session
from flask_restx import Resource, Api, fields, reqparse
from secrets import token_urlsafe
import mysql.connector
import datetime


app = Flask(__name__)

api = Api(app=app, version="0.1", doc="/api", title="Mon API", description="ceci est une description de l'api de test",
          default="mon api", default_label='ceci est une api de test', validate=True)

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1412",
        db="Weather_station_test"
    )
except mysql.connector.Error as e:
    print("La DB n'existe pas elle va etre cree")
    print(repr(e))
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1412",
    )
    sql = ["CREATE DATABASE weather_station;",
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
        sql = "SELECT `id` FROM weather_station_test.`sonde1` WHERE `id`=%s;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print("Il existe au moins un article dans la DB")
        if result == None:
            print("Les tables de la DB sont vides on importe un peu de contenu")
            import_sql_filename = "./db_with_sampledata.sql"
            request_list = get_sql_from_file(import_sql_filename)
            if request_list is not False:
                for idx, sql_request in enumerate(request_list):
                    with db.cursor() as cursor:
                        print(sql_request)
                        cursor.execute(sql_request + ';')
                        db.commit()
except mysql.connector.ProgrammingError:
    print("La DB est vide")
    import_sql_filename = "./db_schema.sql"
    request_list = get_sql_from_file(import_sql_filename)
    if request_list is not False:
        for idx, sql_request in enumerate(request_list):
            with db.cursor() as cursor:
                cursor.execute(sql_request + ';')


### DEMO with simple api function via HTTP GET in default namespace
@api.route("/api/v1/ping")
class Ping(Resource):
    def get(self):
        """
        Test de l'API avec un simple ping
        """
        return {'response': 'pong'}, 200


@api.route("/api/v1/esp", methods=['POST'])
class temperature(Resource):
    def post(self):
        """Supprimer une ligne de données"""
        temp = api.payload['temperature']
        hum = api.payload['humidity']
        #sql = "INSERT INTO weather_station_test.`sonde1` VALUES (`temperature`, `humidity`)"
        sql = "INSERT INTO weather_station_test.`sonde1` (`temperature`, `humidity`) VALUES ("+str(temp)+", "+str(hum)+")"
        with db.cursor(dictionary=True) as cursor:
            result = cursor.execute(sql)
            db.commit()
            last_id = cursor.lastrowid
        return {'user created with id': str(last_id)}, 200


@api.route("/api/v1/delete/temperature/<int:id>", methods=['DELETE'])
class temperature(Resource):
    def delete(self, id):
        """Supprimer une ligne de données"""
        sql = "DELETE FROM weather_station_test.`sonde1` WHERE `id`="+str(id)
        with db.cursor(dictionary=True) as cursor:
            print(sql)
            result = cursor.execute(sql)
            db.commit()
            print(result)
            # if int(result) > 0:
            #     return {'user_deleted_with_success': str(result)}, 200
            # else:
            #     return {'error': 'no user found to delete'}, 204
    # def get(self, id):
    #     """
    #     Retourner un utilisateur pour un ID donné
    #     """
    #     sql = "SELECT `id`, CAST(`temperature` as double) as temperature, CAST(`humidity` as double) as humidity, CAST(`added` as CHAR) as added FROM `sonde1` WHERE `id`=%s"
    #     with db.cursor(dictionary=True) as cursor:
    #         cursor.execute(sql, (id,))
    #         result = cursor.fetchone()
    #     return result
@api.route("/api/v1/add", methods=['POST'])
class temperature(Resource):
    def post(self):
        """Supprimer une ligne de données"""
        #sql = "INSERT INTO weather_station_test.`sonde1` VALUES (`temperature`, `humidity`)"
        sql = "INSERT INTO weather_station_test.`sonde1` (`temperature`, `humidity`) VALUES (%s, %s)"
        with db.cursor(dictionary=True) as cursor:
            result = cursor.execute(sql, (20.6, 51.2))
            db.commit()
            last_id = cursor.lastrowid
        return {'user created with id': str(last_id)}, 200


#
# @app.route('/')
# def index():
#     return 'index'
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
#
#
# @app.route('/user/<username>')
# @login_required
# def profile(username):
#     return f'{username}\'s profile'
#
#
# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))
#
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
#
# @app.route('/about')
# def about():
#     return 'The about page'


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
