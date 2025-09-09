# Day 6: RAG Deep Dive—Chunking, Vector DBs & Retrieval Evals

## Overview
Day 6 explores chunking, storing chunks in vector databases, and evaluating retrieval quality in RAG pipelines.

## What You'll Learn
- Why chunking improves retrieval
- How to store and search chunks in FAISS
- How to evaluate retrieval quality

## Demo
The Python script `chunking_retrieval.py` demonstrates:
- Chunking a document
- Creating embeddings and storing in FAISS
- Retrieving top matches and evaluating relevance

## How to Run
1. Install dependencies:
   ```bash
   pip install faiss-cpu numpy scikit-learn
2. Run the script:
python code/chunking_retrieval.py
