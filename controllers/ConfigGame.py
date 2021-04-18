from flask import render_template, session
from flask.views import View

from Util.Lib import Lib
from Util.Route import Routes
from core.ChessCore import ChessCore


class ConfigGame(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if 'board' not in session:
            core = ChessCore()
            core.setBoardToSession()

        piece_hashes = Lib.getPieceHashes()
        CONFIG_GAME_ROUTE = Routes.getRoute(Routes.Config_Game)

        return render_template('config.html', piece_hashes=piece_hashes, CONFIG_GAME_ROUTE=CONFIG_GAME_ROUTE)
