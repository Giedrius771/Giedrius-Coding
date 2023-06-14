## 1 uzduotis #####
import requests
import re


def kaciu_nuotraukos(num_photos):
    for i in range(num_photos):
        r = requests.get('http://random.cat/')
        response_text = r.text
        image_url_match = re.search(r'<img src="(.*?)"', response_text)
        if image_url_match:
            image_url = image_url_match.group(1)
            image_data = requests.get(image_url).content
            with open(f'cat{i + 1}.jpg', 'wb') as f:
                f.write(image_data)
            print(f'Nuotrauka {i + 1} išsaugota.')
        else:
            print(f'Nuotrauka {i + 1} negalima.')


kaciu_nuotraukos(5)
###### 2 uzduotis #####
import requests


def gauti_info_serverio(urls):
    serveriai = []
    for url in urls:
        try:
            response = requests.head(url)
            server = response.headers.get('Server')
            serveriai.append(server)
        except requests.exceptions.RequestException as e:
            serveriai.append(str(e))
    return serveriai


urls = [
    "https://www.google.com/",
    "https://www.delfi.lt/",
    "https://www.15min.lt/",
    "https://www.lrytas.lt/",
    "http://www.google.com/"
]

serveriai = gauti_info_serverio(urls)
print(serveriai)
##### 3 uzduotis #####
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
