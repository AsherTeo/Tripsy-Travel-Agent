from model_llm import llm
from dotenv import load_dotenv
from states import TravelState

load_dotenv()

def chatbot(state: TravelState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {'messages': [response]}