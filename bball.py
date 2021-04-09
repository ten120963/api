import requests
import json
from operator import itemgetter

year_parameter = input("Please enter a Year: ")
team_parameter = input("Please enter a Team Name: ")

team_response = requests.get("https://www.balldontlie.io/api/v1/teams")

#print(team_response.status_code)
#print(team_response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(team_response.json())

for c in team_response.json()['data']:
	if str(c['abbreviation']) == team_parameter:
		team_id = str(c['id'])
	'''
	print("id: " + str(c['id']))
	print("full name: " + str(c['full_name']))
	print("------------------------------------------")	
	print(" ")
	#print(c)
	'''

response = requests.get("https://www.balldontlie.io/api/v1/games?seasons[]=" + year_parameter + "&team_ids[]=" + team_id + "&per_page=100")

#print(response.status_code)
#print(response.json())

#jprint(response.json())


for d in sorted(response.json()['data'], key=itemgetter('date')):	
	print("date: " + str(d['date']))
	print("home team: " + str(d['home_team']['full_name']))
	print("home team score: " + str(d['home_team_score']))
	print("visitor team: " + str(d['visitor_team']['full_name']))
	print("visitor team score: " + str(d['visitor_team_score']))	
	print("------------------------------------------")	
	print(" ")
	#print(d)

#jprint(response.json()['data'])

