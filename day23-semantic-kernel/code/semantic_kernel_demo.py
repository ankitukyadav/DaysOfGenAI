from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# Initialize kernel and add OpenAI connector
kernel = Kernel()
kernel.add_chat_service(
    "openai-gpt",
    OpenAIChatCompletion(
        "gpt-3.5-turbo",
        api_key="YOUR_OPENAI_API_KEY"  # Replace with your key
    )
)

# Define a simple prompt skill
async def main():
    prompt = "Summarize the benefits of composable GenAI workflows."
    result = await kernel.chat_service.complete(prompt)
    print("Semantic Kernel Output:", result)

# To run: use an async event loop, e.g. with asyncio.run(main())
