from pprint import pprint
import requests
import os

SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/6deea1b1bdb483b6fca93ef2efc9254e/flightDeals/prices"
)


class DataManager:
    def __init__(self):
        self.sheety_auth_token = f"Bearer {os.environ['SHEETY_AUTH_TOKEN']}"
        self.sheety_url = (
            "https://api.sheety.co/6deea1b1bdb483b6fca93ef2efc9254e/flightDeals/prices"
        )
        self.headers = {"Authorization": self.sheety_auth_token}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers,
            )
            print(response.text)
