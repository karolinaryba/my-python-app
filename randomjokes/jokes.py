#! /Users/karolina.ryba/.pyenv/shims/python

import random
from flask import Flask, render_template

app = Flask(__name__)


joke_db = [
    "Why did the orange lose the race? It ran out of juice.",
    "How you fix a broken pumpkin? With a pumpkin patch.",
    "Why are fish so smart? They live in schools!",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "Why did the man fall down the well? Because he couldn’t see that well!",
    "What did the sink tell the toilet? You look flushed!",
    " Where do boats go when they're sick? To the dock.",
    "What has ears but cannot hear? A cornfield!",
    "Stop looking for the perfect match; use a lighter.",
    "Can February March? No, but April May!",
    "Why was 6 afraid of 7? Because 7 ate nine!",
    "I'm so good at sleeping that I do it with my eyes closed.",
    "Try the seafood diet—you see food, then you eat it.",
    "What do you call a pencil with two erasers? Pointless.",
    "Did you hear the one about the roof? Never mind, it's over your head.",
    "What's brown and sticky? A stick.",
    "I hated facial hair but then it grew on me.",
    "It really takes guts to be an organ donor."]


    

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/generator")
def generator():
    html_response = render_template('generator.html') +"<p>"+ random.choice(joke_db)+"</p>"+render_template('newjoke.html')
    return html_response

if __name__ == "__main__":
     app.run(host='127.0.0.1')