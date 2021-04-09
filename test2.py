import requests
import json
from datetime import datetime


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

parameters = {
    "by_postal": 14203
}

response = requests.get("https://api.openbrewerydb.org/breweries", params=parameters)

jprint(response.json())

place_list = []

for d in response.json():
	place_address = d['name'] + ', ' + d['street'] + ', ' + d['city'] + ', ' + d['state'] + ', ' + d['postal_code'] 
	place_list.append(place_address)

print(place_list)

for r in place_list:
	print(r)

