from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Sample docs
docs = [
    "LangChain is a framework for GenAI workflows.",
    "RAG combines retrieval and generation for smarter answers.",
    "FAISS is a vector store for similarity search."
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
question = "What is LangChain?"
answer = qa.run(question)
print("Answer:", answer)
