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
        if 'board' not in session:
            core = ChessCore()
            core.setBoardToSession()

        piece_hashes = Lib.getPieceHashes()

        CONFIG_GAME_ROUTE = Routes.getRoute(Routes.Config_Game)

        SUGGESTION_URL = Routes.getRoute(Routes.Api_Moves)

        MOVE_URL = Routes.getRoute(Routes.Api_Make_Move)

        return render_template('config.html',
                               piece_hashes=piece_hashes,
                               CONFIG_GAME_ROUTE=CONFIG_GAME_ROUTE,
                               SUGGESTION_URL=SUGGESTION_URL,
                               MOVE_URL=MOVE_URL
                               )

    @staticmethod
    def post():
        pass
