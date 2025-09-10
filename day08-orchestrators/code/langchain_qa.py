from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Sample documents
docs = [
    "LangChain is a framework for developing applications powered by LLMs.",
    "LlamaIndex helps you connect LLMs to external data sources.",
    "FAISS is used for efficient similarity search."
]

# Create embeddings and vector store
embeddings = OpenAIEmbeddings(openai_api_key="YOUR_OPENAI_API_KEY")
vectorstore = FAISS.from_texts(docs, embedding=embeddings)

# Build QA chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key="YOUR_OPENAI_API_KEY"),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Ask a question
question = "What is LangChain used for?"
answer = qa.run(question)
print("Answer:", answer)
