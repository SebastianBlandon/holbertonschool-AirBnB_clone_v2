#!/usr/bin/python3
"""
    HBNB Flask!
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route("/c/<text>")
def c_is_fun(text):
    """ C route """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
