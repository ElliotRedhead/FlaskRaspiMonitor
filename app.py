from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Basic view to check Flask routing"""
    return "Hello world"


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=app.debug)
