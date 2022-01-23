from flask import Flask
from flask import render_template
import pymysql
import mariadb
import datetime

app = Flask(__name__)

db_host = "localhost"
try:
    db = mariadb.connect(
        host=db_host,
        user="root",
        password="****",
        db="weather_station_test"
    )
except (mariadb.OperationalError, mariadb.InternalError) as e:
    print("La DB n'existe pas elle va etre cree")
    print(repr(e))
    db = mariadb.connect(
        host=db_host,
        user="root",
        password="****",
        db="weather_station_test"
    )
    sql = ["CREATE DATABASE weather_station_test;", "use weather_station_test;"]
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
except mariadb.ProgrammingError:
    print("La DB est vide")
    import_sql_filename = "./db_schema.sql"
    request_list = get_sql_from_file(import_sql_filename)
    if request_list is not False:
        for idx, sql_request in enumerate(request_list):
            with db.cursor() as cursor:
                cursor.execute(sql_request + ';')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello/<n>")
def hello_name(n):
    return render_template("hello.html", name=n)


if __name__ == "__main__":
    app.run()
