"""
Abfahrten vom BVG-Server ermitteln:
https://v6.bvg.transport.rest/
"""

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


from datetime import datetime

s = '2025-05-24T19:24:00+02:00'
d = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S+%f:00")
print(d.hour)
print(d.minute)
