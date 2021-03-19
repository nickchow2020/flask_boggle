from boggle import Boggle
from flask import Flask,request,render_template,session,redirect,jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'abc123456'
toolbar = DebugToolbarExtension(app)

plays = 1
scores = []

@app.route('/')
def hello_world():
    """Implement the home page sections with jinja and render it's template"""
    game_board = boggle_game.make_board()
    session["game_board"] = game_board
    return render_template("home.html",game_board=game_board)


@app.route("/check_word",)
def save_value():
    """Check for words validation"""
    value = request.args["word"]
    game_board = session["game_board"]
    response = boggle_game.check_valid_word(game_board,value.upper())
    return jsonify({"result": response})


@app.route("/post_score",methods=["POST"])
def save_score():  
        """Handle post request to score the play and score into the session"""
        current_score = request.get_json("score")
        scores.append(current_score)

        session["the_scores"] = scores
        session["the_plays"] = plays

        the_scores = session.get("the_scores",[])
        the_plays = session.get("the_plays",1)

        return jsonify(current_score == max(the_scores))