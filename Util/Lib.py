from flask import make_response, jsonify

from core.ChessCore import ChessCore

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
            'status': 0,
            'error': msg
        }), 304)

    @staticmethod
    def getPieceHashes() -> object:
        piece_hashes = {}

        # wP -> P
        # bK -> k
        for i in ChessCore.WHITE_PIECE_SYMBOLS:
            piece_type = 'w' + i
            piece_hashes[piece_type] = i.lower()

        for j in ChessCore.BLACK_PIECE_SYMBOLS:
            piece_type = 'b' + j
            piece_hashes[piece_type] = j

        return piece_hashes
