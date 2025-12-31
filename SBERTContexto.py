import pandas as pd
import random
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("dict.csv", header=None, names=["word"])
df["word"] = df["word"].astype(str).str.lower().str.strip()
df = df[df["word"].str.isalpha()]

words = df["word"].tolist()
if not words:
    raise RuntimeError("Empty dictionary")

model = SentenceTransformer("all-MiniLM-L12-v2")

TARGET_WORD = random.choice(words)
TARGET_EMB = model.encode(TARGET_WORD, normalize_embeddings=True)


def sbert_similarity(guess):
    guess = guess.lower().strip()
    if not guess.isalpha():
        return {"error": "Invalid"}

    emb = model.encode(guess, normalize_embeddings=True)
    sim = cosine_similarity([TARGET_EMB], [emb])[0][0]
    score = 100 / (1 + np.exp(-12 * (sim - 0.5)))

    return {
        "word": guess,
        "score": float(score),
        "correct": guess == TARGET_WORD
    }
