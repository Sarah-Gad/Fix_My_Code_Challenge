#!/usr/bin/python3
""" Index view """
from flask import jsonify
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

@app_views.route('/status', methods=['GET'])
def status():
    """ Status of the web server """
    return jsonify({"status": "OK"})
