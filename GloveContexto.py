import pandas as pd
import numpy as np
import random
import spacy

# ---------- LOAD DATA ----------
df = pd.read_csv("dict.csv", header=None, names=["word"])
df["word"] = df["word"].astype(str).str.lower().str.strip()
df = df[df["word"].str.isalpha()]

nlp = spacy.load("en_core_web_md")

valid_words = [w for w in df["word"] if nlp.vocab[w].has_vector]
if not valid_words:
    raise RuntimeError("No GloVe vectors found")


# ---------- UTILS ----------
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ---------- TARGET ----------
def new_target():
    return random.choice(valid_words)


# ---------- SIMILARITY ----------
def glove_similarity(guess: str, target_word: str):
    guess = guess.lower().strip()

    if not guess.isalpha():
        return {"error": "Invalid"}

    if not nlp.vocab[guess].has_vector:
        return {"error": "OOV"}

    target_vec = nlp.vocab[target_word].vector
    guess_vec = nlp.vocab[guess].vector

    sim = cosine_sim(target_vec, guess_vec)
    score = 100 / (1 + np.exp(-10 * (sim - 0.35)))

    # threshold-based correctness
    correct = (guess == target_word) or (sim >= 0.98)

    return {
    "word": str(guess),
    "score": float(score),
    "correct": bool(correct)
     }