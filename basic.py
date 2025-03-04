from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello_world():
    return "Hello, World!"


@app.route("/data")
def data():
    if (
        request.headers.get("Content-Type") == "application/json"
        and request.get_json().get("return_type") == "json"
    ):
        return ["spam", "ham", "eggs", "bacon"]
    return "spam,ham,eggs,bacon"
