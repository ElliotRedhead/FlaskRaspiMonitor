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


@app.route("/basic-include")
def stitched_html():
    """Example of Jinja include, and tab title determined using Context Processor"""
    # https://jinja.palletsprojects.com/en/3.0.x/templates/#include
    # https://flask.palletsprojects.com/en/2.0.x/templating/#context-processors
    return render_template("structure/base.html", title="Injected title")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=app.debug)
