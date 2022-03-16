import mysql.connector as ms


def importing():
    file = open("utils\\data.sql","r")
    sql = file.read()
    dbconn = ms.connect(user='root', password='root', host='localhost')
    cursor = dbconn.cursor()
    DB_NAME = "Cafe"
    cursor.execute("USE " + DB_NAME)
    for result in cursor.execute(sql, multi=True):
        if result.with_rows:
            print(result.fetchall())
    dbconn.commit()
    dbconn.close()