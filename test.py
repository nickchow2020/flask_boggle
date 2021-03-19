from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_home(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn("<h1>Boggle Game</h1>",html)
            self.assertEqual(len(session["game_board"]),5)

    def test_check_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["game_board"] = [
                                    ["A", "B", "C", "D", "E"]]
            res = client.get("check_word?word=e")
            self.assertEqual(res.status_code,200)
            self.assertEqual(res.json["result"],"ok")

    def test_post_score(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session["the_scores"] = [4,5,6,7]
    
            res = client.post("/post_score",data={"score":10,"plays":1})

            self.assertEqual(res.status_code,400)