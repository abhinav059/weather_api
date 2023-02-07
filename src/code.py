
import requests

import os

from datetime import datetime

api_key = "2de3320c8a170ed55152347fa1cdb391"

user_location_input = input("ENTER THE CITY NAME: ")

api_url = f"https://api.openweathermap.org/data/2.5/weather?q={user_location_input}&appid={api_key}"

api_link = requests.get(api_url)  # api get request
api_data = api_link.json() #storing the data in json format 

if api_data["cod"] == "404":
    print("INVALID INPUT! PLEASE CHECK YOUR LOCATION")
else:
    temperature = (api_data["main"]["temp"]) - 273.15
    weather = api_data["weather"][0]["description"]
    humidity = api_data["main"]["humidity"]
    wind = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p ")

    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    print(f"WEATHER OF {user_location_input} ON {date_time}")
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")

    print("CURRENT TEMPERATURE:{:.2f} deg C".format(temperature))
    print(f"CURRENT WEATHER: {weather}")
    print(f"HUMIDITY: {humidity}")
    print(f"WIND SPEED: {wind}")

    print("THANK YOU 🙂")
    print("RUN AGAIN TO GET ANOTHER RESULT")

