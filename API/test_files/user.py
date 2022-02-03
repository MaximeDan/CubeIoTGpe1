import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request



# Add a new data into the database rows [table name : utilisateurs]
@app.route('/api/v1/user/ajouter/', methods=['POST'])
def ajouter_user():
    _json = request.json
    _user = _json['nom_dutilisateur']
    _nom = _json['nom']
    _prenom = _json['prenom']
    _email = _json['email']
    _password = _json['mot_de_passe']

    if _user and _nom and _prenom and _email and _password and request.method == 'POST':
        sqlQuery = "INSERT INTO utilisateurs(nom_dutilisateur, nom, prenom, email, mot_de_passe) VALUES(%s, %s, %s, %s,%s)"
        bindData_add_user = (_user, _nom, _prenom, _email,  _password)
        conn = mysql.connect()
        cursor_add_user = conn.cursor()
        cursor_add_user.execute(sqlQuery, bindData_add_user)
        conn.commit()
        response_add_user = jsonify('les données ont été enregistrées avec succès !')
        response_add_user.status_code = 200
        return response_add_user
    else:
        return not_found()


@app.route('/api/v1/utilisateurs/')
def lire():
    try:
        conn = mysql.connect()
        cursor_don = conn.cursor(pymysql.cursors.DictCursor)
        cursor_don.execute("SELECT id, nom_dutilisateur, nom, prenom, email, mot_de_passe FROM utilisateurs")
        empRows = cursor_don.fetchall()
        response_don = jsonify(empRows)
        response_don.status_code = 200
        return response_don
    except Exception as e:
        print(e)
    finally:
        cursor_don.close()
        conn.close()


@app.route('/api/v1/utilisateur/<int:id>')
def fitlrerHumid(id):
    try:
        conn = mysql.connect()
        cursor_user = conn.cursor(pymysql.cursors.DictCursor)
        cursor_user.execute(
            "SELECT id, nom_dutilisateur, nom, prenom, email, mot_de_passe FROM utilisateurs WHERE id =%s", id)
        empRow = cursor_user.fetchone()
        response_filt_user = jsonify(empRow)
        response_filt_user.status_code = 200
        return response_filt_user
    except Exception as e:
        print(e)
    finally:
        cursor_user.close()
        conn.close()


@app.route('/api/v1/user/modifier/', methods=['PUT'])
def modifier():
    try:
        _json = request.json
        _id = _json['id']
        _user = _json['nom_dutilisateur']
        _nom = _json['nom']
        _prenom = _json['prenom']
        _email = _json['email']
        _password = _json['mot_de_passe']

        if _id and _user and _nom and _prenom and _email and _password and request.method == 'PUT':
            sqlQuery = "UPDATE utilisateurs SET id=%s, nom_dutilisateur=%s, nom=%s, prenom=%s, email=%s, mot_de_passe=%s WHERE id=%s"
            bindData_mod = (_id, _user, _nom, _prenom, _email, _password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData_mod)
            conn.commit()
            response_mod = jsonify('les données ont été modifié avec succès')
            response_mod.status_code = 200
            return response_mod
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/api/v1/user/supprimer/<int:id>', methods=['DELETE'])
def supprimer(id):
    try:
        conn = mysql.connect()
        cursor_sup = conn.cursor()
        cursor_sup.execute("DELETE FROM utilisateurs WHERE id=%s", id)
        conn.commit()
        response_sup = jsonify('Données ont été supprimées avec succès!')
        response_sup.status_code = 200
        return response_sup
    except Exception as e:
        print(e)
    finally:
        cursor_sup.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Enregistrement introuvable mais l\'api marche : ' + request.url,
    }
    response_error = jsonify(message)
    response_error.status_code = 404
    return response_error


if __name__ == "__main__":
    app.run()
