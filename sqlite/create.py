# coding: UTF-8
import sqlite3

dbpath="sample_db.sqlite"

connection=sqlite3.connect(dbpath)
cursor=connection.cursor()

try:
    # create
    cursor.execute("DROP TABLE IF EXISTS sample")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sample(id INTEGER PRIMARY KEY, name TEXT, age DOUBLE)"
    )

    # insert
    cursor.execute("INSERT INTO sample VALUES (1,'test1',1.5)")
    cursor.execute("INSERT INTO sample VALUES (2,'test1',2.3)")
    cursor.execute("INSERT INTO sample VALUES (3,'test2',2.3)")
    cursor.execute("INSERT INTO sample VALUES (4,'test2',2.3)")
    cursor.execute("INSERT INTO sample VALUES (5,'test2',2.3)")


except sqlite3.Error as e:
    print("sqlite3 Error occured : ",eargs[0])

connection.commit()

connection.close()