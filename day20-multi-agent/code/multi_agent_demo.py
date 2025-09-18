import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def retrieval_agent(query):
    # Simulate retrieval (in real life, use a vector DB or search API)
    if "LangChain" in query:
        return "LangChain is a framework for building GenAI workflows."
    return "No relevant info found."

def reasoning_agent(context, question):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Orchestration
question = "What is LangChain and how is it used?"
context = retrieval_agent(question)
answer = reasoning_agent(context, question)
print("Final Answer:", answer)
