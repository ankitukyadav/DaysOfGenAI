from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sentences = [
    "Generative AI is changing the world.",
    "GenAI is changing the world."
]

for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.squeeze(0)
    avg_embedding = torch.mean(embeddings, dim=0)
    print(f"Sentence: {sentence}")
    print(f"Tokens: {tokenizer.tokenize(sentence)}")
    print(f"Avg Embedding (first 5 dims): {avg_embedding[:5].numpy()}\n")

# Cosine similarity between sentence embeddings
embeddings_list = []
for sentence in sentences:
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.squeeze(0)
    avg_embedding = torch.mean(embeddings, dim=0)
    embeddings_list.append(avg_embedding)

cos_sim = torch.nn.functional.cosine_similarity(embeddings_list[0], embeddings_list[1], dim=0)
print(f"Cosine similarity between sentences: {cos_sim.item():.4f}")
