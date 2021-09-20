from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Title %r>" % self.title


db.create_all()
# new_book = Book(title="Atomic Habits", author="James Clear", rating=8.9)
# new_book2 = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book2)
# db.session.commit()

# Read all
all_books = db.session.query(Book).all()
# print(all_books)
# Read a particular record
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)
# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()


# Update A Record By PRIMARY KEY
# book_id = 5
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()


# Delete A Particular Record By PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


@app.route("/")
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form.get("b_name"),
            author=request.form.get("b_author"),
            rating=request.form.get("b_rating"),
        )
        db.session.add(new_book)
        db.session.commit()
    return render_template("add.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book_id = id
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form.get("new_rating")
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", id=id)


@app.route("/delete/<int:id>")
def delete(id):
    book_id = id
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
