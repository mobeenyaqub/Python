import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "graph2",
    "name": "programming_graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime(year=2022, month=9, day=1)

pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "80.5"
}

response = requests.post(url=f"{graph_endpoint}/graph2", json=pixel, headers=headers)
print(response.text)
