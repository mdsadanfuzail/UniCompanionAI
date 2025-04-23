from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import TextLoader
from langchain_chroma import Chroma
from uuid import uuid4
import os
from dotenv import find_dotenv, load_dotenv
from llama_parse import LlamaParse


import nest_asyncio
nest_asyncio.apply()

dotenv = find_dotenv()
load_dotenv(dotenv)
llamaparse_api_key = os.getenv("LLAMA_CLOUD_API_KEY")
cohere_api_key = os.getenv("COHERE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Congfig
DATA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\data"
CHROMA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\chromadb"

#embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")
embeddings_model = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key=cohere_api_key)

def ParseData():
    parsingInstruction = """The provided document is a rules and regulations pdf of a University named Anna University.        
        It also contains tables.
        Try to be precise while answering the questions"""
    
    parser = LlamaParse(api_key=llamaparse_api_key, result_type="markdown", parsing_instruction=parsingInstruction)
    llama_parse_documents = parser.load_data(r"C:\Users\91638\Desktop\UniCompanionAI\data\UG R 2021.pdf")
    parsed_data = llama_parse_documents

    return parsed_data

def makeVectorStore():

    vector_store = Chroma(
        collection_name="UniCompanionAI",
        embedding_function=embeddings_model,
        persist_directory=CHROMA_PATH
    )

    #llama_parse_documents = ParseData()
    #print(llama_parse_documents[1].text[:100])
    
    #with open(r'C:\Users\91638\Desktop\UniCompanionAI\data\output.md', 'a', encoding='utf-8', errors='ignore') as f:  # Open the file in append mode ('a')
    #    for doc in llama_parse_documents:
    #        f.write(doc.text + '\n')

    #loader = DirectoryLoader(r'C:\Users\91638\Desktop\UniCompanionAI\data', glob="**/*.md")
    #loader = UnstructuredMarkdownLoader(r"C:\Users\91638\Desktop\UniCompanionAI\data\output.md", encoding="latin-1")
    loader = TextLoader(r"C:/Users/91638/Desktop/UniCompanionAI/data/output.md", encoding="utf-8")


    raw = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = text_splitter.split_documents(raw)

    uuids = [str(uuid4()) for _ in range(len(chunks))]

    vector_store.add_documents(documents=chunks, ids=uuids)

    print("VectorStore created successfully")

makeVectorStore()