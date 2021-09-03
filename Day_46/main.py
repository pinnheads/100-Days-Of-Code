import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

client_id = "Enter ID"
client_secret = "Secret"

# Ask user for a date
user_input = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD"
)

# Build url based on user input
base_url = "https://www.billboard.com/charts/hot-100/"
req_url = base_url + user_input

# Get Billboard data
response = requests.get(url=req_url)
data = response.text

# Make soup
soup = BeautifulSoup(data, "html.parser")

# Extract top 100 songs name
top_songs = [
    song.string
    for song in soup.find_all(
        name="span",
        class_="chart-element__information__song text--truncate color--primary",
    )
]

# Authentication with spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt",
    )
)

# Get user ID
user_id = sp.current_user()["id"]

# Search and add song uris from spotify
song_uris = []
year = user_input.split("-")[0]
for song in top_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Get the amount of songs found in spotify
songs_amt = len(song_uris)

# Create a spotify playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{user_input}_Top_{songs_amt}",
    public=False,
    collaborative=False,
    description=f"Top {songs_amt} on the day {user_input}",
)

# Get the new playlist id
playlist_id = playlist["id"]

# Add all the songs to the new playlist
sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist_id, tracks=song_uris
)
