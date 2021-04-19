from flask import request
from flask.views import MethodView
from Util.Lib import Lib
from Util.ErrorUtil import ErrorUtil
from controllers.ConfigGame import ConfigGame
from controllers.Game import GameView
from core.ChessCore import ChessCore


# Possible Move
class MovesApi(MethodView):
    """ api/moves/<alg_move> """

    @staticmethod
    def get(alg_move: str):
        """ Return the entire inventory collection """

        alg_validation = ErrorUtil.isAlgNotation('alg_move', alg_move)

        if not alg_validation['valid']:
            return alg_validation['response']

        page_action = request.referrer.rsplit('/', 1)[-1]

        # TODO put some kind of place for all this information to be stored
        session_key = ConfigGame.session_key if page_action == 'config-game' else GameView.session_key

        print(session_key)

        core = ChessCore.getBoard(session_key)

        print(core.board)

        res = {
            'status': 1,
            'result': core.getPossibleMovesAlg(alg_move).tolist()
        }

        return Lib.resJson(res)


# Moves
class MakeMoveApi(MethodView):
    """ api/make-move """

    @staticmethod
    def post():
        """ Sets chess play in the Core """
        data = request.get_json()

        required_validation = ErrorUtil.isRequired('move', data)

        if not required_validation['valid']:
            return required_validation['response']

        move_validation = ErrorUtil.isValidMoveNotation('move', data['move'])

        if not move_validation['valid']:
            return move_validation['response']

        page_action = request.referrer.rsplit('/', 1)[-1]

        # TODO put some kind of place for all this information to be stored
        session_key = ConfigGame.session_key if page_action == 'config-game' else GameView.session_key

        core = ChessCore.getBoard(session_key)

        parsed_move_validation = ErrorUtil.isValidMove(core.board, 'move', data['move'])

        if not parsed_move_validation['valid']:
            return parsed_move_validation['response']

        core.move_piece(data['move'])

        res = {
            'status': 1,
            'data': data
        }
        return Lib.resJson(res)
