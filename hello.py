from flask import Flask
from flask import request
import re

app = Flask(__name__)

@app.route("/")
def index():
    question = request.args.get("celsius", "")
    return (
        """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + question
    )

if __name__ == '__main__':
    app.run()