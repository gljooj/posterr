import pymongo
from flask import Flask

from src.core.usecase.profile import Profile

app = Flask("posterr")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    profile = Profile(username)
    return f"<p>Hello, {profile.payload()}!</p>"


@app.route("/home", methods=["GET"])
def home():
    return "<p>Hello, World!</p>"


@app.route("/post", methods=["GET", "POST"])
def post():
    return "<p>Hello, World!</p>"


@app.route("/comment", methods=["GET", "POST"])
def comment():
    return "<p>Hello, World!</p>"
