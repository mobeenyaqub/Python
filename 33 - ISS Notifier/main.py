import requests

parameters = {
    "lat": -1,
    "lng": -1
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.raise_for_status())
data = response.json()["results"]["sunrise"]
print(data)
