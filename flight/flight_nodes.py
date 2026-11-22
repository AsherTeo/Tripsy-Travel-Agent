from states import TravelState
from langgraph.types import interrupt
import model_llm
from flight.model import FlightParams
import serpapi
import os 
from function import *
import json 

def flight_parser(state:TravelState):

    llm_flight_params = model_llm.load_llm().with_structured_output(FlightParams)
    response = llm_flight_params.invoke(state['messages'])

    return {'flight_params': response.model_dump()}

def flight_api(state:TravelState):
    api_key = os.getenv("SERP_API_KEY")
    client = serpapi.Client(api_key=api_key)
    params = state['flight_params']

    try:
        results = client.search(params)
        best = get_best_flight(results)
    except Exception as e:
        best = None
    with open('output.json', 'w') as file:
        json.dump(best, file, indent=4)
  
    return {'flight_results': best or None}

def flight_options(state:TravelState):
    if not state.get('flight_results'):
        return {'messages': [{'role': 'assistant', 'content': "No flights found, try different dates."}]}

    """
    Summary the flight and append into a list 
    """
    options = summary_flight(state['flight_results'])
    options_list = []

    for i, o in enumerate(options, 1):
        text = f" {i}) ${o['price']} | {o['airline']} | {o['departure_airport']} | {o['departure_time']} → {o['arrival_airport']} {o['arrival_time']}"  
        options_list.append(text)

    """
    Append the options into the prompt for interrupt
    """
    n = len(options)
    texts = ("Please choose one flight:\n" + "\n".join(options_list))
    prompt = texts + '\n' + f'Please enter a flight number from 1 to {n}'
    valid = [str(i) for i in range(1, n + 1)]

    answer = interrupt(prompt)

    while str(answer).strip() not in valid:
        answer = interrupt(f'Invalid. Please enter a flight number from 1 to {n}')

    choice = int(answer)
  
    return {
        'messages': [{'role': 'assistant', 'content': f'You picked flight {choice} and the flight parameter are {options[choice - 1]}'}],
        'flight_outbound_picked': state['flight_results']['Total_Flight'][choice - 1]
    }

