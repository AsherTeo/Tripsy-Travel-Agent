from states import TravelState
from langgraph.types import interrupt
from langchain.messages import SystemMessage, HumanMessage
from model_llm import load_llm
from flight.model import FlightParams
import serpapi
import os 
from function import *
import json 

llm = load_llm()
api_key = os.getenv("SERP_API_KEY")
client = serpapi.Client(api_key=api_key)

def flight_parser(state:TravelState):
    
    llm_flight_params = llm.with_structured_output(FlightParams)
    response = llm_flight_params.invoke(state['messages'])
    print("This the paras", response.model_dump())
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

def got_flight(state:TravelState):
    result = state['flight_outbound_results']
    if not result:
        return 'no result'
    return 'got result'

def retry_outbound_node(state:TravelState):
    params = state['flight_params']
    outbound_date = params['outbound_date'] 
    return_date = params['return_date'] if params['return_date'] else ""
    dates = outbound_date + f"'to {return_date}'"
    msg = f"Sorry, there are no flights from {params['departure_id']} to {params['arrival_id']} on {dates}"

    valid = ['y', 'n']
    answer = interrupt(f'{msg}. \nDo you want to retry? (y/n)')
    while answer not in valid:
        answer = interrupt(f"Invalid. Do you want to retry? (y/n)")

    return {'try_again': answer.strip()}

def yes_node(state:TravelState):
    options = state['try_again']
    if options == 'y':
        return 'yes'
    if options == 'n':
        return 'no'

def update_outbound_node(state:TravelState):

    answer = interrupt('Please type in your new request')
    user_params = state['flight_params']

    prompt = (
        f"This is user previous search information {user_params}"
        f"This is user new reqirement {answer}"
        "Keep everything the same except the user requirements"
        "Example: if the user type 2026, then just change the year keep the rest untouched"
        "Example: if the user type a whole new requirement, change everything accordingly"
    )

    llm_flight_params = llm.with_structured_output(FlightParams)
    
    new_params = llm_flight_params.invoke(prompt)

    return {
        "messages": [HumanMessage(content=answer)],
        'flight_params': new_params.model_dump(),
        "flight_outbound_results": None,
        "flight_outbound_picked": None,
        "flight_outbound_params": None,
        
    }

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

    if state['flight_params']['type'] == 2:
        outbound_value = state['flight_outbound_params']
        price = int(outbound_value.split("|")[0].split("$")[1])
        text = (
                "========== ✈️ Your trip summary ========== \n\n"
                f"Outbound\n   {fmt_leg(outbound_flight)}\n\n"
                f"Total (round trip): ${price}")
        
        return {'messages': [{'role': 'assistant', 'content': text}]}
    
    else:
        return_flight = state['flight_return_picked']['flights']
        return_value = state['flight_return_params']

        price = int(return_value.split("|")[0].split("$")[1])

        text = (
            "========== ✈️ Your trip summary ========== \n\n"
            f"Outbound\n   {fmt_leg(outbound_flight)}\n\n"
            f"Return\n   {fmt_leg(return_flight)}\n\n"
            f"Total (round trip): ${price}"
        )
    return {'messages': [{'role': 'assistant', 'content': text}]}


def flight_end(state:TravelState):

    prompt = "Thanks for using Tripsy! Hope you have an amazing trip. See you next time! ✈️"

    return{
        "messages": [{'role': 'assistant', 'content': prompt}],
        'flight_params': None,
        "flight_outbound_results": None,
        "flight_outbound_picked": None,
        "flight_outbound_params": None,
    }