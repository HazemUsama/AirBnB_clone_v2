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
@app.route("/states_list", strict_slashes=False)
def show_states():
    """Display all states"""
    states = storage.all(State)
    for state in states.values():
        print(state.id, state.name)

    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current session"""
    storage.close()


if __name__ == '__main__':
    app.run()
