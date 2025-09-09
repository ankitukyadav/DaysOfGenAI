import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def safe_completion(prompt, forbidden_words=None):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    output = response.choices[0].message['content']
    # Post-process: block forbidden words
    if forbidden_words:
        for word in forbidden_words:
            if word.lower() in output.lower():
                return "[Blocked: Unsafe content detected]"
    return output

# Guardrail 1: Explicit instruction
prompt_explicit = "You are a medical assistant. Only answer if you are certain. What is the recommended dosage of aspirin for adults?"

# Guardrail 2: Output format constraint
prompt_format = "Respond in JSON format: {'dosage': 'value', 'unit': 'mg'} What is the recommended dosage of aspirin for adults?"

# Guardrail 3: Content filter
forbidden = ["overdose", "child"]

for name, prompt in [("Explicit Instruction", prompt_explicit), ("Format Constraint", prompt_format)]:
    print(f"\n{name} Guardrail:\n{safe_completion(prompt, forbidden_words=forbidden)}")
