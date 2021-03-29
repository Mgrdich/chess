from flask import render_template
from flask.views import View
from run import app


class Game(View):
    methods = ['GET']

    def dispatch_request(self):
        return render_template('main.html')


app.add_url_rule('/game', view_func=Game.as_view('game'))
