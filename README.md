CONTEXTO — Semantic Word Guessing Game 
=======================================

> A full-stack semantic word guessing game inspired by Contexto — but built from scratch by me, end-to-end.This is not a letter-matching game like Wordle. Here, guesses are ranked by meaning.

### You can choose between **GloVe** and **SBERT** embeddings and see how semantic similarity actually behaves in real time.

What This Project Is
--------------------

*   A complete **full-stack project**
    
*   Backend built with **Python (Flask)**
    
*   Frontend built with **HTML / CSS / JavaScript**
    
*   Semantic similarity using **two different NLP models**
    
*   Interactive, scrollable web UI
    
*   Built, broken, fixed, and shipped by me lol
    

How the Game Works
------------------

1.  A **target word** is randomly selected from a dataset_(examples: relationship, foundation, procrastination etc etc)_
    
2.  You type guesses into the web app i made named Contexto
    
3.  Each guess is embedded using the selected model but button or scroll
    
4.  **Cosine similarity** is calculated between your guess and the target
    
5.  You receive ranked feedback based on semantic closeness with the word you entered
    
6.  Closer meaning = More %age near 100
    

> No spelling tricks. No letters.Only vibes, vectors, and meaning.

Embedding Options (Core Feature)
--------------------------------

You can switch between **two embedding models** directly from the UI.

### 🔹 GloVe

*   Static word embeddings
    
*   Faster and lighter
    
*   Good for understanding classic semantic relationships
    

### 🔹 SBERT (Sentence-BERT)

*   Context-aware transformer embeddings
    
*   Much deeper semantic understanding
    
*   Slower, but significantly more accurate
    

> This allows direct comparison of how different embeddings behave on the same task.

Tech Stack
----------

### Backend

*   Python 3
    
*   Flask
    
*   NumPy
    
*   scikit-learn (cosine similarity)
    

### NLP

*   GloVe word embeddings
    
*   Sentence Transformers (SBERT)
    

### Frontend

*   HTML
    
*   CSS
    
*   JavaScript
    

Running the Project Locally
---------------------------

### Clone the repository
`   git clone https://github.com/yourusername/your-repo-name.git   `

### Install dependencies
`   pip install -r requirements.txt   `

### Start the Flask server
`   python app.py   `

### Open your browser
`   http://127.0.0.1:5000   `

Current Status
--------------

*   Fully working local web app
    
*   GloVe + SBERT toggle implemented
    
*   End-to-end full-stack flow
    
*   Hints system coming soon
    
*   Deployment planned (making it global weeeeeh)
    

Why I Built This?!
----------------

*   To understand semantic similarity beyond theory
    
*   To use embeddings in a real, interactive product
    
*   To build a end-to-end full-stack NLP project, not just a jupyter notebook
    
*   To learn Flask and frontend development by doing and debugging real issues
    

Feedback & Ideas
----------------

*   Open an issue!!!
    
*   Or DM me on linkedin: www.linkedin.com/in/shreya-raghav
>>  — I’m genuinely open to feedback
