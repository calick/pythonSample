# coding: UTF-8
import sqlite3

dbpath="sample_db.sqlite"
connection=sqlite3.connect(dbpath)
cursor=connection.cursor()

try:
    # UPDATE
    ## id=2の行のデータを更新
    cursor.execute('UPDATE sample SET name="hoge", age=3.2 WHERE id=2')

except sqlite3.Error as e:
    print("sqlite3 Error occured : ",eargs[0])

connection.commit()
connection.close()

