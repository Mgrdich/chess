from flask import render_template, session
from flask.views import View

from Util.Lib import Lib
from Util.Route import Routes
from core.ChessCore import ChessCore


class GameView(View):
    methods = ['GET']
    session_key = 'board'

    def dispatch_request(self):
        if GameView.session_key not in session:
            core = ChessCore()
            core.setBoardToSession()
        else:
            core = ChessCore.getBoard()

        piece_hashes = Lib.getPieceHashes()

        SUGGESTION_URL = Routes.getRoute(Routes.Api_Moves)

        MOVE_URL = Routes.getRoute(Routes.Api_Make_Move)

        return render_template('main.html',
                               piece_hashes=piece_hashes,
                               MOVE_URL=MOVE_URL,
                               SUGGESTION_URL=SUGGESTION_URL,
                               FEN=core.board.fen()
                               )
