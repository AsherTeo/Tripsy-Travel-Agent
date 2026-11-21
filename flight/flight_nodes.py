from states import TravelState
import model_llm
from flight.model import FlightParams
import serpapi
import os 
from function import *
import json 

def flight_parser(state:TravelState):

    llm_flight_params = model_llm.load_llm().with_structured_output(FlightParams)
    response = llm_flight_params.invoke(state['messages'])

    return {'flight_params': response}

def flight_api(state:TravelState):
    api_key = os.getenv("SERP_API_KEY")
    client = serpapi.Client(api_key=api_key)
    params = state['flight_params'].model_dump(exclude_none=True)

    try:
        results = client.search(params)
        best = get_best_flight(results)
    except Exception as e:
        best = None
    with open('output.json', 'w') as file:
        json.dump(best, file, indent=4)
  
    return {'flight_results': best or None}

def flight_result(state:TravelState):
    options = summary_flight(state['flight_results'])

    text_lines = []

    for i, o in enumerate(options, 1):
        text = f" {i}) ${o['price']} | {o['airline']} | {o['departure_airport']} | {o['departure_time']} → {o['arrival_airport']} {o['arrival_time']}"  
        text_lines.append(text)

    choose = ("Please choose one flight:\n" + "\n".join(text_lines))
    return {'messages': [{'role': 'assistant', 'content': choose}], 'flight_options': options}