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


@app.route("/extended")
def extended_html():
    """Example of Jinja template inheritance"""
    cool_variable = 3
    if cool_variable < 0:
        frozen = True
    else:
        frozen = False
    return render_template(
        "pages/child_template.html",
        title="New title",
        cool_variable=cool_variable,
        frozen=frozen,
    )


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=app.debug)
