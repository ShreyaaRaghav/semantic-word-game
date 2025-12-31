from flask import Flask, redirect, render_template, request, session, url_for
from GloveContexto import glove_similarity, TARGET_WORD as GLOVE_TARGET
from SBERTContexto import sbert_similarity, TARGET_WORD as SBERT_TARGET

app = Flask(__name__)
app.secret_key = "contexto-secret-key"


@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


# ---------- HOME / MAIN GAME ----------
@app.route("/", methods=["GET", "POST"])
def home():

    # Reset on reload OR explicit new game
    if request.method == "GET" and (request.args.get("new") == "1" or not request.referrer):
        session.clear()

    session.setdefault("glove_history", [])
    session.setdefault("sbert_history", [])
    session.setdefault("gave_up_glove", False)
    session.setdefault("gave_up_sbert", False)

    # Handle guess submission
    if request.method == "POST":
        guess = request.form.get("guess")
        model = request.form.get("model")
        scroll = request.form.get("scroll")

        if model == "glove" and not session["gave_up_glove"]:
            response = glove_similarity(guess)
            if "score" in response:
                session["glove_history"].append({
                    "word": response["word"],
                    "score": float(response["score"]),
                    "correct": response["correct"]
                })

        elif model == "sbert" and not session["gave_up_sbert"]:
            response = sbert_similarity(guess)
            if "score" in response:
                session["sbert_history"].append({
                    "word": response["word"],
                    "score": float(response["score"]),
                    "correct": response["correct"]
                })

        session.modified = True
        return redirect(url_for("home") + f"#{scroll}")

    return render_template(
        "index.html",
        glove_history=session["glove_history"],
        sbert_history=session["sbert_history"],
        glove_answer=GLOVE_TARGET if session["gave_up_glove"] else None,
        sbert_answer=SBERT_TARGET if session["gave_up_sbert"] else None
    )


# ---------- GIVE UP ROUTE ----------
@app.route("/giveup", methods=["POST"])
def give_up():
    model = request.form.get("model")

    if model == "glove":
        session["gave_up_glove"] = True
    elif model == "sbert":
        session["gave_up_sbert"] = True

    session.modified = True
    return redirect(url_for("home") + f"#{model}")


if __name__ == "__main__":
    app.run(debug=True)
