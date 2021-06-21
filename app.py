from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Your number one news source"

@app.route("/news")
def hello_world():
    return "Your number one news source"
