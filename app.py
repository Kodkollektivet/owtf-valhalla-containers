#!/usr/bin/env python

import configparser
from subprocess import check_output
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({ "description": read_config('description')})

@app.route("/run")
def run():
    command = read_config('command')
    res = check_output([command, "-l"])
    print(res)
    return jsonify({ "response": str(res) })

def read_config(key):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['main'][key]


if __name__ == "__main__":
    app.run(debug=True)

