from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_cohere import ChatCohere
from langchain_cohere import ChatCohere

#Global variable to store the chat model instance
chat_model = None

def initialize_chat_model(cohere_api_key):
    """Return a singleton instance of the ChatCohere model."""
    global chat_model
    if chat_model is None:
        chat_model = ChatCohere(
            cohere_api_key=cohere_api_key,
            model='command-light',
            max_tokens=50
        )
        print("ChatCohere model initialized.")
    else:
        print("ChatCohere model already initialized.")

def get_retriever(vector_store):
    print("Setting up the RAG retriever...")

    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={'k':1, 'lambda_mult':0.7})

    print("RAG retriever SUCCESS...!!")
    return retriever

def invoke_chain(retriever,asking_question):

    global chat_model
    print("\nEntering Pipeline\n")

    TEMPLATE ='''
    Answer the following question:
    {question}

    To answer the question, use only the following context:
    {context}

    '''
        
    prompt_template = PromptTemplate.from_template(template = TEMPLATE)

    question = asking_question

    chain = ({'context':retriever,
         'question':RunnablePassthrough()} 
         | prompt_template  
         |chat_model
         |StrOutputParser())
    
    
    print("\nChatbot Response:")
    
    #for chunk in chain.stream(question):
    #   print(chunk, end="")
    
    return chain.invoke(question)