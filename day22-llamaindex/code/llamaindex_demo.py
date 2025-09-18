from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext
from langchain.llms import OpenAI

# Load documents from a directory (for demo, use in-memory docs)
docs = [
    "LlamaIndex connects LLMs to your data.",
    "You can build search and RAG pipelines easily.",
    "Chunking and indexing are handled automatically."
]

# Create an index
llm_predictor = LLMPredictor(llm=OpenAI(openai_api_key="YOUR_OPENAI_API_KEY"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
index = GPTVectorStoreIndex.from_documents(docs, service_context=service_context)

# Query the index
query = "How does LlamaIndex help with RAG?"
response = index.query(query)
print("Answer:", response)
