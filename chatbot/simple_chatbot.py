from model_llm import load_llm
from dotenv import load_dotenv
from states import TravelState


load_dotenv()
llm = load_llm()

def chatbot(state: TravelState):
    messages = state['messages']
    response = llm.invoke(messages)
    
    return {'messages': [response]}