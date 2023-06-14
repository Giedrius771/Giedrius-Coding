import requests
import json

api_key = "7e88e657b0ff90bbc5af70683581a1fe"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Iveskite miesto pavadinima: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
    weather_description = z[0]["description"]

    temperature_in_celsius = round(current_temperature - 273.15)

    print("Temperature is " + str(temperature_in_celsius) + "°C")
    print("Description: " + str(weather_description))

else:
    print("Miestas nerastas")
