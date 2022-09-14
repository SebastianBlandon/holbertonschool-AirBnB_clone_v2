#!/usr/bin/python3
"""
    List of states with Flask application!
"""

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown(response):
    storage.close()


@app.route('/states_list')
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
