from datetime import datetime

APP_ID = ""
API_KEY = ""
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = ""
TODAY_DATE = datetime.today().strftime("%d/%m/%Y")
TODAY_TIME = datetime.today().strftime("%H:%M:%S")
BEARER_AUTH = ""

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

headers = {
    "authorization": f"Bearer {BEARER_AUTH}"
}