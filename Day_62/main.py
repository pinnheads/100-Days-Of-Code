from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Location Url", validators=[DataRequired(), URL(message="Invalid Url")]
    )
    open_time = StringField("Open", validators=[DataRequired()])
    close_time = StringField("Close", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()],
    )
    wifi_strength = SelectField(
        "Wifi Strength Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()],
    )
    power_socket = SelectField(
        "Power Socket Availability",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_location = form.location.data
        cafe_open = form.open_time.data
        cafe_close = form.close_time.data
        cafe_coffee_rating = form.coffee_rating.data
        cafe_wifi_rating = form.wifi_strength.data
        cafe_power_socket = form.power_socket.data

        with open("cafe-data.csv", newline="", mode="a+") as csv_file:
            csv_file.write(
                f"\n{cafe_name},{cafe_location},{cafe_open},{cafe_close},{cafe_coffee_rating},{cafe_wifi_rating},{cafe_power_socket}"
            )
        return redirect(url_for("cafes"))

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
