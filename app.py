#!/usr/bin/env python

import configparser
import os
from subprocess import Popen, PIPE
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

# Process should be a que to enable multiple subprocesses
process = None


@app.route("/")
def index():
    """Returns information about the command and possible routes"""
    return jsonify({"description": read_config('description')})


@app.route("/run")
def run():
    """Starts the subproccess"""
    global process

    script = read_config('command')
    process = Popen([script], stdout=PIPE)
    return jsonify({"message": "Subprocess started"})


@app.route("/result")
def result():
    """Read the result from the subprocess """
    global process

    if not process:
        return jsonify({"response": "No running proccess"})
    elif not process.poll() == 0:
        return jsonify({"response": "Process still running"})

    res = process.communicate()
    process.kill()
    process = None
    return jsonify({"response": str(res[0])})


def read_config(key):
    """Read key from config"""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['main'][key]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
