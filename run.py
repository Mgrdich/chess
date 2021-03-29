from dotenv import load_dotenv
from flask import Flask, render_template
import chess
import os

from controllers import Game

load_dotenv()  # take environment variables from .env.

board = chess.Board()

app = Flask(__name__)

app.add_url_rule('/game', view_func=Game.as_view('game'))


# Routes
# in their current directories
@app.route("/")
def index():
    return render_template('index.html')


# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
