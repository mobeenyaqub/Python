import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

link1 = "https://api.openweathermap.org/data/2.5/weather"
link2 = "https://api.openweathermap.org/data/3.0/onecall"

parameters = {
    "lat": -1,
    "lon": -1,
    "appid": "",
    "exclude": "current,minutely,daily"
}
response = requests.get(url=link1, params=parameters)
print(response.status_code)

weather_data = response.json()
print(weather_data)
