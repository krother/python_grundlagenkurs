from pprint import pprint

import httpx

station_id = "900061104"
url = "https://v6.bvg.transport.rest/stops/900061104/departures"


params = {
    "results": 5,
}

response = httpx.get(url, params=params)
print(response.status_code)

abfahrten = response.json()["departures"]
pprint(abfahrten[0])
