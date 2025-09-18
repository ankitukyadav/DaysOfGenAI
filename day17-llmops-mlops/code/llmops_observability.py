import openai
import logging

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Set up logging
logging.basicConfig(filename='llm_requests.log', level=logging.INFO)

def get_llm_output(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    output = response.choices[0].message['content']
    # Log request and response
    logging.info(f"Prompt: {prompt}\nOutput: {output}\n")
    return output

# Example usage
if __name__ == "__main__":
    prompt = "Summarize the benefits of CI/CD for AI apps."
    print(get_llm_output(prompt))

# Simple test for CI/CD
def test_llm_output():
    result = get_llm_output("What is LLMOps?")
    assert "LLM" in result or "Ops" in result

# To run: pytest llmops_observability.py
