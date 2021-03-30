from dotenv import load_dotenv
from flask import Flask, render_template
import werkzeug
from controllers.Game import GameView
from controllers.index import IndexView
import chess
import os

werkzeug.cached_property = werkzeug.utils.cached_property

load_dotenv()  # take environment variables from .env.

board = chess.Board()

app = Flask(__name__)

# Routes

app.add_url_rule('/', view_func=IndexView.as_view('helloWorld'))
app.add_url_rule('/game', view_func=GameView.as_view('game'))


@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return render_template('error.html', error=error), 404


# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
