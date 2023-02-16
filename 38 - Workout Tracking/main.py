import requests
from data import *

message = input("Enter your workout routine: ")

exercise_parameters = {
    "query": message,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 178,
    "age": 21
}

nutritionix_response = requests.post(url=NUTRITIONIX_URL, json=exercise_parameters, headers=exercise_headers)
nutritionix_result = nutritionix_response.json()

sheety_response = requests.get(url=SHEETY_URL)

for exercise in nutritionix_result["exercises"]:
    sheety_params = {
        "sheet1": {
            "date": TODAY_DATE,
            "time": TODAY_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=SHEETY_URL, json=sheety_params, headers=headers)
