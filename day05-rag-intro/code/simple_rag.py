import openai
import faiss
import numpy as np

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Sample knowledge base
docs = [
    "Python is a popular programming language for AI.",
    "FAISS is a library for efficient similarity search.",
    "OpenAI provides powerful LLM APIs."
]
# Create embeddings (dummy: random for demo, use real embeddings in production)
embeddings = np.random.rand(len(docs), 128).astype('float32')
index = faiss.IndexFlatL2(128)
index.add(embeddings)

def retrieve(query, k=1):
    # Dummy query embedding (random for demo)
    query_emb = np.random.rand(1, 128).astype('float32')
    _, I = index.search(query_emb, k)
    return [docs[i] for i in I[0]]

def generate_answer(query):
    retrieved = retrieve(query)
    prompt = f"Context: {retrieved[0]}\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

question = "What is FAISS used for?"
print("RAG Answer:", generate_answer(question))
