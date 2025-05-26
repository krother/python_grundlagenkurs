from pprint import pprint

import httpx

url = "https://v6.bvg.transport.rest/locations"

params = {
    "poi": False,
    "addresses": False,
    "query": "Kaisereiche",
}

response = httpx.get(url, params=params)
print(response.status_code)

stationen = response.json()
print(f"{len(stationen)} gefunden")
pprint(stationen[:3])
