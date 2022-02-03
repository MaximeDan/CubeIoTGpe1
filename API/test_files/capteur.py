import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request


# Add a new data into the database rows [table name : api]
@app.route('/api/v1/capteur/ajouter/', methods=['POST'])
def ajouter_capteur():
    _json = request.json
    _nom = _json['nom']
    _description = _json['description']
    _version = _json['version']
    _statut = _json['statut']

    if _nom and _description and _version and _statut and request.method == 'POST':
        sqlQuery = "INSERT INTO `api` (`id`, `nom`, `description`, `version`, `statut`) VALUES(NULL,%s, %s,%s ,%s)"
        bindData_cap = (_nom, _description, _version, _statut)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData_cap)
        conn.commit()
        response_cap = jsonify('les données ont été enregistrées avec succès !')
        response_cap.status_code = 200
        return response_cap
    else:
        return not_found()


@app.route('/api/v1/capteurs/')
def lire():
    try:
        conn = mysql.connect()
        cursor_caps = conn.cursor(pymysql.cursors.DictCursor)
        cursor_caps.execute("SELECT id, nom, description, version, statut FROM api")
        empRows = cursor_caps.fetchall()
        response_caps = jsonify(empRows)
        response_caps.status_code = 200
        return response_caps
    except Exception as e:
        print(e)
    finally:
        cursor_caps.close()
        conn.close()


@app.route('/api/v1/capteur/<int:id>')
def fitlrer_capteur(id):
    try:
        conn = mysql.connect()
        cursor_capteur = conn.cursor(pymysql.cursors.DictCursor)
        cursor_capteur.execute(
            "SELECT id, nom, description, version, statut FROM api WHERE id =%s", id)
        empRow = cursor_capteur.fetchone()
        response_filt_cap = jsonify(empRow)
        response_filt_cap.status_code = 200
        return response_filt_cap
    except Exception as e:
        print(e)
    finally:
        cursor_capteur.close()
        conn.close()


@app.route('/api/v1/capteur/modifier/', methods=['PUT'])
def modifier():
    try:
        _json = request.json
        _id = _json['id']
        _nom = _json['nom']
        _description = _json['description']
        _version = _json['version']
        _statut = _json['statut']

        if _id and _nom and _description and _version and _statut and request.method == 'PUT':
            sqlQuery = "UPDATE `api` SET `nom` = %s, `description` = %s, `version` = %s, `statut` = %s WHERE `api`.`id` = %s"
            bindData_mod_cap = (_id, _nom, _description, _version, _statut)
            conn = mysql.connect()
            cursor_mod_cap = conn.cursor()
            cursor_mod_cap.execute(sqlQuery, bindData_mod_cap)
            conn.commit()
            response_mod_cap = jsonify('les données ont été modifié avec succès')
            response_mod_cap.status_code = 200
            return response_mod_cap
        else:
            return not_found()
    except Exception as e: \
            print(e)
    finally:
        cursor_mod_cap.close()
        conn.close()


@app.route('/api/v1/capteur/supprimer/<int:id>', methods=['DELETE'])
def supprimer(id):
    try:
        conn = mysql.connect()
        cursor_sup_cap = conn.cursor()
        cursor_sup_cap.execute("DELETE FROM api WHERE id=%s", id)
        conn.commit()
        response_sup_cap = jsonify('Données ont été supprimées avec succès!')
        response_sup_cap.status_code = 200
        return response_sup_cap
    except Exception as e:
        print(e)
    finally:
        cursor_sup_cap.close()
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
