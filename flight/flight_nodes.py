from states import TravelState
from langgraph.types import interrupt
import model_llm
from flight.model import FlightParams
import serpapi
import os 
from function import *
import json 

api_key = os.getenv("SERP_API_KEY")
client = serpapi.Client(api_key=api_key)

def flight_parser(state:TravelState):

    llm_flight_params = model_llm.load_llm().with_structured_output(FlightParams)
    response = llm_flight_params.invoke(state['messages'])

    return {'flight_params': response.model_dump()}

def outbound_flight_api(state:TravelState):
    
    params = state['flight_params']

    try:
        results = client.search(params)
        best = get_best_flight(results)
    except Exception as e:
        best = None
    with open('output.json', 'w') as file:
        json.dump(best, file, indent=4)
  
    return {'flight_outbound_results': best or None}

def select_onbound_flight_options(state:TravelState):
    if not state.get('flight_outbound_results'):
        return {'messages': [{'role': 'assistant', 'content': "No flights found, try different dates."}]}

    """
    Summary the flight and append into a list 
    """
    options = summary_flight(state['flight_outbound_results'])
    options_list = []

    for i, o in enumerate(options, 1):
        text = f" {i}) ${o['price']} | {o['airline']} | {o['departure_airport']} | {o['departure_time']} → {o['arrival_airport']} {o['arrival_time']}"  
        options_list.append(text)

    """
    Append the options into the prompt for interrupt
    """
    n = len(options)
    date = state['flight_params']['outbound_date']
    texts = f"Flights on {date}, please select one:\n" + "\n".join(options_list)
    prompt = texts + '\n' + f'Please enter a flight number from 1 to {n}'
    valid = [str(i) for i in range(1, n + 1)]

    answer = interrupt(prompt)

    while str(answer).strip() not in valid:
        answer = interrupt(f'Invalid. Please enter a flight number from 1 to {n}')

    choice = int(answer)
  
    return {
        'messages': [{'role': 'assistant', 'content': f'Outbound flight confirmed: {options_list[choice - 1]}'}],
        'flight_outbound_picked': state['flight_outbound_results']['Total_Flight'][choice - 1],
        'flight_outbound_params': options_list[choice - 1]
    }
    

############################################################## Return ############################################################

def got_return(state:TravelState):
    params = state['flight_params']

    trip_type = params['type'] if isinstance(params, dict) else params.type 

    if trip_type == 1:
        return 'yes'
    return 'no'

"""
If round trip is yes: 
"""

def return_flight_api(state:TravelState):
    
    """
    Add departure_token into the flight parameter
    """

    outbound_infor = state['flight_outbound_picked']
    departure_token = outbound_infor['departure_token'] if isinstance(outbound_infor, dict) else outbound_infor.departure_token

    params = state['flight_params']
    params['departure_token'] = departure_token

    try:
        results = client.search(params)
        best = get_best_flight(results)
    except Exception as e:
        best = None
    with open('return.json', 'w') as file:
        json.dump(best, file, indent=4)
    
    return {'flight_return_results': best or None}


def select_return_flight_options(state:TravelState):
    if not state.get('flight_return_results'):
            return {'messages': [{'role': 'assistant', 'content': "No flights found, try different dates."}]}
    
    """
    Summary the flight and append into a list 
    """
    options = summary_flight(state['flight_return_results'])
    options_list = []

    for i, o in enumerate(options, 1):
        text = f" {i}) ${o['price']} | {o['airline']} | {o['departure_airport']} | {o['departure_time']} → {o['arrival_airport']} {o['arrival_time']}"  
        options_list.append(text)

    """
    Append the options into the prompt for interrupt
    """
    n = len(options)
    date = state['flight_params']['return_date']
    texts = f"Flights on {date}, please select one:\n" + "\n".join(options_list)
    prompt = texts + '\n' + f'Please enter a flight number from 1 to {n}'
    valid = [str(i) for i in range(1, n + 1)]

    answer = interrupt(prompt)

    while str(answer).strip() not in valid:
        answer = interrupt(f'Invalid. Please enter a flight number from 1 to {n}')

    choice = int(answer)
    
    return {
        'messages': [{'role': 'assistant', 'content': f'Return flight confirmed: {options_list[choice - 1]}'}],
        'flight_return_picked': state['flight_return_results']['Total_Flight'][choice - 1],
        'flight_return_params': options_list[choice - 1]
    }
    

def summary_chosen_flight(state:TravelState):

    outbound_flight = state['flight_outbound_picked']['flights']
    return_flight = state['flight_return_picked']['flights']
    return_value = state['flight_return_params']

    price = int(return_value.split("|")[0].split("$")[1])

    text = (
        "✈️ Your trip summary\n\n"
        f"Outbound\n   {fmt_leg(outbound_flight)}\n\n"
        f"Return\n   {fmt_leg(return_flight)}\n\n"
        f"Total (round trip): ${price}"
    )
    return {'messages': [{'role': 'assistant', 'content': text}]}