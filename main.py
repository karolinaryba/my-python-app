#!/Users/karolina.ryba/.pyenv/shims/python
import json
from flask import Flask, request, Response

app = Flask(__name__)

movie_db = {
    "1" : {
        "name" : "Stargate", 
        "release_date" : "1994"},
    "2" : {
        "name" : "Sunshine", 
        "release_date" : "2007"},
    "3" : {
        "name" : "The Holiday",
        "release_date" : "2006"}
}

@app.route("/")
def hello():
    return "Hello world"

@app.route("/movies")
def movies():
    return json.dumps(movie_db)

#read
@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    return json.dumps(movie_db[movie_id])

if __name__ == "__main__":
    app.run(host='127.0.0.1')

    #create(post), read(get), update(put), delete(get)