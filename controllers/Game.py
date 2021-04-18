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

        piece_hashes = Lib.getPieceHashes()



        return render_template('main.html', piece_hashes=piece_hashes)
