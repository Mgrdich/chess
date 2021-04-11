from flask import render_template, session
from flask.views import View
from core.ChessCore import ChessCore


class GameView(View):
    methods = ['GET']

    def dispatch_request(self):
        session['board'] = ChessCore()
        return render_template('main.html')

