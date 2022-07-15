from flask import Flask, request

from src.controller.home_controller import HomeController
from src.controller.post_controller import PostController
from src.controller.profile_controller import ProfileController

app = Flask("posterr")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    profile_controller = ProfileController(username=username, page=request.args.get('page', 1))
    return profile_controller.profile_page()


@app.route("/home/<username>", methods=["GET"])
def home(username):
    home_controller = HomeController(username=username, page=request.args.get('page', 1))
    return home_controller.home_page()


@app.route("/post", methods=["POST"])
def post():
    controller = PostController()
    return controller.new_post(request.json)


@app.route("/comment", methods=["GET", "POST"])
def comment():
    return "<p>Hello, World!</p>"
