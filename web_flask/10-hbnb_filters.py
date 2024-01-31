#!/usr/bin/python3
# Start a Flask web application
"""
starts a Flask web application
"""
from flask import Flask, render_template, url_for
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def HBNB_Filters():
    """Display all states"""
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', states=states.values(),
                           amenities=amenities.values())


@app.teardown_appcontext
def tear_down(exc):
    """Remove the current session"""
    storage.close()


if __name__ == '__main__':
    app.run()
