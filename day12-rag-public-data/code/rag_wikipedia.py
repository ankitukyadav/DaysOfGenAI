import openai
import wikipedia

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def retrieve_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except Exception as e:
        return "No relevant Wikipedia article found."

def generate_answer(query):
    context = retrieve_wikipedia(query)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Test RAG pipeline
question = "What is LangChain?"
print("RAG Answer:", generate_answer(question))
