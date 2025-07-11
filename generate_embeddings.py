import pandas as pd
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Load data
DATA_PATH = os.path.join("data", "movies_cleaned.csv")
df = pd.read_csv(DATA_PATH)

# Generate genres column by combining all active genres
genre_cols = df.columns[4:]  # Assuming genre columns start from 5th column
df['genres'] = df[genre_cols].apply(lambda row: ' '.join(genre_cols[row == 1]), axis=1)

# Create a text field for embedding: title + genres
df['text'] = df['title'] + " " + df['genres']

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate sentence embeddings
embeddings = model.encode(df['text'].tolist(), convert_to_numpy=True)

# Save embeddings to a compressed .npz file
np.savez_compressed("data/embeddings.npz", vectors=embeddings)
