#!/usr/bin/python3

""" Start a Flask web application with a route /hbnb """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Print Hello HBNB! """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print Hello HBNB! """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)