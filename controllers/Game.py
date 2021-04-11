from flask import render_template,session
from flask.views import View

from core.ChessCore import ChessCore


class GameView(View):
    methods = ['GET']

    def dispatch_request(self):
        if 'board' not in session:
            ChessCore().setMyBoardSession()

        return render_template('main.html')

