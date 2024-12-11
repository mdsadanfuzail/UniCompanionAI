import os
from dotenv import find_dotenv, load_dotenv

from fastapi import FastAPI
from pipeline import invoke_chain, get_retriever, initialize_chat_model 
from vectorstore import get_vectorstore  

app = FastAPI()

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
cohere_api_key = os.getenv("API_KEY")

vector_store = get_vectorstore(cohere_api_key)  # Retrieve the vector store, initialized in main.py
retriever = get_retriever(vector_store)
initialize_chat_model(cohere_api_key)


@app.get("/")
def read_root():
    return {"message": "UniCompanionAI!"}

@app.get("/get_answer/")
def get_answer(question: str):
    """
    Endpoint to get an answer to a Query
    """
    # Invoke the pipeline to get an answer
    response = invoke_chain(retriever, question)
    return {"answer": response}
