# coding: utf-8
import cgi
import os
import time

_weekdayname = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_monthname = [None,
              "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Request(object):
    """
    HTTPのリクエストをハンドリングするクラス
    CGI側でインスタンスを生成することによって利用する
    クエリデータや環境変数へのアクセス,主要ヘッダへの
    アクセス用メソッドを提供
    """
    def __init__(self, environ=os.environ):
        """
        インスタンスの初期化メソッド
        クエリ,環境変数をアトリビュートとして保持する
        """
        self.form=cgi.FieldStorage() 
        self.environ=environ

class Response(object):
    """
    HTTPのレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成して利用する
    レスポンスやヘッダの内容の保持,ヘッダを含めたレスポンスの
    送信を行う
    """
    def __init__(self,charset='utf-8'):
        """
        ※環境変数にはWebアプリケーションが受け取ることができる様々な情報が詰まっている
        ヘッダ用の辞書、本文用の文字列などを初期化する
        """
        # self.headers={'Content-type':'text/html;charset=%s' %charset}
        self.headers={'Content-type':'text/html;charset=utf-8'}
        self.body=""
        self.status=200
        self.status_message='aaa'  

    # レスポンスヘッダを設定する
    def set_header(self,name,value):
        self.headers[name]=value
    
    # 設定済みのレスポンス用ヘッダを返す
    # ヘッダが定義されていない場合はNoneを返す
    def get_header(self,name):
        return self.headers.get(name,None)

    def set_body(self,bodystr):
        # レスオンすとして出力する本文の文字列を返す
        self.body=bodystr

    # ヘッダと本文を含めたレスポンス文字列全体を作るメソッド
    def make_output(self,timestamp=None):
        if timestamp is None:
            timestamp = time.time()
            year, month, day, hh, mm, ss, wd, y, z = time.gmtime( timestamp)
            dtstr="%s, %02d %3s %4d %02d:%02d:%02d GMT" % (
                        _weekdayname[wd], day,
                        _monthname[month], year,
                        hh, mm, ss)
            # レスポンスを返す時間を表すLast-Modifiedヘッダは、決められたフォーマットに沿って文字列を作らなければな
            self.set_header("Last-Modified", dtstr)
            # self.set_header("Last-Modified", "Fri, 31 May 2019 23:28:00 GMT")
            headers='\n'.join(["%s: %s" % (k, v)
                            for k,v in self.headers.items()])
            # hds=u"Content-type: text/html;charset=utf-8" + '\n' + "Last-Modified: Fri, 31 May 2019 23:28:00 GMT"
            # hds="Content-Type: text/html; charset=utf-8" + '\n' + "Content-Type: multipart/form-data; boundary=something"
            return headers+'\n\n'+self.body
            # return hds+'\n\n'+ self.body
            # return self.body
            # return get_htmltemplate()

    # 特殊メソッドと呼ばれるメソッドで、インスタンスオブジェクトを文字列に変換しようとするときに呼ばれる
    def __str__(self):
        # リクエストを文字列に変換する
        # return self.make_output().encode('utf-8')
        return self.make_output()
        # return self.body
        # return get_htmltemplate()

def get_htmltemplate():
    """
    レスポンスとして返すHTMLのうち,定型部分を返す
    """
    html_body = u"""
    <html>
      <head>
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
      </head>
      <body>
        <h1>sample page</h1>
      %s
      </body>
    </html>"""
    return html_body
