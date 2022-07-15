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


@app.route("/user", methods=["post"])
def user():
    profile_controller = ProfileController(username=None, page=request.args.get('page', 1))
    return profile_controller.new_user(request.json)


@app.route("/home/<user>", methods=["GET"])
def home(user):
    home_controller = HomeController(user=user, page=request.args.get('page', 1))
    return home_controller.home_page()


@app.route("/post", methods=["POST"])
def post():
    controller = PostController()
    return controller.new_post(request.json)
