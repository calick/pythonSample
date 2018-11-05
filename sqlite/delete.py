# coding: UTF-8
import sqlite3

dbpath="sample_db.sqlite"
connection=sqlite3.connect(dbpath)
cursor=connection.cursor()

try:
    # DELETE
    cursor.execute('DELETE FROM sample WHERE id > 1')

except sqlite3.Error as e:
    print("sqlite3 Error occured : ",eargs[0])

connection.commit()
connection.close()

