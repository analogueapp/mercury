import requests
from bs4 import BeautifulSoup, SoupStrainer
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Dict, Optional
from apis.wikipedia import get_short_details, search_google, WikiUrlTitle
from constants import wikipedia_url
import os

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

    spotify_id = url.split("/")[-1]
    spotify_id = spotify_id.split('?')[0]
    spotify_type = url.split("/")[-2]

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

        playlist = spotify.playlist(spotify_id)
        playlist_items = spotify.playlist_tracks(spotify_id, limit=5)

        api_data["playlist_details"] = playlist
        api_data["playlist_tracks"] = playlist_items

    elif spotify_type == "show": #wiki data added

        show = spotify.show(spotify_id, market="US")
        show_episodes = spotify.show_episodes(spotify_id, market="US")

        api_data["show_details"] = show
        api_data["episodes"] = show_episodes

        wiki_url = parse_wiki_url(api_data["show_details"]['name'] , WikiUrlTitle.show)
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "track": #wiki data added
        track = spotify.track(spotify_id)
        api_data["track_details"] = track

        wiki_url = parse_wiki_url(api_data['track_details']['name'], WikiUrlTitle.track, api_data['track_details']['artists'][0]['name'])
        api_data['wiki_data'] = parse_data_from_wiki(wiki_url)

    elif spotify_type == "episode":
        episode = spotify.episode(spotify_id, market="US")
        api_data["episode_details"] = episode
    
    elif spotify_type == "album":
        album = spotify.album(spotify_id)
        api_data['album_details'] = album
    
    return api_data