from dotenv import load_dotenv
from flask import Flask
import werkzeug
from controllers.Game import Game
from controllers.index import HelloWorld
import chess
import os

werkzeug.cached_property = werkzeug.utils.cached_property


load_dotenv()  # take environment variables from .env.

board = chess.Board()

app = Flask(__name__)

# Routes
app.add_url_rule('/', view_func=HelloWorld.as_view('helloWorld'))
app.add_url_rule('/game', view_func=Game.as_view('game'))

# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
