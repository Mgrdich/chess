from flask import make_response, jsonify, g
from flask.views import MethodView
from Util.Lib import Lib
from Util.ErrorUtil import ErrorUtil


class MovesApi(MethodView):
    """ api/moves/<alg_move> """

    @staticmethod
    def get(alg_move: str):
        """ Return the entire inventory collection """

        alg_validation = ErrorUtil.isAlgNotation('alg_move', alg_move)

        if not alg_validation['valid']:
            return alg_validation['response']

        print(g.chess_core)
        res = {
            'status': 1,
            'result': g.chess_core.getPossibleMovesAlg(alg_move)
        }

        return Lib.resJson(res)

    @staticmethod
    def put(alg_move: str):
        """ Sets chess play in the Core """

        alg_validation = ErrorUtil.isAlgNotation('alg_move', alg_move)

        if not alg_validation['valid']:
            return alg_validation['response']

        # TODO make your request here
        return make_response(jsonify({'ks': 'emak'}), 200)
