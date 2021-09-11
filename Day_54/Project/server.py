from flask import Flask
from random import randint


RANDOM_NUM = randint(0, 9)
print(RANDOM_NUM)
app = Flask(__name__)


def format_result(fn):
    def wrapper(*args, **kwargs):
        guess = fn(kwargs["user_guess"])
        if guess > RANDOM_NUM and guess < 10:
            return (
                "<h1 style='color: purple'>Too High, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
            )
        elif guess < RANDOM_NUM:
            return (
                "<h1 style='color: crimson'>Too Low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
            )
        elif guess == RANDOM_NUM:
            return (
                "<h1 style='color: #00a884'>You Found Me :)</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
            )
        elif guess >= 10:
            return (
                "<h1 style='color: red'>What is this???</h1>"
                "<img src='https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif?cid=ecf05e471utt6hjtxhj0jphydam1s863djwoimizgekdo3fe&rid=giphy.gif&ct=g'>"
            )

    return wrapper


@app.route("/")
def home_page():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
    )


@app.route("/<int:user_guess>")
@format_result
def check_number(user_guess):
    return user_guess


if __name__ == "__main__":
    app.run(debug=True)
