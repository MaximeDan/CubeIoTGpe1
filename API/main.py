import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request


# Add a new data into the database rows [table name : donnees]
@app.route('/api/v1/ajouter/', methods=['POST'])
def ajouter():
    #try:
    _json = request.json
    _temperature = _json['temperature']
    _humidity = _json['humidite']
    _capteur = _json['capture']

    if _temperature and _humidity  and _capteur and request.method == 'POST':
        sqlQuery = "INSERT INTO donnees(temperature, humidite, capture) VALUES(%s, %s, %s)"
        bindData_aj = (_temperature, _humidity, _capteur)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sqlQuery, bindData_aj)
        conn.commit()
        response_aj = jsonify('les données ont été enregistrées avec succès !')
        response_aj.status_code = 200
        return response_aj
    else:
        return not_found()
    #except Exception as e:
    #    print(e)
    #finally:
    #   cursor.close()
    #  conn.close()



# fetch all rows from  database concernning the table utilisateurs [table name : donnees]
@app.route('/api/v1/donnees/')
def lire():
    try:
        conn = mysql.connect()
        cursor_don = conn.cursor(pymysql.cursors.DictCursor)
        cursor_don.execute("SELECT id, temperature, humidite, date, capture FROM donnees")
        empRows = cursor_don.fetchall()
        response_don = jsonify(empRows)
        response_don.status_code = 200
        return response_don
    except Exception as e:
        print(e)
    finally:
        cursor_don.close()
        conn.close()


@app.route('/api/v1/donnees/humidite/<int:id>')
def fitlrerHumid(id):
    try:
        conn = mysql.connect()
        cursor_hum = conn.cursor(pymysql.cursors.DictCursor)
        cursor_hum.execute("SELECT id, humidite, date, capture FROM donnees WHERE id =%s", id)
        empRow = cursor_hum.fetchone()
        response_filt_hum = jsonify(empRow)
        response_filt_hum.status_code = 200
        return response_filt_hum
    except Exception as e:
        print(e)
    finally:
        cursor_hum.close()
        conn.close()


@app.route('/api/v1/donnees/temperature/<int:id>')
def fitlrerTemp(id):
    try:
        conn = mysql.connect()
        cursor_temp = conn.cursor(pymysql.cursors.DictCursor)
        cursor_temp.execute("SELECT id, temperature, date, capture FROM donnees WHERE id =%s", id)
        empRow = cursor_temp.fetchone()
        response_filt_temp = jsonify(empRow)
        response_filt_temp.status_code = 200
        return response_filt_temp
    except Exception as e:
        print(e)
    finally:
        cursor_temp.close()
        conn.close()


@app.route('/api/v1/modifier/', methods=['PUT'])
def modifier():
    try:
        _json = request.json
        _id = _json['id']
        _temperature = _json['temperature']
        _humidity = _json['humidite']
        _date = _json['date']
        _capteur = _json['capture']
        if _id and _temperature and _humidity and _date and _capteur and request.method == 'PUT':
            sqlQuery = "UPDATE donnees SET temperature=%s, humidite=%s, date=%s, capture=%s WHERE id=%s"
            bindData_mod = (_id, _temperature, _humidity, _date, _capteur)
            conn = mysql.connect()
            cursor_mod = conn.cursor()
            cursor_mod.execute(sqlQuery, bindData_mod)
            conn.commit()
            response_mod = jsonify('les données ont été modifié avec succès')
            response_mod.status_code = 200
            return response_mod
        else:
            return not_found()
    except Exception as e: \
            print(e)
    finally:
        cursor_mod.close()
        conn.close()


@app.route('/api/v1/supprimer/<int:id>', methods=['DELETE'])
def supprimer(id):
    try:
        conn = mysql.connect()
        cursor_sup = conn.cursor()
        cursor_sup.execute("DELETE FROM donnees WHERE id=%s", id)
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
