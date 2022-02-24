from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():

    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        complete_api_link = "https://api.weather.gov/points/"+latitude+","+longitude

        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        if len(api_data)>5:
            return render_template("error.html")
        else:
            final_api_link = api_data["properties"]["forecast"]

            api_ans = requests.get(final_api_link)

            final_data = api_ans.json()
            flag=0


            for i in final_data["properties"]["periods"]:
                if i["name"]=="Wednesday Night":
                    name = i["name"]
                    temp = i["temperature"]
                    wind_speed = i["windSpeed"]
                    weather_desc = i["detailedForecast"]
                    flag=1
                    break
            
            if flag==1:
                return render_template("result.html",name=name,temp=temp,wind_speed=wind_speed,weather_desc=weather_desc)
            else:
                name = "Weather Data for Wednesday Night is not available here"
                temp = 'NA'
                wind_speed = 'NA'
                weather_desc = 'NA'
                return render_template("result.html",name=name,temp=temp,wind_speed=wind_speed,weather_desc=weather_desc)
        
    return render_template("index.html")