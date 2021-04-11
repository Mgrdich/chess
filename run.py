from dotenv import load_dotenv
from flask import Flask, render_template, url_for, redirect
import werkzeug
from controllers.Game import GameView
from controllers.MovesApi import MovesApi
from controllers.index import IndexView
import os

# TODO add session and store it in board or data related to that page
# TODO maybe integrate it into the move and core API get Setter and Getter


werkzeug.cached_property = werkzeug.utils.cached_property

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

# Routes

app.add_url_rule('/', view_func=IndexView.as_view('helloWorld'))
app.add_url_rule('/game', view_func=GameView.as_view('game'))
app.add_url_rule('/api/moves/<alg_move>', view_func=MovesApi.as_view('movesApi'))


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
