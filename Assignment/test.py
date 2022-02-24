import requests
import json
latitude="39.7456"
longitude="-97.0892"

complete_api_link = "https://api.weather.gov/points/"+latitude+","+longitude

api_link = requests.get(complete_api_link)
api_data = api_link.json()
if api_data['status']==404:
    return("Hi")
else:
    print("No Hi")

final_api_link = api_data["properties"]["forecast"]

api_ans = requests.get(final_api_link)

final_data = api_ans.json()

for i in final_data["properties"]["periods"]:
    if i["name"]=="Wednesday Night":
        name = i["name"]
        temp = i["temperature"]
        wind_speed = i["windSpeed"]
        weather_desc = i["detailedForecast"]
        break
    else:
        name = "Weather Data for Wednesday Night is not available here"
        temp = 'NA'
        wind_speed = 'NA'
        weather_desc = 'NA'