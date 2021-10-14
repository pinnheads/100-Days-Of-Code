from flask import Flask, jsonify, render_template, request, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }


@app.route("/")
def home():
    cafes = db.session.query(Cafe).all()
    return render_template("index.html", all_cafes=cafes)


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    param = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=param).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        )


## HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        data = request.form.to_dict()
        new_cafe = Cafe(
            name=data["name"],
            map_url=data["map_url"],
            img_url=data["img_url"],
            location=data["location"],
            seats=data["seats"],
            has_toilet=bool(int(data["has_toilet"])),
            has_wifi=bool(int(data["has_wifi"])),
            has_sockets=bool(int(data["has_sockets"])),
            can_take_calls=bool(int(data["can_take_calls"])),
            coffee_price=data["coffee_price"],
        )
        print(request.form.to_dict())
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


## HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return (
            jsonify(response={"success": "Successfully updated the price."}),
            200,
        )
    else:
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ),
            404,
        )


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id was not found in the database."
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True)
