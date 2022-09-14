#!/usr/bin/python3
"""
    List of states!
"""

from models.engine import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', num=n)


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(response):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
