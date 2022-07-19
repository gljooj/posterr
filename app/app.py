from flask import Flask, request

from data_test_migrate import CreateTests
from src.controller.home_controller import HomeController
from src.controller.post_controller import PostController
from src.controller.profile_controller import ProfileController

app = Flask("posterr")


@app.route("/hello")
def hello_world():
    return "<p>Hello, From Posterr!</p>"


@app.route("/", methods=["GET"])
def setup():
    return CreateTests().setup()


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET" and 'user' in request.headers:
        profile_controller = ProfileController(user=request.headers.get('user'),
                                               page=request.args.get('page', 1))
        return profile_controller.profile_page()

    """Create profile"""
    if request.method == "POST" and 'user' not in request.headers:
        profile_controller = ProfileController(user=None)
        return profile_controller.new_user(request.json)


@app.route("/home", methods=["GET"])
def home():
    home_controller = HomeController(user=request.headers.get('user'),
                                     page=request.args.get('page', 1),
                                     post_from=request.args.get('post_from', 'all'),
                                     start_at=request.args.get('start_at', None),
                                     end_at=request.args.get('end_at', None))
    return home_controller.home_page()


@app.route("/home/post", methods=["POST"])
@app.route("/profile/post", methods=["POST"])
@app.route("/post", methods=["POST"])
def post():
    controller = PostController(request.headers.get('user'))
    return controller.new_post(request.json)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
