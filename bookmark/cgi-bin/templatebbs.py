# coding: utf-8
import sqlite3
from string import Template
from os import path
from httphandler import Request,Response,get_htmltemplate
import cgi
import cgitb;cgitb.enable()

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

con=sqlite3.connect('./bookmark.dat')
cur=con.cursor()

# データベースにデータを登録するためのテーブルを作成
try:
    cur.execute("""CREATE TABLE bookmark ( title text, url text);""")
except:
    pass

req=Request()
f=req.form
value_dic={'message':'','title':'','url':'','bookmarks':''}

# postであれば入力チェックをして問題なければ登録の処理を行う
if 'post' in f:
# if f.get('post',None) != None:
    if not f.getvalue('title','') or not f.getvalue('url',''):
        value_dic['message']=u'タイトルとURLは必須項目です'
        value_dic['title']=unicode(f.getvalue('title',''),'utf-8','ignore')
        value_dic['url']=f.getvalue('url','')
    else:
        cur.execute(
            """INSERT INTO bookmark(title,url) VALUES(?, ?)""",
            (f.getvalue('title',''),f.getvalue('url',''))
        )
        con.commit()

# ブックマークの一覧を表示
listbody=''
cur.execute("SELECT title,url FROM bookmark")
for item in cur.fetchall():
    listbody+="""<dt>%s</dt><dd>%s</dd>\n"""%(item)
listbody="""<ul>\n%s</ul>"""%listbody
value_dic['bookmarks']=listbody

# 以下出力の処理
res=Response()

t=Template(open('template/bookmarkform.html','r',encoding='utf-8').read())

body=t.substitute(value_dic)
print(body)
print("--------------------------------------------------------")
res.set_body(body)

print(res)
