import requests
from bs4 import BeautifulSoup, SoupStrainer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Dict, Optional
from apis.wikipedia import get_short_details, search_google, WikiUrlTitle
from constants import wikipedia_url
import os
from urllib.parse import urlparse

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_skey = os.getenv('SPOTIFY_CLIENT_SKEY')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        spotify_client_id, spotify_client_skey
    )
)

def parse_wiki_url(title: str, content: str, creator: Optional[str] = None) -> str:
    
    if content == WikiUrlTitle.artist:
        title = title + ' musician wikipedia'

    elif content == WikiUrlTitle.show:
        title = title + ' podcast wikipedia'
    
    elif content == WikiUrlTitle.track:
        title = title + ' ' + creator + ' song wikipedia'

    url = search_google(title)
    return url




def parse_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)


def spotify_get(url: str) -> Dict:

    api_data = {}
    parse_url = urlparse(url)
    spotify_id = parse_url.path.split('/')[2]
    spotify_type = parse_url.path.split('/')[1]

    uri = "spotify:%s:%s" % (spotify_type, spotify_id)

    if spotify_type == "artist": #wiki data added

        artist = spotify.artist(spotify_id)
        artist_album = spotify.artist_albums(uri, album_type='album', limit= 5)
        artist_top_tracks = spotify.artist_top_tracks(uri)
        api_data["artist_details"] = artist
        api_data["artist_albums"] = artist_album
        api_data["top_tracks"] = artist_top_tracks['tracks']

        wiki_url = parse_wiki_url(api_data['artist_details']['name'] , WikiUrlTitle.artist)
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "playlist":

        playlist = spotify.playlist(uri)
        playlist_items = spotify.playlist_tracks(uri, limit=5)

        api_data["playlist_details"] = playlist
        api_data["playlist_tracks"] = playlist_items

    elif spotify_type == "show": #wiki data added

        show = spotify.show(uri, market="US")
        show_episodes = spotify.show_episodes(uri, market="US")

        api_data["show_details"] = show
        api_data["episodes"] = show_episodes

        wiki_url = parse_wiki_url(api_data["show_details"]['name'] , WikiUrlTitle.show)
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "track": #wiki data added
        track = spotify.track(uri)
        api_data["track_details"] = track

        wiki_url = parse_wiki_url(api_data['track_details']['name'], WikiUrlTitle.track, api_data['track_details']['artists'][0]['name'])
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "episode":
        episode = spotify.episode(uri, market="US")
        api_data["episode_details"] = episode
    
    elif spotify_type == "album":
        album = spotify.album(uri)
        api_data['album_details'] = album
    
    return api_data