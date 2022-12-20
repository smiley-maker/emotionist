import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd


env_path = Path('.') / '.env'
load_dotenv()
cid = os.environ['CLIENT_ID_']
secret = os.environ['CLIENT_SECRET_']


def getData(cid, secret, playlist_link):
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    rows = []

    for track in sp.playlist_tracks(playlist_URI)["items"]:
        track_uri = track["track"]["uri"]
        track_name = track["track"]["name"]
        artist_uri = track["track"]["artists"][0]["uri"]
        artist_info = sp.artist(artist_uri)
        artist_name = track["track"]["artists"][0]["name"]
        artist_pop = artist_info["popularity"]
        artist_genres = artist_info["genres"]
        album = track["track"]["album"]["name"]
        track_pop = track["track"]["popularity"]
        rows.append([track_uri, track_name, artist_uri, artist_info, artist_name, artist_pop, artist_genres, album, track_pop])

    df = pd.DataFrame(rows, columns=["Track URI", "Track Name", "Artist URI", "Artist Info", "Artist Name", "Artist Popularity", "Artist Genres", "Album", "Track Popularity"])
    print(df.head())
    return df





#Authentication - without user
#client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
getData(cid, secret, playlist_link)