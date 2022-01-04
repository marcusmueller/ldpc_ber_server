#!/usr/bin/python

from flask import Flask
from web_utils import *
from worker import Worker

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route("/api/codes", methods=['GET'])
def get_codes():
    return jsonify(worker.codes)

@app.route("/api/status", methods=['GET'])
    return jsonify(worker.status)

def run(config, debug):
    worker = Worker(config, debug)
    app.run(debug=debug)
