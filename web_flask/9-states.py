#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states_and_cities(id=None):
    """Display all states"""
    states = storage.all(State)
    cities = storage.all(City)
    state = None
    for st in states.values():
        if st.id == id:
            state = st
            break

    return render_template('9-states.html', states=states.values(),
                           cities=cities.values(), id=id, state=state)


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current session"""
    storage.close()


if __name__ == '__main__':
    app.run()
