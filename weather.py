import requests
import json

parameters = input("Please enter a City or part of a City Name: ")

response = requests.get("https://www.metaweather.com/api/location/search/?query=" + parameters)
#response = requests.get("https://www.metaweather.com/api/location/search/?lattlong=35.666431,-105.972572")
#response = requests.get("https://www.metaweather.com/api/location/44418/")

print(response.status_code)
print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

woeid_parm = ''

for c in response.json():
    print("woeid: " + str(c['woeid']))
    woeid_parm = c['woeid']
    #print(c)

new_response = requests.get("https://www.metaweather.com/api/location/" + str(woeid_parm) + "/")

print(new_response.status_code)
print(new_response.json())
jprint(new_response.json())

print("City: " + new_response.json()['title'])
print("State: " + new_response.json()['parent']['title'])
print("Sunrise: " + new_response.json()['sun_rise'])
print("Sunset: " + new_response.json()['sun_set'])
print("Timezone: " + new_response.json()['timezone'])
print("------------------------------------------")	
print(" ")

for d in new_response.json()['consolidated_weather']:
	print("applicable_date: " + str(d['applicable_date']))
	print("max_temp: " + str(d['max_temp']))
	print("min_temp: " + str(d['min_temp']))
	print("wind_direction_compass: " + str(d['wind_direction_compass']))
	print("wind_speed: " + str(d['wind_speed']))
	print("weather_state_name: " + str(d['weather_state_name']))
	print("------------------------------------------")	
	print(" ")
	#print(d)

