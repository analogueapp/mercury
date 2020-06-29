import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_skey = os.getenv('SPOTIFY_CLIENT_SKEY')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        spotify_client_id, spotify_client_skey
    )
)

def search_music(query):
    spotify_result = spotify.search(query,limit=10,type='track',market=None,offset=0)
    
    result = []

    for each in spotify_result['tracks']['items']:
        single_result = {}

        single_result['title'] = each['name']
        single_result['track_number'] = each['track_number']
        single_result['popularity'] = each['popularity']
        single_result['preview_url'] = each['preview_url']
        single_result['url'] = each['external_urls']['spotify']
        single_result['duration'] = each['duration_ms']
        single_result['artists'] = [singer['name'] for singer in each['artists']]
        single_result['track_album'] = each['album']['name']
        single_result['track_album_image'] = each['album']['images'][0]

        result.append(single_result)
        del single_result

    return result

def search_podcast(query):
    spotify_result = spotify.search(query,limit=10,type='show',market='US',offset=0)

    result = []

    for each in spotify_result['shows']['items']:
        single_result = {}

        single_result['title'] = each['name']
        single_result['description'] =  each['description']
        single_result['publisher'] = each['publisher']
        single_result['image'] = each['images'][0]
        single_result['url'] = each['external_urls']['spotify']
        single_result['languages'] = each['languages']

        result.append(single_result)
        del single_result

    return result