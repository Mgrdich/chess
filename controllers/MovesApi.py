from flask import make_response, jsonify
from flask.views import MethodView
from core.ChessUtil import ChessUtil


class MovesApi(MethodView):
    """ api/moves/<alg_move> """

    def get(self, alg_move):
        """ Return the entire inventory collection """
        if not ChessUtil.isAlgebraicNotation(alg_move):
            return make_response(jsonify({
                'status': 0,
                'errors': {
                    'alg_move': 'not a valid alg_move'
                }
            }
            ), 200)

        return make_response(jsonify({'ks': 'emak'}), 200)

    def put(self, alg_move):
        """ Return the entire inventory collection """
        if not ChessUtil.isAlgebraicNotation(alg_move):
            return make_response(jsonify({
                'status': 0,
                'errors': {
                    'alg_move': 'not a valid alg_move'
                }
            }
            ), 200)

        print('put', alg_move)
        return make_response(jsonify({'ks': 'emak'}), 200)
