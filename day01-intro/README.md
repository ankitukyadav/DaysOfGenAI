# Day 1: GenAI—Beyond the Basics

## Overview
We explore what sets Generative AI apart from traditional AI, focusing on how LLMs process language using tokenization and embeddings.

## What You'll Learn
- Difference between GenAI and traditional AI
- How LLMs break down sentences into tokens
- Visualizing token embeddings in 2D space

## Demo
The Python script `tokenization_embedding.py` demonstrates:
- Tokenizing a sentence using HuggingFace Transformers
- Extracting embeddings for each token
- Visualizing embeddings using PCA and matplotlib

## How to Run
1. Install dependencies:
   ```bash
   pip install transformers torch matplotlib scikit-learn
   ```
2. Run the script:
   ```bash
   python code/tokenization_embedding.py
   ```

## Diagram
A hand-drawn style diagram visualizes the flow:
- Sentence → Tokenizer → Tokens → Embeddings → 2D Plot

## Reflection
Visualizing embeddings makes the inner workings of LLMs tangible. Try it with your own sentences!

## Call to Action
Try the code, visualize your own sentence, and share your plot! #GenAIwithAY
