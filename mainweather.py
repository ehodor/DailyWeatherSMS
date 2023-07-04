#Created by Emma Hodor

import requests
import datetime as dt
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
proxy = TwilioHttpClient()
proxy.session.proxies = {"https": os.environ["https_proxy"]}
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("SID")
auth_token = os.environ.get("TOKEN")
phone_number = os.environ.get("PHONE")
key_api = os.environ.get("API")
twilio_phone = os.environ.get("TWILIO")

ep_params = {
    "lat": 40.743992 ,
    "lon": -74.032364,
    "appid": key_api,
}

response = requests.get(weather_endpoint, params=ep_params)
response.raise_for_status()
json_data = response.json()
threehr_weather=json_data["list"][0]["weather"][0]["id"]
cur_time = dt.datetime.now()
#if cur_time.hour == "07":

if threehr_weather < 900:
    main_weather = json_data["list"][0]["weather"][0]['main']
    client = Client(account_sid, auth_token, http_client=proxy)
    message = client.messages.create(
        body=f"{main_weather} expected within next three hours.",
        from_=f'+{twilio_phone}',
        to=f'+{phone_number}',
    )
    print(message.status)