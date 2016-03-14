#!/usr/bin/env python
"""Boilerplate for creating a new OWTF API

Each plugin should run in a docker container and
expose its functionality through an API.
"""

from flask import Flask, request, jsonify, url_for
from commands.ls import Ls

app = Flask(__name__)


@app.route("/")
def index():
    """Index summarizes all endpoints

    Should show all commands and endpoint urls.
    """
    return jsonify( {
        "help": "Hello this is one docker container.",
        "commands": {
            "ls": full_url_for(".ls")
        }
    })

@app.route("/ls", methods=["GET", "POST"])
def ls():
    """ls - List folders

    paths:
        GET
            returns info about the command
        POST
            Runs the command using the post data
            as flags and params
    """
    if request.method == 'POST':
        result = Ls.run(request.get_json(force=True))
        return jsonify(result)
    else:
        return jsonify(Ls.info())

def full_url_for(route):
    """Prints a complete endpoint URL"""
    return url_for(route, _external=True)

if __name__ == "__main__":
    app.run(debug=True)
