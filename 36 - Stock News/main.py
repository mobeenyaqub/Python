import requests
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alpha_api_key = ""
alpha_url = "https://www.alphavantage.co/query"

news_api_key = ""
news_url = "https://newsapi.org/v2/everything"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key
}


def send_alert(msg):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=msg,
                         from_='',
                         to=''
                     )


def alpha_process(a=True):
    alpha_response = requests.get(url=alpha_url, params=alpha_parameters)
    alpha_data = alpha_response.json()

    dictionary = {key: value for key, value in alpha_data['Time Series (Daily)'].items()}
    keys = list(alpha_data['Time Series (Daily)'])  # dates

    yesterday = keys[1]
    yesterday_close = float((dictionary[yesterday]['4. close']))

    day_before_yesterday = keys[2]
    day_before_yesterday_close = float((dictionary[day_before_yesterday]['4. close']))

    if a:
        return abs(yesterday_close - day_before_yesterday_close)
    else:
        return keys[0]


news_parameters = {
    "q": STOCK,
    "from": alpha_process(False),
    "sortBy": "popularity",
    "apiKey": news_api_key
}

if alpha_process() >= 5:
    news_response = requests.get(url=news_url, params=news_parameters)
    news_data = news_response.json()['articles']
    k = list(news_data[0])

    for i in range(0, 3):
        message = f"Headline: {news_data[i][str(k[2])]}\n\nBrief: {news_data[i][str(k[3])]}"
        send_alert(message)
