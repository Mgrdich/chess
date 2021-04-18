from flask import render_template
from flask.views import View

from Util.Route import Routes


class IndexView(View):
    methods = ['GET']

    def dispatch_request(self):
        GAME_ROUTE = Routes.Game_Url
        CONFIG_ROUTE = Routes.Config_Game
        return render_template('index.html', GAME_ROUTE=GAME_ROUTE, CONFIG_ROUTE=CONFIG_ROUTE)
