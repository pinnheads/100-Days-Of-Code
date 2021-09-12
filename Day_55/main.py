from flask import Flask, render_template
from random import randint
import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = randint(0, 9)
    year = dt.datetime.now().strftime("%Y")
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def age_gender(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(
        f"https://api.genderize.io?name={name}"
    ).json()
    data = response.json()
    name = data["name"]
    age = data["age"]
    gender = gender_response["gender"]

    return render_template("age.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
    blog_data = response.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
