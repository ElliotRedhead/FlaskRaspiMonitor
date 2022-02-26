from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    """Basic view to check Flask routing"""
    return "Hello world"


@app.route("/standalone")
def basic_html():
    """Display a single HTML file only"""
    return render_template("pages/standalone.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=app.debug)
