from flask import render_template, session
from flask.views import View

# from core.ChessCore import ChessCore


class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('index.html')
