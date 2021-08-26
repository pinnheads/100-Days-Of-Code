import requests
from os import environ
import datetime as dt

nutrix_id = environ.get("NUTRIX_APP_ID")
nutrix_api_key = environ.get("NUTRIX_APP_KEY")
sheety_auth_token = environ.get("SHEETY_AUTH_TOKEN")
my_gender = environ.get("GENDER")
my_weight = environ.get("WEIGHT")
my_height = environ.get("HEIGHT")
my_age = environ.get("AGE")

exercise_text = input("What exercises did you do? ")

sheety_headers = {"Authorization": f"Bearer {sheety_auth_token}"}

sheety_url = (
    "https://api.sheety.co/6deea1b1bdb483b6fca93ef2efc9254e/myWorkouts/workouts"
)
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutrix_id,
    "x-app-key": nutrix_api_key,
}

parameters = {
    "query": exercise_text,
    "gender": my_gender,
    "weight_kg": my_weight,
    "height_cm": my_height,
    "age": my_age,
}


response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
data = response.json()
required_data = data["exercises"]


for index in range(len(required_data)):
    data_to_save = {
        "workout": {
            "date": (dt.datetime.now()).strftime("%d/%m/%Y"),
            "time": (dt.datetime.now()).strftime("%H:%M:%S"),
            "exercise": required_data[index]["name"],
            "duration": required_data[index]["duration_min"],
            "calories": required_data[index]["nf_calories"],
        }
    }
    response = requests.post(url=sheety_url, headers=sheety_headers, json=data_to_save)
    response.raise_for_status()


sheety_get = requests.get(url=sheety_url, headers=sheety_headers)
print(sheety_get.text)
