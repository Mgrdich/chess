from flask import render_template, session, request
from flask.views import View

from Util.BoardSessions import BoardSessions
from Util.Lib import Lib
from Util.Route import Routes
from core.ChessCore import ChessCore


class ConfigGame(View):
    methods = ['GET', 'POST']
    session_key = BoardSessions.getBoardSession(Routes.Config_Game)

    def dispatch_request(self):
        if request.method == 'GET':
            return ConfigGame.get()
        elif request.method == 'POST':
            return ConfigGame.post()

    @staticmethod
    def get():

        if ConfigGame.session_key in session:
            core = ChessCore.getBoard(ConfigGame.session_key)
        else:
            core = ChessCore()
            core.setBoardToSession(session_key=ConfigGame.session_key)

        piece_hashes = Lib.getPieceHashes()

        CONFIG_GAME_ROUTE = Routes.getRoute(Routes.Config_Game)

        SUGGESTION_URL = Routes.getRoute(Routes.Api_Moves)

        MOVE_URL = Routes.getRoute(Routes.Api_Make_Move)

        FEN = core.board.fen() if core else ''

        return render_template('config.html',
                               piece_hashes=piece_hashes,
                               CONFIG_GAME_ROUTE=CONFIG_GAME_ROUTE,
                               SUGGESTION_URL=SUGGESTION_URL,
                               MOVE_URL=MOVE_URL,
                               FEN=FEN
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
