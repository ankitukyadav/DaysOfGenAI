# Day 2: LLMs Under the Hood—Tokenization & Embeddings

## Overview
Day 2 dives deeper into how LLMs process text: tokenization and embeddings. We compare how two similar sentences are tokenized and how their embeddings differ.

## What You'll Learn
- How LLMs tokenize sentences
- How embeddings represent meaning
- Measuring similarity between sentences using cosine similarity

## Demo
The Python script `compare_embeddings.py` demonstrates:
- Tokenizing two sentences
- Extracting and averaging token embeddings
- Comparing sentence similarity using cosine similarity

## How to Run
1. Install dependencies:
   ```bash
   pip install transformers torch numpy
   ```
2. Run the script:
   ```bash
   python code/compare_embeddings.py
   ```

## Diagram
A hand-drawn style diagram visualizes:
- Two sentences → Tokenizer → Tokens → Embeddings → Similarity Score

## Reflection
Tiny changes in wording can shift meaning for an LLM. Cosine similarity helps us measure this shift.

## Call to Action
Try the code with your own sentences and share your results! #GenAIwithAY
