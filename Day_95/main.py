from flask import Flask, render_template, request, redirect
import requests
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        word = request.form["word"]
        if word == "":
            return redirect(404)
        api_key = os.environ["API_KEY"]
        req_header = {"Authorization": f"Token {api_key}"}

        word_meaning = requests.get(
            f"https://owlbot.info/api/v4/dictionary/{word}", headers=req_header
        )

        dict_data = word_meaning.json()

        return render_template(
            "index.html",
            data=dict_data,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
