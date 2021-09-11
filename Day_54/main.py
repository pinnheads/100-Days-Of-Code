from flask import Flask


def logging_decorator(function):
    def wrapper(*args):
        print(function.__name__)
        return function()

    # To use the same decorator multiple time rename the wrapper function
    wrapper.__name__ = function.__name__
    return wrapper


def make_bold(function):
    def wrapper_function(**kwargs):
        return "<b>" + function() + "</b>"

    wrapper_function.__name__ = function.__name__
    return wrapper_function


def make_italics(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"

    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"

    return wrapper_function


app = Flask(__name__)

# Python decorators
@app.route("/")
@logging_decorator
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@logging_decorator
@make_bold
@make_italics
@make_underline
def say_bye():
    return "Bye!"


@app.route("/<name>")
@make_bold
def greet(name):
    return f"<h1>Hello {name}!</h1>"


@app.route("/<name>/<int:number>")
@logging_decorator
def greet_again(name, number):
    return f"<h1>Hello {name}, you are {number} years old!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
