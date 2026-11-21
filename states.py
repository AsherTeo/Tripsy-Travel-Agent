from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from flight.model import FlightParams

class TravelState(MessagesState):
    flight_params: FlightParams | None
    flight_results: dict
    flight_options: List | None