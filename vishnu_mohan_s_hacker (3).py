# -*- coding: utf-8 -*-
"""VISHNU MOHAN.S HACKER

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sShwA1qizS9RNFJo1y6kVZ82-9WHPq8g
"""

import requests

"""#include os"""

from datetime import datetime

api_key='fe53d4a2a5d01dc4440c92da4dfcca32'
location=input("Enter the city name:")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q=thiruvananthapuram&appid=fe53d4a2a5d01dc4440c92da4dfcca32"
api_link=requests.get(complete_api_link)
api_data=api_link.json()

"""#create variable to store and display data"""

temp__city=((api_data['main']['temp'])-273.15)
weather_disc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %Y | %I:%H:%S %p")

print("--------------------------------------------------------------")
print("Weather stats for -{} || {}".format(location.upper(), date_time))
print("----------------------------------------------------------")

print("Current temperature is:{:.2f} deg C".format(temp__city))
print("Current weather disc  : ",weather_disc)
print("Current Humidity      :",hmdt,'%')
print("Current wind speed    :",wind_spd,'kmph')