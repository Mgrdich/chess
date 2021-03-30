from flask import render_template, make_response
from flask.views import View


class HelloWorld(View):
    methods = ['GET']

    def dispatch_request(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)
