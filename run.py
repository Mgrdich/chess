from flask import Flask, render_template
import chess
import chess.svg

# TODO replace the svg with normal html things


board = chess.Board()

app = Flask(__name__)


# Routes
@app.route("/")
def index():
    svg = chess.svg.board(board=board)
    return render_template('main.html', svg=svg)


# Web server config
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
