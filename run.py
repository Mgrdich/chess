from dotenv import load_dotenv
from flask import Flask, render_template
import chess
import os

load_dotenv()  # take environment variables from .env.

board = chess.Board()

app = Flask(__name__)


# Routes
@app.route("/")
def index():
    return render_template('main.html')


# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('HOST'), debug=True)
