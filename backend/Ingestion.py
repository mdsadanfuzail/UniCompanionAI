from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
import os
from dotenv import find_dotenv, load_dotenv

dotenv = find_dotenv()
load_dotenv(dotenv)
cohere_api_key = os.getenv("COHERE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Congfig
DATA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\data"
CHROMA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\chromadb"

#embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")
embeddings_model = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key=cohere_api_key)


vector_store = Chroma(
    collection_name="UniCompanionAI",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH
)

loader = PyPDFDirectoryLoader(DATA_PATH)

raw = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False,
)

chunks = text_splitter.split_documents(raw)

uuids = [str(uuid4()) for _ in range(len(chunks))]

vector_store.add_documents(documents=chunks, ids=uuids)