# 🎧 Universal Recommendation Engine (URE)

This is a personalized content recommendation system inspired by Spotify, YouTube, and Netflix's Universal Recommendation Engine (URE) architecture.

This app generates semantic embeddings with BERT, and performs fast similarity search using FAISS.

---

## ✨ Features


- **Semantic Embeddings**: Uses `sentence-transformers` (MiniLM) to represent titles + genres meaningfully
- ⚡ **Vector Search**: Uses FAISS to find top-5 similar items instantly
- **MovieLens Dataset**: Works on real metadata from 100K movie dataset
- **Streamlit UI**: Dual-mode interface — manual search or Spotify-based recommendation


---

## Getting Started

### Install Dependencies

```bash
pip install -r requirements.txt
