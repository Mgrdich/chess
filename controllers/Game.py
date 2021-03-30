from flask import render_template, make_response
from flask.views import View


class Game(View):
    methods = ['GET']

    def dispatch_request(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('main.html'), 200, headers)

