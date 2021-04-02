from flask import make_response, jsonify
from flask.views import MethodView


class MovesApi(MethodView):
    """ api/moves/<alg_move> """

    def get(self, alg_move):
        """ Return the entire inventory collection """
        print('get', alg_move)
        return make_response(jsonify({'ks': 'emak'}), 200)

    def put(self, alg_move):
        """ Return the entire inventory collection """
        print('put', alg_move)
        return make_response(jsonify({'ks': 'emak'}), 200)
