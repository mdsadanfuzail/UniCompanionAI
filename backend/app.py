import os
from dotenv import find_dotenv, load_dotenv

from fastapi import FastAPI
from pipeline import invoke_chain, create_rag_pipeline, initialize_chat_model  # Import invoke_chain
from vectorstore import get_vectorstore  # Import function to get vectorstore

# Initialize FastAPI app
app = FastAPI()

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
cohere_api_key = os.getenv("API_KEY")

# Initialize vector store
vector_store = get_vectorstore(cohere_api_key)  # Retrieve the vector store, initialized in main.py
retriever = create_rag_pipeline(vector_store, cohere_api_key)
initialize_chat_model(cohere_api_key)


@app.get("/")
def read_root():
    return {"message": "Welcome to UniCompanionAI API!"}

@app.get("/get_answer/")
def get_answer(question: str):
    """
    Endpoint to get an answer to a specific question
    """
    # Invoke the pipeline to get an answer
    response = invoke_chain(retriever, question)
    return {"answer": response}
