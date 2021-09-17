from flask.helpers import url_for
from flask import Flask, redirect, request
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        print(request.form)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
