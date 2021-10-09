from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def landing():
    return render_template("landing.html")


@app.route("/about")
def generic():
    return render_template("generic.html")


if __name__ == "__main__":
    app.run(debug=True)
