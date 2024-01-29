#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def C_is_fun(text):
    """display “C ”, followed by the value of the text"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/<string:text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python(text="is cool"):
    """display Python, followed by the value of the text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def if_num(n):
    """display n, if it's a number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def if_num_disp(n):
    """display template, if it's a number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
