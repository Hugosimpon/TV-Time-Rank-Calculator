from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    board = request.args.get("board", "Board 1")
    return render_template("index.html", board=board)

if __name__ == "__main__":
    app.run(debug=True)