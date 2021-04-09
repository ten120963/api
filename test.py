import requests
import json
from datetime import datetime

response = requests.get("http://api.open-notify.org/astros.json")

print(response.status_code)
print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

for d in response.json():
    print(d, response.json()[d])

people = response.json()['people']
jprint(people)   

for p in response.json()['people']:
    print(p['craft'])
    print(p['name'])

parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

jprint(response.json())

test_request = response.json()['request']
jprint(test_request)

for c in response.json()['request']:
    print(c, response.json()['request'][c])

pass_times = response.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)

print(times)    
