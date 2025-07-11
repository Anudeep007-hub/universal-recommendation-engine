import streamlit as st
import pandas as pd
import numpy as np
import faiss
import os
from sentence_transformers import SentenceTransformer

# Load data and embeddings
CSV_PATH = os.path.join("data","movies_cleaned.csv")
EMBEDDINGS_PATH = os.path.join("data", "embeddings.npz")
df = pd.read_csv(CSV_PATH)
embeddings = np.load(EMBEDDINGS_PATH)['vectors']
model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

# Build FAISS index
faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
faiss_index.add(embeddings)

# Recommendation logic
def recommend(query):
    query_vec = model.encode([query]).astype('float32')
    _, I = faiss_index.search(query_vec, 5)
    return df.iloc[I[0]]

# ----- UI -----
st.title("Universal Recommendation Engine")
st.markdown("Choose a mode: manual keyword search or fetch preferences from Spotify.")

# ---------------- Manual Search ----------------
st.subheader("Search Genre")
manual_input = st.text_input("Enter genres, moods, or keywords (e.g., action thriller AI)")

if st.button("Search Manually"):
    if manual_input.strip():
        results = recommend(manual_input)
        st.success(f"Top Matches for: `{manual_input}`")
        for _, row in results.iterrows():
            genres = ', '.join(df.columns[4:][row[df.columns[4:]] == 1])
            st.markdown(f"**{row['title']}** — Genres: _{genres}_")
    else:
        st.warning("Please enter some keywords to search.")

