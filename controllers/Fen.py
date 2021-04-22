from flask import render_template
from flask.views import View

from Util.Route import Routes


class Fen(View):
    methods = ['GET']

    def dispatch_request(self):
        CONFIG_ROUTE = Routes.getRoute(Routes.Config_Game)
        return render_template('fen.html', CONFIG_ROUTE=CONFIG_ROUTE)
