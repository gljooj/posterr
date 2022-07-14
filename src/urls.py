from flask import Flask, request

from src.controller.profile_controller import Profile

app = Flask("posterr")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    profile = Profile(username=username, page=request.args.get('page'))
    return profile.profile_page()


@app.route("/home", methods=["GET"])
def home(username):
    profile = Profile(username=username, page=request.args.get('page'))
    return profile.profile_page()


@app.route("/post", methods=["GET", "POST"])
def post():
    return "<p>Hello, World!</p>"


@app.route("/comment", methods=["GET", "POST"])
def comment():
    return "<p>Hello, World!</p>"
