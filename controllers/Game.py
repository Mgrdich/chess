from flask import render_template, session
from flask.views import View

from core.ChessCore import ChessCore


class GameView(View):
    methods = ['GET']

    def dispatch_request(self):
        core = ChessCore()
        if 'board' in session:
            print('get')
            core = ChessCore.getMyBoardSession()  # session instance
        else:
            print('set')
            core.board.push_san("e4")
            core.setMyBoardSession()

        core.printBoard()

        return render_template('main.html')
