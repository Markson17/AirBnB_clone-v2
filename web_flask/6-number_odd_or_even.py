#!/usr/bin/python3

""" Start a Flask web application with a route /number_odd_or_even/<n> """

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Print Hello HBNB! """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print Hello HBNB! """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer.
    The page displays an H1 tag: 'Number: n' inside the tag BODY.
    """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer.
    The page displays an H1 tag: 'Number: n is even|odd' inside the tag BODY.
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)