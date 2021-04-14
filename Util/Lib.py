from flask import make_response, jsonify

"""
    Universal Utility store 
"""


class Lib:
    def __init__(self):
        pass

    @staticmethod
    def resJson(obj: object, status: int = 200):
        return make_response(jsonify(obj), status)

    @staticmethod
    def resInvalidJson(msg: str):
        return make_response(jsonify({
            'error': msg
        }), 304)

    @staticmethod
    def transform_board_piece(piece: str) -> str:
        # wP -> P
        # bK -> k
        if piece[0] == 'w':
            return piece[1]

        return piece[1].lower()
