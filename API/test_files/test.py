import requests
import json
import time


temperature = 100
humidite = 100
capteur = 'test'
farenheit = 30

while True:

    url = "http://127.0.0.1:5000/api/v1/ajouter/"
    payload = json.dumps({
        "capture": capteur,
        "humidite": humidite,
        "temperature": temperature,
        "farenheit" :  farenheit
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(10)
