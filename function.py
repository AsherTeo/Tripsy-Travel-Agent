
def get_best_flight(results, n = 5):

    best_fligts = results.get('best_flights', [])
    other_flights = results.get('other_flights', [])

    all_flights = best_fligts + other_flights

    if not all_flights:
        return {"error": "No flights found", "search_parameters": results.get('search_parameters')}
    
    cheapest = sorted(all_flights, key=lambda x: x.get("price", float("inf")))[:n]

    #lowest_flight = min(all_flights, key = lambda x:x.get('price', float('inf')))
  
    return {"Total_Flight": cheapest}

def summary_flight(results):
    summary = []

    for i, result in enumerate(results['Total_Flight']):
        price = result['price']
        flights = result['flights']

        departure_airport = flights[0]['departure_airport']['id']
        departure_time = flights[0]['departure_airport']['time']
        arrival_airport = flights[0]['arrival_airport']['id']
        arrival_time = flights[0]['arrival_airport']['time']

        flight_number = flights[0]['flight_number']
        airline = flights[0]['airline']

        summary.append({
                        "price": price, 
                        "airline": airline, 
                        'flight_number':flight_number,
                        "departure_airport": departure_airport,
                        "departure_time": departure_time,
                        "arrival_airport": arrival_airport,
                        "arrival_time": arrival_time
                    })
    return summary

