import requests
from bs4 import BeautifulSoup, SoupStrainer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = "cc05b898faef4c89b0e9ad87e37b8158"
SPOTIFY_CLIENT_SECRET = "ec2d58eea4e446a28fa120e49567fbfc"

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
    )
)


def spotify_get(url):
    
    api_data = {}

    spotify_id = url.split("/")[-1]
    spotify_type = url.split("/")[-2]

    uri = "spotify:%s:%s" % (spotify_type, spotify_id)

    if spotify_type == "artist":

        artist = spotify.artist(spotify_id)
        artist_album = spotify.artist_albums(spotify_id, limit=5)
        artist_top_tracks = spotify.artist_top_tracks(spotify_id)

        api_data["artist_details"] = artist
        api_data["artist_albums"] = artist_album
        api_data["top_tracks"] = artist_top_tracks

    elif spotify_type == "playlist":

        playlist = spotify.playlist(spotify_id)
        playlist_items = spotify.playlist_tracks(spotify_id, limit=5)

        api_data["playlist_details"] = playlist
        api_data["playlist_tracks"] = playlist_items

    elif spotify_type == "show":

        show = spotify.show(spotify_id, market="US")
        show_episodes = spotify.show_episodes(spotify_id, market="US")

        api_data["show_details"] = show
        api_data["episodes"] = show_episodes

    elif spotify_type == "track":

        track = spotify.track(spotify_id)

        api_data["track_details"] = track

    elif spotify_type == "episode":

        episode = spotify.episode(spotify_id, market="US")

        api_data["episode_details"] = episode

    return api_data
