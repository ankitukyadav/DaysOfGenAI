# Day 5: Retrieval Augmented Generation (RAG)—Bringing Knowledge to LLMs

## Overview
Day 5 introduces RAG, a technique that combines LLMs with external knowledge sources for smarter, more factual answers.

## What You'll Learn
- What RAG is and why it matters
- How to build a simple RAG pipeline in Python
- Using FAISS for retrieval and OpenAI for generation

## Demo
The Python script `simple_rag.py` demonstrates:
- Creating a knowledge base
- Retrieving relevant context using FAISS
- Augmenting LLM responses with retrieved context

## How to Run
1. Install dependencies:
   ```bash
   pip install openai faiss-cpu numpy
2. Add your OpenAI API key to the script.
3. Run the script:
python code/simple_rag.py
