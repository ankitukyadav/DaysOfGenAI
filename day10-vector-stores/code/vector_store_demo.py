# FAISS (local)
import faiss
import numpy as np

# Create random embeddings for demo
embeddings = np.random.rand(5, 128).astype('float32')
index = faiss.IndexFlatL2(128)
index.add(embeddings)

# Query
query = np.random.rand(1, 128).astype('float32')
_, I = index.search(query, k=2)
print("FAISS Top 2 indices:", I[0])

# Pinecone (cloud)
import pinecone

pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
index_name = "genai-demo"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=128)
index = pinecone.Index(index_name)

# Upsert vectors
vectors = [(str(i), embeddings[i]) for i in range(5)]
index.upsert(vectors)

# Query Pinecone
query_vector = query[0]
result = index.query(vector=query_vector, top_k=2)
print("Pinecone Top 2 IDs:", [match['id'] for match in result['matches']])
