import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   
sys.path.append(str(ROOT))

from langsmith import Client, evaluate, traceable
from uuid import uuid4
from build_graph import graph
from langgraph.types import Command
from eval.generate_dataset import gnr_dateset, get_answer
from eval.metrics import eval_parser, eval_result
from flight.flight_nodes import flight_parser

project_name = 'Tripsy'
dataset_name = 'Testingset'

client = Client()

"""
Create project 
"""

if not client.has_project(project_name= project_name):
    client.create_project(project_name=project_name)

"""
Create dataset
"""

if not client.has_dataset(dataset_name=dataset_name):
    dataset = client.create_dataset(dataset_name=dataset_name)
else:
    dataset = client.read_dataset(dataset_name=dataset_name)

"""
Create Examples
"""
import json 

if not list(client.list_examples(dataset_id=dataset.id)):
    path = gnr_dateset(name_dataset= dataset_name, number_of_dataset = 10)
    with open(path, encoding='utf-8') as file:
        testing = json.load(file)

    for test in testing:
        client.create_example(
            dataset_id=dataset.id,
            inputs=test['inputs'],
            outputs=test['outputs'],
        )

"""
Create pipelines

"""
@traceable
def run_parser(inputs:dict):
    state = {'messages': inputs['query']}
    response = flight_parser(state)
    return {
        'flight_params' : response['flight_params']
    }

@traceable
def run_graph(inputs: dict):

    config = {'configurable': {'thread_id': str(uuid4())}}

    query = inputs['query']
    try:
        response = graph.invoke({'messages': [{'role': 'user', 'content': query}]}, config, interrupt_after=['select_onbound_flight_options'])
        for _ in range(5):
            if '__interrupt__' in response:
                prompt = response['__interrupt__'][0].value
                answer = get_answer(prompt)
                response = graph.invoke(Command(resume = answer), config, interrupt_after=['select_onbound_flight_options'],)
    except Exception as e:
        print('graph error', repr(e))

    state = graph.get_state(config).values
    params = state.get('flight_params')
    if params is not None and not isinstance(params, dict):
        params = params.model_dump()

    return {
        'flight_params': params,
        'flight_outbound_picked': state.get('flight_outbound_picked')
    }

if __name__ == '__main__': 

    """
    Run parser first if no error then run the graph
    """
    # evaluate(
    #     run_parser,
    #     data = dataset_name,
    #     evaluators= [eval_parser],
    #     experiment_prefix= 'parser'
    # ) 

    evaluate(
        run_graph,
        data=dataset_name,
        evaluators=[eval_result],
        experiment_prefix= 'result'
    )
