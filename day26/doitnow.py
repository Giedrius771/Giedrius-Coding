import requests
import csv
from keys import geoip_apikey, openweather_apikey

geoip_url = "https://freegeoip.app/json/"
openweather_url = "https://api.openweathermap.org/data/2.5/weather"

ip_list = ['78.61.177.42', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174',
           '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']


def convert_to_celsius(temp):
    return round((temp - 32) * 5 / 9, 2)


with open('weather_forecast.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['IP', 'Country', 'City', 'Temp (C)', 'Weather'])

    for ip in ip_list:
        # Gauti info is freegeoip
        geoip_params = {
            'apiKey': geoip_apikey,
        }
        geoip_response = requests.get(geoip_url + ip, params=geoip_params)
        geoip_data = geoip_response.json()

        if 'country_name' in geoip_data:
            country = geoip_data['country_name']
        else:
            country = 'N/A'

        if 'city' in geoip_data:
            city = geoip_data['city']
        else:
            city = 'N/A'

        # Gauti info is OpenWeatherMap
        openweather_params = {
            'q': city + ',' + country,
            'units': 'imperial',
            'appid': openweather_apikey
        }
        openweather_response = requests.get(openweather_url, params=openweather_params)
        openweather_data = openweather_response.json()

        if 'main' in openweather_data:
            temperature = openweather_data['main']['temp']
            temperature_celsius = convert_to_celsius(temperature)
        else:
            temperature = 'N/A'
            temperature_celsius = 'N/A'

        if 'weather' in openweather_data and len(openweather_data['weather']) > 0:
            weather_description = openweather_data['weather'][0]['description']
        else:
            weather_description = 'N/A'

        writer.writerow([ip, country, city, temperature_celsius, weather_description])

        print(f"Weather for IP: {ip}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"Temperature: {temperature_celsius}°C")
        print(f"Weather: {weather_description}")
        print("=========================")

print("CSV file generated successfully.")
