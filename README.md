# DataSocietyAssignment

#### Write a weather-forecasting application that takes geographic US latitude/longitude values as input and presents the weather from a point in time at the given location(s). Use a language and presentation method of your choice.

#### This application should:
- Accept geographic US latitude/longitude values as input
- For example: 39.7456, -97.0892

#### Retrieve weather data using this free weather service: API Web Service (https://www.weather.gov/documentation/services-web-api&sa=D&source=calendar&ust=1641768438693965&usg=AOvVaw3OWCV8Z2DjkIpuF6eXz_L2)

### Present the “temperature” value for “Wednesday Night” at the input location

- Your chosen tools will dictate your presentation method, but the key to this requirement is that the end-user receives the resulting forecast data. 
- This could be done via a dynamic web page, command-line output, etc.
- Along with the source code, include a README.md file in Markdown format which documents your solution and how to use it. Deliver the application via shared git repository (e.g. GitHub, BitBucket).

#### Tech Stack 
- Frontend : HTML,CSS,JS,BOOTSTRAP
- Backend : Flask(Python)
- Deployed using Heroku

#### Web Application URL : https://datasocietywebapp.herokuapp.com/

#### Features included in the application

1) User can find the temperature of a given latitude and longitude on "Wedenesday Night" as specified in the SRS by typing the latitude and longitude in the form on the webpage.
3) If the given latitude and longitude details do not exist in the api(https://www.weather.gov/documentation/services-web-api&sa=D&source=calendar&ust=1641768438693965&usg=AOvVaw3OWCV8Z2DjkIpuF6eXz_L2) mentioned in SRS , Sorry message is displayed to the user.

#### Here are some latitudes and longitudes of the cities in US(United States) that can be used to test the web page by the user.

- Fort Valley, GA, USA              32.559334 , -83.904587
- Douglas, GA, USA                  31.504131 , -82.867790
- Darien, GA, USA                   31.375116 , -81.436729
- Brunswick, GA, USA                31.164404 , -81.505600
- Bainbridge, GA, USA               30.903612 , -84.585205
- Melbourne, FL, USA                28.118488 , -80.670372
- New Castle, DE, USA               39.668564 , -75.586189
- Miami Beach, FL, USA              25.793449 , -80.139198
- South San Francisco, CA, USA      37.662937 , -122.433014
- San Marino, CA, USA               34.121300 , -118.132607

### Screenshots of the web application

#### When you open the webpage, this is how you'll find it.

![firstpage](/images/firstpage.PNG)

#### Enter latitude and longitude and click on "Get weather details"

![secondpage](/images/secondpage.PNG)

#### The output screen when you give the correct latitude and longitude as specified in SRS.

![thirdpage](/images/thirdpage.PNG)

#### Let's say you type false latitude and longitude( That don't exist/ That which do not exist in the API used )

![wrong details](/images/wrongdetails.PNG)

#### The output screen when you type wrong details.

![ifwrong](/images/ifwrong.PNG)



