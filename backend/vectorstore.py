from langchain_cohere.embeddings import CohereEmbeddings
from langchain_chroma import Chroma

def create_vector_store(documents, cohere_api_key):
    cohere_embeddings = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key=cohere_api_key)

    vectorstore = Chroma.from_documents(documents = documents,
                     embedding = cohere_embeddings,
                     persist_directory = "./chroma_UniCompanionAI_Vectorstore")
    

def get_vectorstore(api_key):
    cohere_embeddings = CohereEmbeddings(model = "embed-english-light-v3.0",
                                     cohere_api_key = api_key)

    vectorstore = Chroma(persist_directory = "./chroma_UniCompanionAI_Vectorstore",
                     embedding_function = cohere_embeddings)
    
    print("vectorstore load Success...!!")
    
    return vectorstore