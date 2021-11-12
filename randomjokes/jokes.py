#! /Users/karolina.ryba/.pyenv/shims/python

import random
from flask import Flask, render_template

app = Flask(__name__)


joke_db = [
    "What the ocean say to other ocean? They just waved",
    "Wanna hear a construction joke? I'm err building it",
    "Two bytes meet,the first byte asks are you ill? He said na I'm feeling off, my wife left me and my son decided to get with l3 cache",
    "Programming is like sex. One mistake and you have to support it for the rest of your life.",
    "Why did the programmer quit his job? Cos he didn't get a raise!" ]

    

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/generator")
def generator():
    html_response = render_template('generator.html') +"<p>"+ random.choice(joke_db)+"</p>"+render_template('newjoke.html')
    return html_response

if __name__ == "__main__":
     app.run(host='127.0.0.1')