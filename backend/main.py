import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

from loaders import initial_load_and_split
from vectorstore import create_vector_store

import uvicorn

def main():
    # Dynamically resolve the base directory
    base_dir = Path(__file__).resolve().parent.parent

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    cohere_api_key = os.getenv("API_KEY")

    REBUILD_VECTORSTORE = os.getenv("VECTORSTORE_EXISTS") == "false"

    if REBUILD_VECTORSTORE:
        print("vectorstore does not exist, creating vectorstore")
        
        # Use base directory to construct the path
        docx_file = base_dir / "dataset" / "contents.docx"
        print(f"Resolved file path: {docx_file}")

        if not docx_file.exists():
            raise FileNotFoundError(f"File not found at {docx_file}")
        
        documents = initial_load_and_split(str(docx_file))
        create_vector_store(documents, cohere_api_key)

    else:
        print("vectorstore exists, loading vectorstore")
    
    uvicorn.run("app:app", host="127.0.0.1", port=8006, reload=True)

if __name__ == "__main__":
    main()
