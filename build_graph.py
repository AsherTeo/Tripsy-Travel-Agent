from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import InMemorySaver 
from chatbot.simple_chatbot import *
from states import TravelState
from router import router_node
from flight.flight_nodes import *
from itinerary.itinerary_nodes import itineary_parser

builder = StateGraph(TravelState)
builder.add_node('chatbot_node', chatbot)
builder.add_node('flight_parser', flight_parser)
builder.add_node('flight_api', flight_api)
builder.add_node('flight_options', flight_options)
#builder.add_node('select_options_node',select_options_node)


builder.add_node('itineary_parser', itineary_parser)

builder.add_conditional_edges(START, router_node, {'chatbot': 'chatbot_node', 
                                                   'flight_search': 'flight_parser', 
                                                   'itineary_search': 'itineary_parser'
                                                })

builder.add_edge('flight_parser', 'flight_api')
builder.add_edge('flight_api', 'flight_options')
#builder.add_edge('flight_options', 'select_options_node')
graph = builder.compile(checkpointer=InMemorySaver())