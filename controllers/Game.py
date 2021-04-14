from flask import render_template, session
from flask.views import View

from Util.Lib import Lib
from core.ChessCore import ChessCore


class GameView(View):
    methods = ['GET']

    def dispatch_request(self):
        if 'board' not in session:
            core = ChessCore()
            core.setBoardToSession()

        piece_hashes = {}

        for i in ChessCore.WHITE_PIECE_SYMBOLS:
            piece_type = 'w' + i
            piece_hashes[piece_type] = Lib.transform_board_piece(piece_type)

        for i in ChessCore.BLACK_PIECE_SYMBOLS:
            piece_type = 'b' + i.upper()
            piece_hashes[piece_type] = Lib.transform_board_piece(piece_type)

        return render_template('main.html', piece_hashes=piece_hashes)
