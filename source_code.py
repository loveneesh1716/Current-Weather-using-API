import requests
from datetime import datetime

user_api = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
location = input("Enter city name: ")

complete_api_link = user_api+location
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("Weather Stats for -> {} ".format(location.upper() ))
print ("Date And Time     -> {} ".format(date_time))
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
