import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def try_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Example: Custom prompt pattern
custom_prompt = (
    "You are a helpful AI assistant. "
    "First, summarize the following topic in 2 sentences. "
    "Then, list 3 practical applications. "
    "Topic: Generative AI"
)

print("Custom Pattern Output:\n", try_prompt(custom_prompt))
