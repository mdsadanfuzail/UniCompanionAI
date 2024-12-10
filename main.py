import os
from dotenv import find_dotenv, load_dotenv
from langchain_cohere import ChatCohere
from loaders import initial_load_and_split
from vectorstore import get_vectorstore, create_vector_store
from pipeline import create_rag_pipeline, invoke_chain, initialize_chat_model

def main():

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    cohere_api_key = os.getenv("API_KEY")

    REBUILD_VECTORSTORE = os.getenv("VECTORSTORE_EXISTS").lower() == "false"

    if REBUILD_VECTORSTORE == True:
        print("vectorstore does not exist, creating vectorestore")
        docx_file = r"C:\Users\91638\Desktop\StudyBuddyAU\contents.docx"  # List of DOCX files
        documents = initial_load_and_split(docx_file)
        create_vector_store(documents, cohere_api_key)  #initial vectorstore created now only need to access it

    else:
        print("vectorstore exists, loading vectorestore")

    vector_store = get_vectorstore(cohere_api_key)

    retriever = create_rag_pipeline(vector_store, cohere_api_key)

    initialize_chat_model(cohere_api_key)

    #query
    question = "what are the textbooks in engineering chemistry ?"
    invoke_chain(retriever, question)

if __name__ == "__main__":
    main()