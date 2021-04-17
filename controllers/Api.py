from flask import request
from flask.views import MethodView
from Util.Lib import Lib
from Util.ErrorUtil import ErrorUtil
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

        core = ChessCore.getBoard()

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

        required_validation = ErrorUtil.isRequired('move', data.move)

        if not required_validation['valid']:
            return required_validation['response']

        move_validation = ErrorUtil.isValidMoveNotation('move', data.move)

        if not move_validation['valid']:
            return move_validation['response']

        core = ChessCore.getBoard()

        parsed_move_validation = ErrorUtil.isValidMove(core, 'move', data.move)

        if not parsed_move_validation['valid']:
            return parsed_move_validation['response']

        core.move_piece(data.move)

        res = {
            'status': 1,
            'data': data
        }
        return Lib.resJson(res)
