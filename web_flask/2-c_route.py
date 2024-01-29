#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run()
