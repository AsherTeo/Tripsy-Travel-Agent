from datetime import datetime, date,timedelta
#from model_llm import load_llm
import random

def get_answer(prompt):
    if 'retry' in prompt:
        return 'n'
    if 'flight number from' in prompt:
        return '1'
  

def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{['th','st','nd','rd','th','th','th','th','th','th'][n % 10]}"

def format_date(d, include_year=True):
    day, mon_short, mon_full = d.day, d.strftime("%b"), d.strftime("%B")
    year = d.year

    styles = [
        f"{day} {mon_short} {year}",            # 3 Dec 2026
        f"{day:02d} {mon_short} {year}",        # 03 Dec 2026
        f"{mon_short} {day} {year}",            # Dec 3 2026
        f"{mon_full} {day}, {year}",            # December 3, 2026
        f"{ordinal(day)} {mon_full} {year}",    # 3rd December 2026
        f"{ordinal(day)} of {mon_full}, {year}",# 3rd of December, 2026
        f"{day} {mon_short.lower()} {year}",    # 3 dec 2026
        f"{day} {mon_short} {str(year)[2:]}",   # 3 Dec 26
        f"{d:%a} {day} {mon_short} {year}",     # Thu 3 Dec 2026
        d.strftime("%Y-%m-%d"),                 # 2026-12-03
        d.strftime("%Y/%m/%d"),                 # 2026/12/03
    ]
    return random.choice(styles)

def choose_template(out):
    ret = out + timedelta(random.randint(1, 8)) 

    destinations = [
        ("Tokyo Haneda Airport", "HND"),
        ("Tokyo Narita International Airport", "NRT"),
        ("London, Heathrow Airport", "LHR"),
        ("London, Gatwick Airport", "LGW"),
        ("Chiang Mai International Airport", "CNX"),
        ("Jakarta International Airport", "CGK"),
        ("Seoul Incheon International Airport", "ICN"),
    ]
    origins = ["Singapore", "SG", "singapore"]
    travel_class = [("", 1),("economy", 1),("premium economy", 2),("business class", 3),("first class", 4)]
  
    origin  = random.choice(origins)
    dest, _ = random.choice(destinations)
    choice, cls = random.choice(travel_class)
    outs = format_date(out)
    rets = format_date(ret)

    round_trip_templates = [
        f"{origin} to {dest} {outs} to {rets} {choice}",
        f"{origin} to {dest}, departing {outs}, returning {rets}. {choice}",
        f"Hey, I'm looking to fly from {origin} to {dest} from {outs} to {rets}. Can you find me the cheapest flights? {choice}",
        f"i want to fly to {dest} on {outs}, coming back {rets} {choice}",
        f"flight SIN to {dest} leaving {outs} returning {rets} {choice}",
    ]
    one_way_templates = [
        f"pls find flight {origin} to {dest} {outs} one way {choice}",
        f"just need to get to {dest} on {outs}, will book the return later {choice}",
        f"{origin} -> {dest} {outs} single trip {choice}",
        f"I'm currently in {origin}. I need to land at {dest} on {out}. What flight should I take?{choice}",
    ]

    roundtrips = random.random() < 0.6
    templates = (round_trip_templates if roundtrips else one_way_templates)
    input = random.choice(templates)
    
    return {
        'inputs': {'query': input},
        'outputs':{
            "outbound_date": date.strftime(out, "%Y-%m-%d"), 
            "return_date": date.strftime(ret, "%Y-%m-%d") if roundtrips else None,
            "travel_class": cls,
            "type": int(1) if roundtrips else int(2)
        }
    }


def make_dataset():
    current = date.today()
    random_day = current + timedelta(days= random.randint(1, 7))
    new_input = choose_template(random_day)
    
    return new_input

import json 

def gnr_dateset(name_dataset, number_of_dataset):
    path = f'eval/{name_dataset}.json'
    stored = []

    for _ in range(number_of_dataset + 1):
        stored.append(make_dataset())

    with open(path, 'w') as file:
        json.dump(stored, file, indent=4)
    
    return path

