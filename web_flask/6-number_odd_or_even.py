#!/usr/bin/python3

"""Triple quotes for documentation"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def task4(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def task5(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def task6(n):
    if (n % 2) == 0:
        return render_template("6-number_odd_or_even.html", number=n, oe="even")
    else:
        return render_template("6-number_odd_or_even.html", number=n, oe="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
