# coding: utf-8
# sample bottle
from bottle import route, run

# routeデコレーター
# これを使用してURLのPathと関数をマッピングする。
@route('/hello')
def hello():
  return "Hello World!!"

@route('/hello/<name>')
def hello(name):
  return template('Hello {{name}}', name=name)

# ビルトインの開発用サーバーの起動
# ここでは、debugとreloaderを有効にしている
run(host='localhost', port=8080, debug=True, reloader=True)
