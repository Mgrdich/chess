from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect  # , session
import werkzeug
# from flask.sessions import SecureCookieSessionInterface

from Util.Route import Routes

from controllers.ConfigGame import ConfigGame
from controllers.Game import GameView
from controllers.Api import MovesApi, MakeMoveApi
from controllers.Fen import Fen
from controllers.index import IndexView
import os

werkzeug.cached_property = werkzeug.utils.cached_property

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

# Cookie

# where `app` is your Flask Application name.
# session_cookie = SecureCookieSessionInterface().get_signing_serializer(app)

# Routes

app.add_url_rule(Routes.getRoute(Routes.Index), view_func=IndexView.as_view('helloWorld'))
app.add_url_rule(Routes.getRoute(Routes.Game_Url), view_func=GameView.as_view('game'))
app.add_url_rule(Routes.getRoute(Routes.Config_Game), view_func=ConfigGame.as_view('configGame'))
app.add_url_rule(Routes.getRoute(Routes.Api_Make_Move), view_func=MakeMoveApi.as_view('makeMoveApi'))
app.add_url_rule(Routes.getRoute(Routes.Fen), view_func=Fen.as_view('Fen'))
app.add_url_rule(Routes.getRoute(Routes.Api_Moves), view_func=MovesApi.as_view('movesApi'))


# middlewares
# @app.after_request
# def cookies(response):
#     print(session_cookie)
#     same_cookie = session_cookie.dumps(dict(session))
#     response.headers.add("Set-Cookie", f"my_cookie={same_cookie}; Secure; HttpOnly; SameSite=None; Path=/;")
#     return response


@app.errorhandler(404)
def page_not_found(error):
    redirect(url_for('404'))
    return render_template('error.html', error=error), 404


# @app.teardown_appcontext
# def teardown_db():
#     # clear the session cookie here
#     return


# Web server config
if __name__ == "__main__":
    app.secret_key = os.environ.get('SECRET_KEY')
    app.config['SESSION_TYPE'] = os.environ.get('SESSION_TYPE')
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
