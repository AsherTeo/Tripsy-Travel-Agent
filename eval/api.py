import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from datetime import datetime, date
from zoneinfo import ZoneInfo


def find_real_flight(flight_code, target_date):
    url = f'https://www.flightradar24.com/data/flights/{flight_code}'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(url, wait_until='domcontentloaded')

        page.wait_for_timeout(5000)

        html = page.content()

        browser.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.select('[role="region"] article[data-flight-id]')

    some_lst = []

    for row in rows:
        time_tag = row.select_one('time[datetime]')
        dates = time_tag['datetime'] if time_tag else None
        links = row.select('a[href*="/data/airports/"]')

        if len(links) < 2:
            continue
        dep = links[0].select_one('span.leading-none').get_text(strip=True)   
        arr = links[1].select_one('span.leading-none').get_text(strip=True)

        
        stdd = None
        for label in row.select('span.sr-only'):
            if label.get_text(strip=True) == 'STD:':
                std = label.parent.get_text(strip=True).replace('STD:', '', 1).strip()
                current = date.today()
                d = datetime.strptime(dates, "%Y-%m-%d").date()
      
                if d == date.fromisoformat(target_date):
                    stdd = datetime.strptime(std, "%I:%M %p").strftime("%H:%M")
        
                    if not any(item['outbound_time'] == stdd for item in some_lst):
                        some_lst.append({
                            'outbound_date':dates,
                            #'return_date':return_date,
                            'departure_id': dep,
                            'arrival_id':arr,
                            'outbound_time': stdd,
                            #'return_time': return_time
                        })
                break
        # some_dict.append(some_lst)
    return some_lst

# a = find_real_flight('SQ314')
# print(a)