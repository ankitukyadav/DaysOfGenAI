import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def summarize(text):
    prompt = f"Summarize this in one sentence:\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response.choices[0].message['content']

def ask_question(summary, question):
    prompt = f"Based on this summary: '{summary}', answer: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response.choices[0].message['content']

# Example workflow
text = "LangChain is a framework that helps developers build applications powered by large language models."
summary = summarize(text)
answer = ask_question(summary, "What is LangChain used for?")
print("Summary:", summary)
print("Q&A Answer:", answer)
