import openai
import numpy as np

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Local knowledge base
docs = [
    "Python is great for AI development.",
    "LangChain helps build GenAI workflows.",
    "FAISS is a vector store for similarity search."
]
embeddings = np.random.rand(len(docs), 128).astype('float32')

def retrieve(query):
    # Dummy embedding for demo
    query_emb = np.random.rand(1, 128).astype('float32')
    scores = np.dot(embeddings, query_emb.T).flatten()
    idx = np.argmax(scores)
    return docs[idx]

def agent(query):
    if "search" in query.lower():
        result = retrieve(query)
        return f"Retrieved info: {result}"
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            max_tokens=100
        )
        return response.choices[0].message['content']

# Test agent
print(agent("Search for GenAI workflows."))
print(agent("What is Python used for?"))
