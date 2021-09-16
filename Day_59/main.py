from flask import Flask
from post import Post
from flask.templating import render_template
import requests

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
        post["author"]
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


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
