#!/usr/bin/python3

"""Triple quotes for documentation"""

from flask import Flask

"""More documentation because idk where they want it"""

app = Flask(__name__)

"""Documentation here?"""


@app.route("/", strict_slashes=False)
def task0():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def task1():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def task2(text):
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
