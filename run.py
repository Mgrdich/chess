from dotenv import load_dotenv
from flask import Flask, render_template
import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api, Resource
import chess
import os

load_dotenv()  # take environment variables from .env.

board = chess.Board()

app = Flask(__name__)
api = Api(app=app)


@api.route('/')
class HelloWorld(Resource):
    def get(self):
        return render_template('index.html')


# Web server config
if __name__ == "__main__":
    app.run(host=os.environ.get('HOST'), port=os.environ.get('PORT'), debug=True)
