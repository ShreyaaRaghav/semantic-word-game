from flask import Flask, render_template, request, jsonify, session
from GloveContexto import glove_similarity, new_target as new_glove_target
from SBERTContexto import sbert_similarity, new_target as new_sbert_target

app = Flask(__name__)
app.secret_key = "dev-secret-key"

SIM_THRESHOLD = 99.5 
#unused right now, for future work


def new_game():
    session.clear()
    session["glove_target"] = new_glove_target()
    session["sbert_target"] = new_sbert_target()
    session["glove_guesses"] = []
    session["sbert_guesses"] = []
    session["glove_giveup"] = False
    session["sbert_giveup"] = False


@app.route("/", methods=["GET"])
def index():
    new_game()   # reload = new game
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    data = request.json
    model = data["model"]
    guess_word = data["guess"].lower()

    if model == "glove":
        if session["glove_giveup"]:
            return jsonify({"locked": True})

        result = glove_similarity(guess_word, session["glove_target"])
        if "error" in result:
            return jsonify(result)

        session["glove_guesses"].append(
            (result["word"], round(result["score"], 2))
        )

    else:
        if session["sbert_giveup"]:
            return jsonify({"locked": True})

        result = sbert_similarity(guess_word, session["sbert_target"])
        if "error" in result:
            return jsonify(result)

        session["sbert_guesses"].append(
            (result["word"], round(result["score"], 2))
        )

    return jsonify({
        "score": result["score"],
        "correct": result["correct"]
    })


@app.route("/giveup", methods=["POST"])
def giveup():
    model = request.json["model"]

    if model == "glove":
        session["glove_giveup"] = True
        return jsonify({"answer": session["glove_target"]})

    session["sbert_giveup"] = True
    return jsonify({"answer": session["sbert_target"]})


@app.route("/newgame", methods=["POST"])
def restart():
    new_game()
    return jsonify({"status": "reset"})


if __name__ == "__main__":
    app.run(debug=True)
