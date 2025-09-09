from transformers import AutoTokenizer, AutoModel
import torch
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

sentence = "Generative AI is transforming how we build software."
tokens = tokenizer.tokenize(sentence)
inputs = tokenizer(sentence, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
embeddings = outputs.last_hidden_state.squeeze(0)

# Reduce dimensions for visualization
pca = PCA(n_components=2)
embeddings_2d = pca.fit_transform(embeddings.numpy())

# Plot tokens in 2D space
plt.figure(figsize=(8, 5))
for i, token in enumerate(tokens):
    plt.scatter(embeddings_2d[i, 0], embeddings_2d[i, 1])
    plt.text(embeddings_2d[i, 0]+0.01, embeddings_2d[i, 1]+0.01, token)
plt.title("Token Embeddings Visualization")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.grid(True)
plt.show()
