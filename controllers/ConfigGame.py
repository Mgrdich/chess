from flask import render_template, session, request
from flask.views import View

from Util.Lib import Lib
from Util.Route import Routes
from core.ChessCore import ChessCore


class ConfigGame(View):
    methods = ['GET', 'POST']
    session_key = 'config_fen_board'

    def dispatch_request(self):
        if request.method == 'GET':
            return ConfigGame.get()
        elif request.method == 'POST':
            return ConfigGame.post()

    @staticmethod
    def get():
        if ConfigGame.session_key not in session:
            core = ChessCore()
            core.setBoardToSession()
        else:
            core = ChessCore.getBoard()

        piece_hashes = Lib.getPieceHashes()

        CONFIG_GAME_ROUTE = Routes.getRoute(Routes.Config_Game)

        SUGGESTION_URL = Routes.getRoute(Routes.Api_Moves)

        MOVE_URL = Routes.getRoute(Routes.Api_Make_Move)

        return render_template('config.html',
                               piece_hashes=piece_hashes,
                               CONFIG_GAME_ROUTE=CONFIG_GAME_ROUTE,
                               SUGGESTION_URL=SUGGESTION_URL,
                               MOVE_URL=MOVE_URL,
                               FEN=core.board.fen()
                               )

    @staticmethod
    def post():
        data = request.get_json()

        core = ChessCore(data['fen'])
        core.setBoardToSession(session_key=ConfigGame.session_key)

        res = {
            'status': 1,
            'fen': data['fen']
        }

        return Lib.resJson(res)
