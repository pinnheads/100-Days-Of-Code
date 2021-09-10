from flask import Flask

app = Flask(__name__)

# Python decorators
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
