import pandas as pd
import numpy as np
import random
import spacy

df = pd.read_csv("dict.csv", header=None, names=["word"])
df["word"] = df["word"].astype(str).str.lower().str.strip()
df = df[df["word"].str.isalpha()]

nlp = spacy.load("en_core_web_md")

valid_words = [w for w in df["word"] if nlp.vocab[w].has_vector]

if not valid_words:
    raise RuntimeError("No GloVe vectors found")

TARGET_WORD = random.choice(valid_words)
TARGET_VEC = nlp.vocab[TARGET_WORD].vector


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def glove_similarity(guess):
    guess = guess.lower().strip()
    if not guess.isalpha():
        return {"error": "Invalid"}

    if not nlp.vocab[guess].has_vector:
        return {"error": "OOV"}

    sim = cosine_sim(TARGET_VEC, nlp.vocab[guess].vector)
    score = 100 / (1 + np.exp(-10 * (sim - 0.35)))

    return {
        "word": guess,
        "score": float(score),
        "correct": guess == TARGET_WORD
    }
