import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   
sys.path.append(str(ROOT))

from unittest.mock import MagicMock, patch
from langchain.messages import AIMessage
from uuid import uuid4 
from build_graph import graph 
from states import FlightParams
from flight.flight_nodes import *
from tests.config import *

def test_chatbot():
    fake_llm = MagicMock()
    fake_llm.invoke.return_value = AIMessage(content= "You should eat chicken rice")

    with patch("chatbot.simple_chatbot.llm", fake_llm):
        config = {'configurable': {"thread_id": {uuid4()}}}
        response = graph.invoke({'messages': [{"role": "user", "content": "What should i eat ?"}]}, config)

        assert response['messages'][-1].content == "You should eat chicken rice"


def test_flight_parser():

    fake_llm = MagicMock()
    fake_llm.with_structured_output.return_value.invoke.return_value = roundtrips_params

    state = {'messages': 'Plan to visit singapore to guagzhou from 04 feb to 06 feb 2027'}
    
    with patch('flight.flight_nodes.llm', fake_llm):
        response = flight_parser(state)

    assert response['flight_params'] == roundtrips_params.model_dump()

def test_outbound_flight_api():

    fake_client = MagicMock()
    fake_client.search.return_value = roundtrips_results

    state = {'flight_params': roundtrips_params}
    
    with patch('flight.flight_nodes.client', fake_client):
        response = outbound_flight_api(state)

    assert response['flight_outbound_results'] is not None
    assert response['flight_outbound_results'] == get_best_flight(roundtrips_results)

def test_got_flight():
    state = {'flight_outbound_results': roundtrips_results}
    assert got_flight(state) == 'got result'

def test_retry_outbound_node(): 

    fake_interrupt = MagicMock(return_value = 'y')

    state = {'flight_params': roundtrips_params.model_dump()}

    with patch('flight.flight_nodes.interrupt', fake_interrupt):
        response = retry_outbound_node(state)

    assert response['try_again'] == 'y'