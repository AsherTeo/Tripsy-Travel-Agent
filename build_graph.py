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
builder.add_node('retry_outbound_node', retry_outbound_node)
builder.add_node('update_outbound_node', update_outbound_node)

builder.add_node('return_flight_api', return_flight_api)
builder.add_node('select_return_flight_options', select_return_flight_options)
builder.add_node('summary_chosen_flight', summary_chosen_flight)
builder.add_node('flight_end', flight_end)

builder.add_node('itineary_parser', itineary_parser)

##################################################### Connect Nodes #######################################################

builder.add_conditional_edges(START, router_node, {'chatbot': 'chatbot_node', 'flight_search': 'flight_parser', 'itineary_search': 'itineary_parser'})
builder.add_edge('chatbot_node', END)

builder.add_edge('flight_parser', 'outbound_flight_api')
builder.add_conditional_edges('outbound_flight_api', got_flight, {'got result':'select_onbound_flight_options', 'no result': 'retry_outbound_node'})
builder.add_conditional_edges('retry_outbound_node', yes_node, {'yes': 'update_outbound_node', 'no': 'flight_end'})
builder.add_edge('update_outbound_node', 'outbound_flight_api')


builder.add_conditional_edges('select_onbound_flight_options', got_return, {'yes': 'return_flight_api', 'no': 'summary_chosen_flight'})
builder.add_edge('return_flight_api', 'select_return_flight_options')
builder.add_edge('select_return_flight_options', 'summary_chosen_flight')
builder.add_edge('summary_chosen_flight', 'flight_end')
builder.add_edge('flight_end', END)

graph = builder.compile(checkpointer=InMemorySaver())