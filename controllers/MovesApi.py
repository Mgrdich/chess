from flask import make_response, jsonify
from flask.views import MethodView
from Util.ErrorUtil import ErrorUtil


class MovesApi(MethodView):
    """ api/moves/<alg_move> """

    @staticmethod
    def get(alg_move):
        """ Return the entire inventory collection """

        alg_validation = ErrorUtil.isAlgNotation('alg_move', alg_move)

        if not alg_validation['valid']:
            return alg_validation['response']

        # TODO make your request here
        return make_response(jsonify({'ks': 'emak'}), 200)

    @staticmethod
    def put(alg_move):
        """ Sets chess play in the Core """

        alg_validation = ErrorUtil.isAlgNotation('alg_move', alg_move)

        if not alg_validation['valid']:
            return alg_validation['response']

        # TODO make your request here
        return make_response(jsonify({'ks': 'emak'}), 200)
