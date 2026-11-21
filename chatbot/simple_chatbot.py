import model_llm
from dotenv import load_dotenv
from states import TravelState


load_dotenv()

def chatbot(state: TravelState):
    messages = state['messages']
    response = model_llm.load_llm().invoke(messages)
    return {'messages': [response]}