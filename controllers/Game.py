from flask import render_template
from run import api
from flask_restplus import Resource


@api.route('/game/')
class Game(Resource):

    def get(self):
        return render_template('main.html')
