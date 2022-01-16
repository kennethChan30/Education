from flask import Flask
from flask import request
from simplify_index import simplify_index

app = Flask(__name__)

@app.route("/")
def index():
    question = request.args.get("celsius", "")
    ans = simplify_index(question)
    return (
        """<form action="" method="get">
                <input type="text" name="celsius">
                <input type="submit" value="Convert">
            </form>"""
        + "the simplyfied form of " + question + " is "
        + ans
    )


if __name__ == '__main__':
    app.run()