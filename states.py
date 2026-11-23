from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from flight.model import FlightParams

class TravelState(MessagesState):
    flight_params: FlightParams | None

    flight_outbound_results: dict
    flight_outbound_picked:List| None
    flight_outbound_params: dict| None 

    flight_return_results: dict
    flight_return_picked:List| None
    flight_return_params: dict| None 

    try_again : str