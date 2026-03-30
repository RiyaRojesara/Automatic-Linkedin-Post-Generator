from langchain_groq import ChatGroq

# Global LLM instance (will be None until initialized)
llm = None

def get_llm(api_key):
    return ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.3-70b-versatile"
    )

def initialize_llm(api_key):
    """Initialize the global llm variable"""
    global llm
    llm = get_llm(api_key)
    return llm

#from dotenv import load_dotenv
#from langchain_groq import ChatGroq
#import os
#
#load_dotenv()
#
#llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama-3.3-70b-versatile")

#from langchain_groq import ChatGroq
#
#def get_llm(api_key):
#    return ChatGroq(
#        groq_api_key=api_key,
#        model_name="llama-3.3-70b-versatile"
#    )
