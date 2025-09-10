# Open-source: HuggingFace Transformers (Llama)
from transformers import pipeline

llama_pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf")
output_llama = llama_pipe("Explain GenAI in one sentence.", max_new_tokens=50)
print("Llama Output:", output_llama[0]['generated_text'])

# Hosted: OpenAI GPT-3.5
import openai
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Explain GenAI in one sentence."}],
    max_tokens=50
)
print("OpenAI Output:", response.choices[0].message['content'])
