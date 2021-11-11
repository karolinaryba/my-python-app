#!/Users/karolina.ryba/.pyenv/shims/python

from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/hello")
def world():
    return "<h1>Hello World!!!!!</h1>"
if __name__ == "__main__":
    app.run(host='127.0.0.1')