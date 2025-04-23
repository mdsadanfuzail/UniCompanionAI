from langchain_cohere.embeddings import CohereEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere
from langchain_community.llms import HuggingFaceHub

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationalRetrievalChain, RetrievalQA

import gradio as gr
import os
from dotenv import find_dotenv, load_dotenv

dotenv = find_dotenv()
load_dotenv(dotenv)
cohere_api_key = os.getenv("COHERE_API_KEY")
HF_token = os.getenv("HUGGING_FACE_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Congfig
DATA_PATH = r"C:\Users\91638\Desktop\PP\LangChain\RAG Chatbot\data"
CHROMA_PATH = r"C:\Users\91638\Desktop\PP\LangChain\RAG Chatbot\chromadb"

#embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large", api_key=openai_api_key)
embeddings_model = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key=cohere_api_key)

llm = ChatCohere(
        cohere_api_key=cohere_api_key,
        model='command-light',
        max_tokens=100
    )

'''llm = HuggingFaceHub(
    repo_id="deepseek-ai/deepseek-llm-7b-chat",
    model_kwargs={"temperature": 0.7},
    huggingfacehub_api_token = HF_token 
)'''

vector_store = Chroma(
    collection_name="UniCompanionAI",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH
)

num_retrievals = 5
retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k':num_retrievals, 'lambda_mult':0.7})

def response(message, _):

    TEMPLATE ='''
    You are a helpful university assistant chatbot. Answer the following question based only on the provided context.

    Context:
    {context}

    Question: {question}
    '''
        
    '''prompt_template = PromptTemplate.from_template(template = TEMPLATE)

    chain = ({'context':retriever,
         'question':RunnablePassthrough()} 
         | prompt_template  
         |llm
         |StrOutputParser())
    '''
    #return chain.invoke(message)

    # Define prompt template
    template = """
        You are a helpful university assistant chatbot. Answer the following question based only on the provided context.

        Context: {context}
        Question: {question}
        Answer:
        """

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        
    chain = RetrievalQA.from_chain_type(
        llm, retriever=vector_store.as_retriever(), chain_type_kwargs={"prompt": prompt}
    )

    #output = chain.invoke(message)
    #output = chain.stream(message)
    #print(output)

    #return output['result']

    partial_message = ""

    for res in chain.stream(message):
        partial_message += res['result']
        yield partial_message
    
# initiate the Gradio app
chatbot = gr.ChatInterface(response, 
                           textbox=gr.Textbox(placeholder="Ask query here...", 
                                              container=False,
                                              autoscroll=True,
                                              scale=7
                                              ),
                           )

chatbot.launch()