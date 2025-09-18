import openai
from functools import lru_cache

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

@lru_cache(maxsize=32)
def get_llm_output(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message['content']

# Example usage
if __name__ == "__main__":
    prompt = "Explain the benefits of caching in GenAI apps."
    print(get_llm_output(prompt))
    # Repeated call (should be cached)
    print(get_llm_output(prompt))
