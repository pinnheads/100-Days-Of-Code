from datetime import time
import os
import smtplib
from flask import Flask, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from post import Post
from flask.templating import render_template
import requests


my_email = os.environ["MY_SMTP_EMAIL"]
password = os.environ["MY_SMTP_PASSWORD"]


def send_mail(name, email, phone, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("Connection Established")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="utsavdeep01@gmail.com",
            msg=f"Subject:Mail from Blog Site\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n",
        )
        print("Mail has been sent. Check your inbox...")


app = Flask(__name__)

posts = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()
post_objects = []
for post in posts:
    post_obj = Post(
        post["id"],
        post["title"],
        post["subtitle"],
        post["body"],
        post["date"],
        post["image"],
        post["author"],
    )
    post_objects.append(post_obj)
print(post_objects)


@app.route("/")
def home():
    return render_template("index.html", posts=post_objects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(message)
        send_mail(name=name, email=email, phone=phone, message=message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
