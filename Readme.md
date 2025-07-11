# 🎧 Universal Recommendation Engine (URE)

This is a personalized content recommendation system inspired by Spotify, YouTube, and Netflix's Universal Recommendation Engine (URE) architecture.

Built as a project for Banza's AI Internship program, this app simulates and integrates real-world user preferences using Spotify OAuth, generates semantic embeddings with BERT, and performs fast similarity search using FAISS.

---

## ✨ Features

- 🔐 **Spotify Integration**: OAuth-based login to fetch user's top tracks and listening habits
- 🧠 **Semantic Embeddings**: Uses `sentence-transformers` (MiniLM) to represent titles + genres meaningfully
- ⚡ **Vector Search**: Uses FAISS to find top-5 similar items instantly
- 📊 **MovieLens Dataset**: Works on real metadata from 100K movie dataset
- 🌐 **Streamlit UI**: Dual-mode interface — manual search or Spotify-based recommendation
- 🛡️ **Secure Secrets**: Follows `.env` + Streamlit Secrets best practices

---

## Getting Started

### Install Dependencies

```bash
pip install -r requirements.txt
