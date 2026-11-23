from states import FlightParams

onewaytrips_params = FlightParams(
        departure_id="SIN",
        arrival_id="HND",
        outbound_date="2027-02-04",
        return_date= None,
        type=1,
        adults= 2,
    )

onewaytrips_results = {
    "Total_Flight": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-01-02 17:35"
                    },
                    "arrival_airport": {
                        "name": "Haneda Airport",
                        "id": "HND",
                        "time": "2027-01-03 01:00"
                    },
                    "duration": 385,
                    "airplane": "Boeing 787",
                    "airline": "Scoot",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
                    "travel_class": "Economy",
                    "flight_number": "TR 804",
                    "legroom": "31 in",
                    "extensions": [
                        "Average legroom (31 in)",
                        "Wi-Fi for a fee",
                        "In-seat power outlet",
                        "Carbon emissions estimate: 279 kg"
                    ]
                }
            ],
            "total_duration": 385,
            "carbon_emissions": {
                "this_flight": 279000,
                "typical_for_this_route": 417000,
                "difference_percent": -33
            },
            "price": 451,
            "type": "One way",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
            "booking_token": "WyJDalJJVlV4c1RIbDJaemhHWVUxQlVFNXlNR2RDUnkwdExTMHRMUzB0TFhscFltUjNOMEZCUVVGQlIzTkZSazFCUlZsT1UyVkJFZ1ZVVWpnd05Cb0xDS3pnQWhBQ0dnTlRSMFE0SEhDZGtRST0iLFtbIlNJTiIsIjIwMjctMDEtMDIiLCJITkQiLG51bGwsIlRSIiwiODA0Il1dXQ=="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-01-02 14:05"
                    },
                    "arrival_airport": {
                        "name": "Haneda Airport",
                        "id": "HND",
                        "time": "2027-01-02 21:40"
                    },
                    "duration": 395,
                    "airplane": "Airbus A350",
                    "airline": "Singapore Airlines",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
                    "travel_class": "Economy",
                    "flight_number": "SQ 634",
                    "ticket_also_sold_by": [
                        "ANA"
                    ],
                    "legroom": "32 in",
                    "extensions": [
                        "Above average legroom (32 in)",
                        "Free Wi-Fi",
                        "In-seat power & USB outlets",
                        "On-demand video",
                        "Carbon emissions estimate: 319 kg"
                    ]
                }
            ],
            "total_duration": 395,
            "carbon_emissions": {
                "this_flight": 320000,
                "typical_for_this_route": 417000,
                "difference_percent": -23
            },
            "price": 1158,
            "type": "One way",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
            "booking_token": "WyJDalJJVlV4c1RIbDJaemhHWVUxQlVFNXlNR2RDUnkwdExTMHRMUzB0TFhscFltUjNOMEZCUVVGQlIzTkZSazFCUlZsT1UyVkJFZ1ZUVVRZek5Cb0xDTmlJQnhBQ0dnTlRSMFE0SEhERnZRVT0iLFtbIlNJTiIsIjIwMjctMDEtMDIiLCJITkQiLG51bGwsIlNRIiwiNjM0Il1dXQ=="
        },
    ]}


roundtrips_params = FlightParams(
        departure_id="SIN",
        arrival_id="CAN",
        outbound_date="2027-02-04",
        return_date="2027-02-09",
        type=1,
        adults= 1,
    )


roundtrips_results = {
    "Total_Flight": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-04 06:30"
                    },
                    "arrival_airport": {
                        "name": "Shanghai Pudong International Airport",
                        "id": "PVG",
                        "time": "2027-02-04 11:45"
                    },
                    "duration": 315,
                    "airplane": "Airbus A320",
                    "airline": "Spring",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/9C.png",
                    "travel_class": "Economy",
                    "flight_number": "9C 8552",
                    "extensions": [
                        "Carbon emissions estimate: 270 kg"
                    ]
                }
            ],
            "total_duration": 315,
            "carbon_emissions": {
                "this_flight": 270000,
                "typical_for_this_route": 304000,
                "difference_percent": -11
            },
            "price": 552,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/9C.png",
            "departure_token": "WyJDalJJVVY5M2NIUmhkM05pT0dkQlRtdElUa0ZDUnkwdExTMHRMV05uWkhwMk1pMXVNa0ZCUVVGQlIzTkVkMWhOU2xaRVJEQkJFZ1k1UXpnMU5USWFDd2lGcndNUUFob0RVMGRFT0J4d2djNEMiLFtbIlNJTiIsIjIwMjctMDItMDQiLCJQVkciLG51bGwsIjlDIiwiODU1MiJdXV0="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-04 17:40"
                    },
                    "arrival_airport": {
                        "name": "Shanghai Pudong International Airport",
                        "id": "PVG",
                        "time": "2027-02-04 22:55"
                    },
                    "duration": 315,
                    "airplane": "Airbus A320",
                    "airline": "Spring",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/9C.png",
                    "travel_class": "Economy",
                    "flight_number": "9C 7678",
                    "extensions": [
                        "Carbon emissions estimate: 270 kg"
                    ],
                    "often_delayed_by_over_30_min": True
                }
            ],
            "total_duration": 315,
            "carbon_emissions": {
                "this_flight": 270000,
                "typical_for_this_route": 304000,
                "difference_percent": -11
            },
            "price": 571,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/9C.png",
            "departure_token": "WyJDalJJVVY5M2NIUmhkM05pT0dkQlRtdElUa0ZDUnkwdExTMHRMV05uWkhwMk1pMXVNa0ZCUVVGQlIzTkVkMWhOU2xaRVJEQkJFZ1k1UXpjMk56Z2FDd2o3dlFNUUFob0RVMGRFT0J4d3lka0MiLFtbIlNJTiIsIjIwMjctMDItMDQiLCJQVkciLG51bGwsIjlDIiwiNzY3OCJdXV0="
        },
]}