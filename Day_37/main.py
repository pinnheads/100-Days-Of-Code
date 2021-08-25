import requests
import datetime as dt
from os import environ

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "pinnheads"
TOKEN = environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Set new user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

# Create a graph
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = (dt.datetime.now() - dt.timedelta(days=5)).strftime("%Y%m%d")

# Add a Pixel
pixel_params = {"date": today, "quantity": "12.5"}

response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_params)
print(response.text)

# Change a Pixel data
pixel_change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=pixel_change_endpoint, headers=headers)
