import os
from dotenv import find_dotenv, load_dotenv

from loaders import initial_load_and_split
from vectorstore import create_vector_store


import uvicorn

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
    
    uvicorn.run("app:app", host="127.0.0.1", port=8006, reload=True)

if __name__ == "__main__":
    main()