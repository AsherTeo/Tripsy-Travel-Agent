from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import InMemorySaver 
from chatbot.simple_chatbot import *
from states import TravelState

builder = StateGraph(TravelState)
builder.add_node('chatbot_node', chatbot)


builder.add_edge(START, 'chatbot_node')
builder.add_edge('chatbot_node', END)

graph = builder.compile(checkpointer=InMemorySaver())