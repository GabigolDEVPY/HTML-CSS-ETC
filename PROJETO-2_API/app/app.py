from flask import Blueprint, Flask


def createAPP():
    app = Flask(__name__)
    return app