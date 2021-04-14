from flask.views import MethodView
from Util.Lib import Lib
from Util.ErrorUtil import ErrorUtil
from core.ChessCore import ChessCore


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

    @staticmethod
    def put(move_str: str):
        """ Sets chess play in the Core """

        core = ChessCore.getBoard()

        res = {
            'status': 1,
            'result': [],
            'move': move_str
        }
        return Lib.resJson(res)
