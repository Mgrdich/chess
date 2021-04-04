from flask import make_response, jsonify

"""
    Universal Utility store 
"""


class Util:
    def __init__(self):
        pass

    @staticmethod
    def resJson(obj: object, status: int = 200):
        return make_response(jsonify(obj), status)
