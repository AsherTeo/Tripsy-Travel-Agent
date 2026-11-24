import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   
sys.path.append(str(ROOT))

from unittest.mock import MagicMock, patch
from langchain.messages import AIMessage
from uuid import uuid4 
from build_graph import graph 
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
    fake_client.search.return_value = roundtrips_result

    state = {'flight_params': roundtrips_params}
    
    with patch('flight.flight_nodes.client', fake_client):
        response = outbound_flight_api(state)

    assert response['flight_outbound_results'] is not None
    assert response['flight_outbound_results'] == roundtrips_best

def test_got_flight():
    state = {'flight_outbound_results': roundtrips_best}
    assert got_flight(state) == 'got result'

def test_retry_outbound_node(): 

    fake_interrupt = MagicMock(return_value = 'y')

    state = {'flight_params': roundtrips_params.model_dump()}

    with patch('flight.flight_nodes.interrupt', fake_interrupt):
        response = retry_outbound_node(state)

    assert response['try_again'] == 'y'

def test_yes_node():

    state = {'try_again': 'y'}
    assert yes_node(state) == 'yes'

def test_update_outbound_node():

    old_params = roundtrips_params
    new_params = roundtrips_params

    fake_interrupt = MagicMock(return_value = 'change to month to March')
    fake_llm = MagicMock()
    fake_llm.with_structured_output.return_value.invoke.return_value = new_params

    state = {'flight_params': old_params}

    with patch('flight.flight_nodes.interrupt', fake_interrupt), patch('flight.flight_nodes.llm', fake_llm):
        response = update_outbound_node(state)

    assert response['messages'][0].content == 'change to month to March'
    assert response['flight_params'] == new_params.model_dump()
    assert response['flight_outbound_results'] == None

def test_select_onbound_flight_options():

    fake_interrupt = MagicMock(return_value = '1')

    state = {'flight_outbound_results': roundtrips_best,
             'flight_params': roundtrips_params.model_dump()}

    with patch('flight.flight_nodes.interrupt', fake_interrupt):
        response = select_onbound_flight_options(state)

    assert response['flight_outbound_picked'] == roundtrips_best['Total_Flight'][0]
    assert 'Outbound flight confirmed' in response['messages'][-1]['content'] 


def test_return_flight_api():

    fake_client = MagicMock()

    fake_client.search.return_value = roundtrips_result

    state = {'flight_outbound_picked': round_trips_picked, 
             'flight_params': roundtrips_params.model_dump()}

    with patch('flight.flight_nodes.client', fake_client):
        response = return_flight_api(state)
     
    assert response['flight_return_results'] == roundtrips_best
    
def test_select_return_flight_options():

    fake_interrupt = MagicMock(return_value = '1')

    state = {'flight_return_results': roundtrips_best,
             'flight_params': roundtrips_params.model_dump()}

    with patch('flight.flight_nodes.interrupt', fake_interrupt):
        response = select_return_flight_options(state)

    assert response['flight_return_picked'] == roundtrips_best['Total_Flight'][0]
    assert 'Return flight confirmed:' in response['messages'][-1]['content'] 

def test_summary_chosen_flight():

    state = {'flight_outbound_picked': roundtrips_best['Total_Flight'][0],
             'flight_params': roundtrips_params.model_dump(),
             'flight_return_picked': roundtrips_best['Total_Flight'][0],
             'flight_return_params': '1) $890 | ...'}
    
    response = summary_chosen_flight(state)

    texts = ["========== ✈️ Your trip summary ========== \n\n", "Outbound" , "Return", "Total (round trip): $"]
    content = response['messages'][-1]['content']
    
    assert (text in content for text in texts)