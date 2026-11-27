from pydantic import BaseModel, Field
from typing import Literal, Optional

class FlightParams(BaseModel):
    engine: Literal['google_flights'] = 'google_flights'
    hl: Literal['en'] = 'en'  
    gl: Literal['sg'] = 'sg' 
    departure_id: str = Field(default='SIN', description="Return the IATA airport code of the country. " \
                                                         "If the user doesn't mention where they're flying from, use 'SIN'.")
    arrival_id: str = Field(description='Return the IATA airport code of the country')
    currency: Literal['SGD'] = 'SGD'
    type: Literal[1, 2] = Field(default=1,description=(
                                            "Determine the flight type: "
                                            "1 = Round trip, 2 = One way. "
                                            "Follow these rules strictly: "
                                            "1. If the user provides both an outbound date and a return date, "
                                            "classify as 1 (round trip), even if they do not explicitly mention "
                                            "'return' or 'round trip'. "
                                            "2. If the user provides only one travel date without mentioning "
                                            "a return date, classify as 2 (one way). "
                                            "3. If the user explicitly says 'one way', 'single trip', or "
                                            "mentions booking the return later, classify as 2 (one way). "
                                            "4. If the user explicitly requests a round trip, classify as "
                                            "1 (round trip)."
                                        ))
    outbound_date: str = Field(description="Departure date in YYYY-MM-DD format, e.g. 2026-12-01")
    return_date: Optional[str] = Field(default=None, description="Return date in YYYY-MM-DD format")
    travel_class: Literal[1, 2, 3, 4] = Field(default=1, description="1 = economy, 2 = premium economy, 3 = business, 4 = first. Use 1 if the user doesn't say.")
    stops : Literal[1] = 1
    
    deep_search : bool =  True
    no_cache: bool = True
     
    exclude_airlines : Optional[str] = None 
    include_airlines : Optional[str] = None
        
    #multi_city_json: Dict = Field(default_factory=dict)
    
    adults : int 
    # children : Optional[int] 
    # infants_in_seat: int = 0
    # infants_on_lap : int = 0
    
    
    
    outbound_times:Optional[str] = None
    return_times: Optional[str] = None
    
    # max_price : Optional[int] = None 
    # outbound_times : Optional[str] = None 
    # return_times : Optional[str] = None 
    # max_duration : Optional[int] = None 

class AirlineNames(BaseModel):
    names: str = Field(description="Full airline names for the given 2-letter IATA codes, in the same order, e.g. ['Singapore Airlines', 'Garuda Indonesia']")