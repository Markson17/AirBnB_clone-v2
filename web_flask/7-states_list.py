#!/usr/bin/python3
"""
Start a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a HTML page: (inside the tag BODY) """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.teardown_appcontext
def remove_session(response_or_exc):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
