from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

def load_llm():
    llm = init_chat_model(model= 'openai:gpt-4o')
    return llm 

llm = load_llm()