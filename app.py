from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
@app.route("/clock")
def clock():
    """Display the current time"""
    return render_template("pages/clock.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=app.debug)
