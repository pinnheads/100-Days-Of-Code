import requests
import json
from os import environ
from twilio.rest import Client

account_sid = environ.get("TWILIO_ACC_SID")
api_key = environ.get("OWM_API_KEY")
auth_token = environ.get("TWILIO_AUTH_TOKEN")
my_number = environ.get("MY_PHONE_NO")

one_call_url = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lon": 77.6033,
    "lat": 12.9762,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts",
}

response = requests.get(url=one_call_url, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

# Testing
# json_data = json.dumps(hourly_data, indent=4)

# with open("response.json", "w") as response_file:
#     response_file.write(json_data)

will_rain = False

for hour_data in hourly_data:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        # print(f"{id} -> {hour_data['weather'][0]['id']} ") ---> Testing
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella! It will rain.",
        from_="+15625488293",
        to=my_number,
    )
    print(message.status)
