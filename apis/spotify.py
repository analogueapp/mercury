import requests
from bs4 import BeautifulSoup, SoupStrainer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Dict, Optional
from apis.wikipedia import get_short_details
import os

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_skey = os.getenv('SPOTIFY_CLIENT_SKEY')
wikipedia_url = os.getenv('WIKIPEDIA_URL')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        spotify_client_id, spotify_client_skey
    )
)

def parse_wiki_url(title: str, content: str, creator: Optional[str] = None) -> str:
    
    title = title.replace(' ', '_')
    if content == 'artist':
        return wikipedia_url + title + '_(musician)'

    if content == 'show':
        return wikipedia_url + title + '_(podcast)'
    
    if content == 'track':
        creator = creator.replace(' ', '_')
        return wikipedia_url + title + '_(' + creator + '_song)'




def parse_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)


def spotify_get(url: str) -> Dict:

    api_data = {}

    spotify_id = url.split("/")[-1]
    spotify_type = url.split("/")[-2]

    uri = "spotify:%s:%s" % (spotify_type, spotify_id)

    if spotify_type == "artist": #wiki data added

        artist = spotify.artist(spotify_id)
        artist_album = spotify.artist_albums(spotify_id, limit=5)
        artist_top_tracks = spotify.artist_top_tracks(spotify_id)

        api_data["artist_details"] = artist
        api_data["artist_albums"] = artist_album
        api_data["top_tracks"] = artist_top_tracks

        wiki_url = parse_wiki_url(api_data['artist_details']['name'] , spotify_type)
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "playlist":

        playlist = spotify.playlist(spotify_id)
        playlist_items = spotify.playlist_tracks(spotify_id, limit=5)

        api_data["playlist_details"] = playlist
        api_data["playlist_tracks"] = playlist_items

    elif spotify_type == "show": #wiki data added

        show = spotify.show(spotify_id, market="US")
        show_episodes = spotify.show_episodes(spotify_id, market="US")

        api_data["show_details"] = show
        api_data["episodes"] = show_episodes

        wiki_url = parse_wiki_url(api_data["show_details"]['name'] , spotify_type)
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "track": #wiki data added
        track = spotify.track(spotify_id)
        api_data["track_details"] = track

        wiki_url = parse_wiki_url(api_data['track_details']['name'], spotify_type, api_data['track_details']['artists'][0]['name'])
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "episode":
        episode = spotify.episode(spotify_id, market="US")
        api_data["episode_details"] = episode

    return api_data