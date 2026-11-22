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
builder.add_node('outbound_flight_api', outbound_flight_api)
builder.add_node('select_onbound_flight_options', select_onbound_flight_options)
builder.add_node('return_flight_api', return_flight_api)
builder.add_node('select_return_flight_options', select_return_flight_options)
builder.add_node('summary_chosen_flight', summary_chosen_flight)


builder.add_node('itineary_parser', itineary_parser)





builder.add_conditional_edges(START, router_node, {'chatbot': 'chatbot_node', 
                                                   'flight_search': 'flight_parser', 
                                                   'itineary_search': 'itineary_parser'
                                                })

"""
router_node == flight_search 
"""

builder.add_edge('flight_parser', 'outbound_flight_api')
builder.add_edge('outbound_flight_api', 'select_onbound_flight_options')
builder.add_conditional_edges('select_onbound_flight_options', got_return, {'yes': 'return_flight_api', 'no': END})

"""
got_return == yes 
"""
builder.add_edge('return_flight_api', 'select_return_flight_options')
builder.add_edge('select_return_flight_options', 'summary_chosen_flight')

graph = builder.compile(checkpointer=InMemorySaver())