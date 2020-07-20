import http.server

server_address = ("", 8000)
## リクエストを受け取るという出来事が起きると、起動した時のカレントディレクトリにあるファイルを見せる
# handler_class = http.server.SimpleHTTPRequestHandler #ハンドラを設定
## リクエストを受け取るという出来事が起きると、サーバ上のPythonのプログラムを動かす
handler_class = http.server.CGIHTTPRequestHandler #1 ハンドラを設定
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()