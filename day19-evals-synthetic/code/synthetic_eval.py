import openai
import random

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Generate synthetic Q&A pairs
topics = ["Python", "GenAI", "Vector DB", "Prompt Engineering"]
qa_pairs = [(f"What is {topic}?", f"{topic} is a key concept in modern AI.") for topic in topics]

def get_llm_answer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        max_tokens=50
    )
    return response.choices[0].message['content']

# Evaluate LLM answers
correct = 0
for q, expected in qa_pairs:
    answer = get_llm_answer(q)
    print(f"Q: {q}\nExpected: {expected}\nLLM: {answer}\n")
    if topic.lower() in answer.lower():
        correct += 1

accuracy = correct / len(qa_pairs)
print(f"Accuracy on synthetic data: {accuracy:.2f}")
