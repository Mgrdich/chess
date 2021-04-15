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


class MakeMoveApi(MethodView):
    """ api/make-move """

    @staticmethod
    def post(move_str: str):
        """ Sets chess play in the Core """
        data = request.get_json()

        core = ChessCore.getBoard()

        core.move_piece(move_str)

        res = {
            'status': 1,
            'data': data
        }
        return Lib.resJson(res)
