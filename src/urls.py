from flask import Flask

app = Flask("posterr")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
