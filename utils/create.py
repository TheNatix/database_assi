import mysql.connector as ms


def creatingdb():
    file = open("utils\\base.sql","r")
    sql = file.read()
    dbconn = ms.connect(user='root', password='root', host='localhost')
    cursor = dbconn.cursor()
    DB_NAME = "Cafe"
    cursor.execute("CREATE DATABASE " + DB_NAME)
    cursor.execute("USE " + DB_NAME)
    for result in cursor.execute(sql, multi=True):
        if result.with_rows:
            print(result.fetchall())
    dbconn.close()