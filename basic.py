from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def data():
    if request.headers["Content-Type"] == "application/json":
        return ["spam", "ham", "eggs", "bacon"]
    return "spam,ham,eggs,bacon"
