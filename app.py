from langchain_cohere.embeddings import CohereEmbeddings
from langchain_chroma import Chroma
from langchain_cohere import ChatCohere

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferWindowMemory
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
DATA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\data"
CHROMA_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\chromadb"
FAISS_PATH = r"C:\Users\91638\Desktop\UniCompanionAI\faiss_index"


embeddings_model = CohereEmbeddings(model="embed-english-light-v3.0", cohere_api_key=cohere_api_key)

llm = ChatCohere(
        cohere_api_key=cohere_api_key,
        model='command-light',
        max_tokens=100
    )

vector_store = Chroma(
    collection_name="UniCompanionAI",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH
)

num_retrievals = 3
retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k':num_retrievals, 'lambda_mult':0.7})
memory = ConversationBufferWindowMemory(memory_key="chat_history", k=3, return_messages=True)


def query_bot(message, _):

    template = """
        You are a helpful and professional university assistant chatbot for a university called Anna University.

        Answer the question below using only the provided context. 
        When relevant, organize your answer using appropriate structure such as:

        - Bullet points for lists or multiple steps.
        - Tables for comparisons or structured data.
        - Well-formatted paragraphs for descriptive explanations.

        Make sure your answer is clear, concise, and informative.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
        
    chain = RetrievalQA.from_chain_type(
        llm, retriever=vector_store.as_retriever(), memory=memory, chain_type_kwargs={"prompt": prompt}
    )

    partial_message = ""

    for res in chain.stream(message):
        partial_message += res['result']
        yield partial_message

Chatbot = gr.ChatInterface(query_bot, 
                           textbox=gr.Textbox(placeholder="Ask query here...", 
                                              container=False,
                                              autoscroll=True,
                                              scale=7
                                              ),
                           )

if __name__ == "__main__":
    Chatbot.launch()
