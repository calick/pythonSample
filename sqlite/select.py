# coding: UTF-8
import sqlite3

dbpath="sample_db.sqlite"
connection=sqlite3.connect(dbpath)
cursor=connection.cursor()

try:
    # 全権取得
    cursor.execute('SELECT * FROM sample ORDER BY id')
    res = cursor.fetchall()
    print(res)

    # 全件ループ表示方法(イテレータ)
    for row in cursor.execute('SELECT * FROM sample ORDER BY id ASC'):
        print(row)

    # 全件ループ表示方法(fetchall)
    cursor.execute('SELECT * FROM sample ORDER BY id ASC')
    for row in cursor.fetchall():
        print(row)

    print("---")

    # idが2の行を取得
    cursor.execute('SELECT * FROM sample WHERE id=?', ('2',))
    print(cursor.fetchone())

    # nameが"test1"の行を取得
    cursor.execute('SELECT * FROM sample WHERE name=?', ('test1',))
    # print(cursor.fetchall())
    print("test")
    li=cursor.fetchall()
    print(li)
    print("list size is "+ str(len(li)))

    # 取得した値で計算
    total=0.0
    for row in li:
        print(row[0])
        print(row[1])
        print(row[2])
        total+=row[2]
    print(total)

except sqlite3.Error as e:
    print("sqlite3 Error occured : ",eargs[0])

connection.commit()
connection.close()