from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "any-secret-key-you-choose"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = b"W\x07\xe2\xec\xb1Fk\\\xd1A@\x92Wd\x1f\x95"
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return render_template(
        "index.html", logged_in=current_user.is_authenticated
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=generate_password_hash(
                password=request.form.get("password"),
                method="pbkdf2:sha256",
                salt_length=8,
            ),
        )
        if User.query.filter_by(email=request.form.get("email")).first():
            flash(
                message=f"Email already exists! Login with the email.",
                category="error",
            )
            return redirect(url_for("login"))
        else:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(
                url_for(
                    "secrets",
                    name=current_user.name,
                    logged_in=current_user.is_authenticated,
                )
            )
    return render_template(
        "register.html", logged_in=current_user.is_authenticated
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email entered.
        user = User.query.filter_by(email=email).first()
        if not user:
            flash(
                message="Email not found. Try again!",
                category="error",
            )
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash(message="Invalid Password!! Try again", category="error")
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template(
        "login.html", logged_in=current_user.is_authenticated
    )


@app.route("/secrets")
@login_required
def secrets():
    return render_template(
        "secrets.html",
        name=current_user.name,
        logged_in=current_user.is_authenticated,
    )


@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash(message="Successfully Logged out", category="info")
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
