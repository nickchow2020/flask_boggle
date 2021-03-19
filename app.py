from boggle import Boggle
from flask import Flask,request,render_template,session,redirect,jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'abc123456'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    game_board = boggle_game.make_board()
    session["game_board"] = game_board
    return render_template("home.html",game_board=game_board)


@app.route("/check_word",)
def save_value():
    value = request.args["word"]
    game_board = session["game_board"]
    response = boggle_game.check_valid_word(game_board,value)
    return jsonify({"result": response})