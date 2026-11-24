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

roundtrips_params1 = FlightParams(
        departure_id="SIN",
        arrival_id="CAN",
        outbound_date="2027-03-04",
        return_date="2027-03-09",
        type=1,
        adults= 1,
    )

round_trips_picked= {
            "departure_token": "WyJDalJJVVY5M2NIUmhkM05pT0dkQlRtdElUa0ZDUnkwdExTMHRMV05uWkhwMk1pMXVNa0ZCUVVGQlIzTkVkMWhOU2xaRVJEQkJFZ1k1UXpnMU5USWFDd2lGcndNUUFob0RVMGRFT0J4d2djNEMiLFtbIlNJTiIsIjIwMjctMDItMDQiLCJQVkciLG51bGwsIjlDIiwiODU1MiJdXV0="
        }


roundtrips_result = {
    
    "other_flights": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 10:45"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 15:00"
                    },
                    "duration": 255,
                    "airplane": "Boeing 787",
                    "airline": "Scoot",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
                    "travel_class": "Economy",
                    "flight_number": "TR 101",
                    "legroom": "31 in",
                    "extensions": [
                        "Average legroom (31 in)",
                        "Wi-Fi for a fee",
                        "In-seat power outlet",
                        "Carbon emissions estimate: 160 kg"
                    ],
                }
            ],
            "total_duration": 255,
            "carbon_emissions": {
                "this_flight": 160000,
                "typical_for_this_route": 252000,
                "difference_percent": -37
            },
            "price": 672,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZVVWpFd01Sb0xDTEtNQkJBQ0dnTlRSMFE0SEhDTWxnTT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlRSIiwiMTAxIl1dXQ=="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 02:15"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 06:35"
                    },
                    "duration": 260,
                    "airplane": "Boeing 787",
                    "airline": "Singapore Airlines",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
                    "travel_class": "Economy",
                    "flight_number": "SQ 853",
                    "legroom": "32 in",
                    "extensions": [
                        "Above average legroom (32 in)",
                        "Free Wi-Fi",
                        "In-seat power & USB outlets",
                        "On-demand video",
                        "Carbon emissions estimate: 147 kg"
                    ],
                }
            ],
            "total_duration": 260,
            "carbon_emissions": {
                "this_flight": 147000,
                "typical_for_this_route": 252000,
                "difference_percent": -42
            },
            "price": 879,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZUVVRnMU14b0xDS0N1QlJBQ0dnTlRSMFE0SEhDNGt3UT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlNRIiwiODUzIl1dXQ=="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 13:30"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 17:50"
                    },
                    "duration": 260,
                    "airplane": "Boeing 787",
                    "airline": "Singapore Airlines",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
                    "travel_class": "Economy",
                    "flight_number": "SQ 851",
                    "legroom": "32 in",
                    "extensions": [
                        "Above average legroom (32 in)",
                        "Free Wi-Fi",
                        "In-seat power & USB outlets",
                        "On-demand video",
                        "Carbon emissions estimate: 147 kg"
                    ]
                }
            ],
            "total_duration": 260,
            "carbon_emissions": {
                "this_flight": 147000,
                "typical_for_this_route": 252000,
                "difference_percent": -42
            },
            "price": 1081,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZUVVRnMU1Sb0xDSWpNQmhBQ0dnTlRSMFE0SEhEVGpRVT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlNRIiwiODUxIl1dXQ=="
        }
    ],
}

roundtrips_best = {
    "Total_Flight": [
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 10:45"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 15:00"
                    },
                    "duration": 255,
                    "airplane": "Boeing 787",
                    "airline": "Scoot",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
                    "travel_class": "Economy",
                    "flight_number": "TR 101",
                    "legroom": "31 in",
                    "extensions": [
                        "Average legroom (31 in)",
                        "Wi-Fi for a fee",
                        "In-seat power outlet",
                        "Carbon emissions estimate: 160 kg"
                    ],
                }
            ],
            "total_duration": 255,
            "carbon_emissions": {
                "this_flight": 160000,
                "typical_for_this_route": 252000,
                "difference_percent": -37
            },
            "price": 672,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TR.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZVVWpFd01Sb0xDTEtNQkJBQ0dnTlRSMFE0SEhDTWxnTT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlRSIiwiMTAxIl1dXQ=="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 02:15"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 06:35"
                    },
                    "duration": 260,
                    "airplane": "Boeing 787",
                    "airline": "Singapore Airlines",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
                    "travel_class": "Economy",
                    "flight_number": "SQ 853",
                    "legroom": "32 in",
                    "extensions": [
                        "Above average legroom (32 in)",
                        "Free Wi-Fi",
                        "In-seat power & USB outlets",
                        "On-demand video",
                        "Carbon emissions estimate: 147 kg"
                    ],
                    
                }
            ],
            "total_duration": 260,
            "carbon_emissions": {
                "this_flight": 147000,
                "typical_for_this_route": 252000,
                "difference_percent": -42
            },
            "price": 879,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZUVVRnMU14b0xDS0N1QlJBQ0dnTlRSMFE0SEhDNGt3UT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlNRIiwiODUzIl1dXQ=="
        },
        {
            "flights": [
                {
                    "departure_airport": {
                        "name": "Guangzhou Baiyun International Airport",
                        "id": "CAN",
                        "time": "2027-02-09 13:30"
                    },
                    "arrival_airport": {
                        "name": "Singapore Changi Airport",
                        "id": "SIN",
                        "time": "2027-02-09 17:50"
                    },
                    "duration": 260,
                    "airplane": "Boeing 787",
                    "airline": "Singapore Airlines",
                    "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
                    "travel_class": "Economy",
                    "flight_number": "SQ 851",
                    "legroom": "32 in",
                    "extensions": [
                        "Above average legroom (32 in)",
                        "Free Wi-Fi",
                        "In-seat power & USB outlets",
                        "On-demand video",
                        "Carbon emissions estimate: 147 kg"
                    ]
                }
            ],
            "total_duration": 260,
            "carbon_emissions": {
                "this_flight": 147000,
                "typical_for_this_route": 252000,
                "difference_percent": -42
            },
            "price": 1081,
            "type": "Round trip",
            "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/SQ.png",
            "booking_token": "WyJDalJJY1hJemFVbE5XRWc1V0d0QlFtbFBaa0ZDUnkwdExTMHRMUzE1YVdGdk9DMXVNVUZCUVVGQlIzTkdUMVF3UnpGNlUxbEJFZ1ZUVVRnMU1Sb0xDSWpNQmhBQ0dnTlRSMFE0SEhEVGpRVT0iLFtbIlNJTiIsIjIwMjctMDItMDQiLCJDQU4iLG51bGwsIlRSIiwiMTAwIl1dLFtbIkNBTiIsIjIwMjctMDItMDkiLCJTSU4iLG51bGwsIlNRIiwiODUxIl1dXQ=="
        }
    ]
}