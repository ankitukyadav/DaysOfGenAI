import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

def get_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content']

# Pattern 1: Role Assignment
prompt_role = "You are a senior Python developer. Write a function to reverse a string."

# Pattern 2: Step-by-Step
prompt_step = "Write a Python function to reverse a string. First, explain your approach step by step, then provide the code."

# Pattern 3: Few-Shot Example
prompt_fewshot = (
    "Here are examples of reversing strings in Python:\n"
    "Input: 'hello' Output: 'olleh'\n"
    "Input: 'world' Output: 'dlrow'\n"
    "Now, write a function to reverse any string."
)

for name, prompt in [("Role Assignment", prompt_role), ("Step-by-Step", prompt_step), ("Few-Shot", prompt_fewshot)]:
    print(f"\n{name} Pattern:\n{get_completion(prompt)}")
