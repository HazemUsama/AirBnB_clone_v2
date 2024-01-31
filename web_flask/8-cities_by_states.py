#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
@app.route("/cities_by_states", strict_slashes=False)
def show_states_and_cities():
    """Display all states"""
    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states.values())


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current session"""
    storage.close()


if __name__ == '__main__':
    app.run()
