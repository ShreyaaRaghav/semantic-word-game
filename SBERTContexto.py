import pandas as pd
import random
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- LOAD DATA ----------
df = pd.read_csv("dict.csv", header=None, names=["word"])
df["word"] = df["word"].astype(str).str.lower().str.strip()
df = df[df["word"].str.isalpha()]

words = df["word"].tolist()
if not words:
    raise RuntimeError("Empty dictionary")

model = SentenceTransformer("all-MiniLM-L12-v2")


# ---------- TARGET ----------
def new_target():
    return random.choice(words)


# ---------- SIMILARITY ----------
def sbert_similarity(guess: str, target_word: str):
    guess = guess.lower().strip()

    if not guess.isalpha():
        return {"error": "Invalid"}

    target_emb = model.encode(target_word, normalize_embeddings=True)
    guess_emb = model.encode(guess, normalize_embeddings=True)

    sim = cosine_similarity([target_emb], [guess_emb])[0][0]
    score = 100 / (1 + np.exp(-12 * (sim - 0.5)))

    # threshold-based correctness
    correct = (guess == target_word) or (sim >= 0.97)

    return {
    "word": str(guess),
    "score": float(score),
    "correct": bool(correct)

      }