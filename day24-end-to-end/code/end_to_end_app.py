import openai
import faiss
import numpy as np

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Sample knowledge base
docs = [
    "LangChain is a framework for GenAI workflows.",
    "LlamaIndex connects LLMs to your data.",
    "FAISS is a vector store for similarity search."
]
embeddings = np.random.rand(len(docs), 128).astype('float32')
index = faiss.IndexFlatL2(128)
index.add(embeddings)

def retrieve(query):
    # Dummy embedding for demo
    query_emb = np.random.rand(1, 128).astype('float32')
    _, I = index.search(query_emb, 1)
    return docs[I[0][0]]

def answer_query(query):
    context = retrieve(query)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Example usage
question = "What is LangChain?"
print("Final Answer:", answer_query(question))
