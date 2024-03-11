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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def task3(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def task4(n):
    if isinstance(n, int) == True:
        return n
    else:
        return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
