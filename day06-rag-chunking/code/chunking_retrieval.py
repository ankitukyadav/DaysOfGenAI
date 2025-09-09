import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample document
doc = """Generative AI is transforming industries. 
It enables new forms of creativity and automation. 
RAG pipelines combine LLMs with external knowledge for smarter answers. 
Chunking and vector databases are key for scalable retrieval."""

# Chunking
chunks = [chunk.strip() for chunk in doc.split('\n') if chunk.strip()]

# Create embeddings using TF-IDF (for demo; use real LLM embeddings in production)
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(chunks).toarray().astype('float32')

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

def retrieve(query, k=2):
    query_emb = vectorizer.transform([query]).toarray().astype('float32')
    _, I = index.search(query_emb, k)
    return [chunks[i] for i in I[0]]

# Evaluate retrieval
query = "How does RAG use external knowledge?"
results = retrieve(query)
print("Top retrieved chunks:")
for r in results:
    print("-", r)

# Simple evaluation: check if relevant chunk is retrieved
relevant = any("RAG pipelines" in r for r in results)
print("Relevant chunk retrieved?", "Yes" if relevant else "No")
