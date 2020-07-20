# coding: utf-8
# dice
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "HelloWorld"

@app.route("/hoge")
def hoge():
    return "Hello hoge"

app.run(host="localhost",port=12345)

