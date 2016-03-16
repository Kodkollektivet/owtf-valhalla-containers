#!/usr/bin/env python

from flask import Flask, request, jsonify, url_for
from commands.ls import Ls

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({ "key": "value"})

@app.route("/run")
def run():
    return jsonify({ "key": "value"})


if __name__ == "__main__":
    app.run(debug=True)
