from dotenv import load_dotenv
from flask import Flask, render_template, g, current_app
import werkzeug
from controllers.Game import GameView
from controllers.MovesApi import MovesApi
from controllers.index import IndexView
import os

from core.ChessCore import ChessCore

werkzeug.cached_property = werkzeug.utils.cached_property

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

# with app.app_context():
#     # within this block, current_app points to app.
#     print(current_app.name)

# Routes

app.add_url_rule('/', view_func=IndexView.as_view('helloWorld'))
app.add_url_rule('/game', view_func=GameView.as_view('game'))
app.add_url_rule('/api/moves/<alg_move>', view_func=MovesApi.as_view('movesApi'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


# g.name = 'ss'

# @app.teardown_appcontext
# def teardown_db():
#     g.pop('chess_core', None)


# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
