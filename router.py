from pydantic import BaseModel, Field
from typing import Literal
from states import TravelState
import model_llm 

class Router(BaseModel):
    options: Literal['chatbot', 'flight_search', 'itinerary_search'] = Field(
        description= "flight_search': the user wants to find or book flights, or is giving flight details (destination, dates, trip type, number of adults, time of the trips)."
                    "itineary search: user wants things to do, a day-by-day plan." 
                    "chatbot': everything else, e.g. greetings, thanks, general questions, asking for hotel information."
    )


def router_node(state:TravelState):
    router_llm = model_llm.load_llm().with_structured_output(Router)
    response = router_llm.invoke(state['messages'])
    print('This is the options: ', response)
    return [response.options]

