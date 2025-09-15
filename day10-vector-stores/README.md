# Day 11: Vector Stores—FAISS, Milvus, Pinecone, pgvector Explained

## Overview
Day 11 explores vector stores—databases for storing and searching embeddings. FAISS, Milvus, Pinecone, and pgvector are featured.

## What You'll Learn
- Why vector stores matter for GenAI and RAG
- How to store and search embeddings locally and in the cloud
- Key differences between FAISS, Milvus, Pinecone, and pgvector

## Demo
The Python script `vector_store_demo.py` demonstrates:
- Storing and searching embeddings with FAISS (local)
- Storing and searching embeddings with Pinecone (cloud)

## How to Run
1. Install dependencies:
   ```bash
   pip install faiss-cpu pinecone-client numpy
2. Add your Pinecone API key to the script.
3. Run the script:
python code/vector_store_demo.py
