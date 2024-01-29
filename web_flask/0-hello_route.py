#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Return Hello HBNB"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
