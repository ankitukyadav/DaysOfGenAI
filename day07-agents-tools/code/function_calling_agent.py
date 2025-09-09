import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key

# Define some functions the agent can call
def get_weather(city):
    return f"The weather in {city} is sunny and 25°C."

def get_time(city):
    return f"The current time in {city} is 10:00 AM."

# Simulate agent reasoning
def agent(query):
    if "weather" in query.lower():
        city = query.split("in")[-1].strip().replace("?", "")
        return get_weather(city)
    elif "time" in query.lower():
        city = query.split("in")[-1].strip().replace("?", "")
        return get_time(city)
    else:
        # Fallback to LLM
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            max_tokens=100
        )
        return response.choices[0].message['content']

# Test agent
print(agent("What's the weather in Paris?"))
print(agent("What's the time in Tokyo?"))
print(agent("Tell me about GenAI agents."))
