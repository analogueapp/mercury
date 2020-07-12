import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import difflib
from concurrent.futures import ThreadPoolExecutor
import os

spotify_client_id = os.getenv('SPOTIFY_CLIENT_ID')
spotify_client_skey = os.getenv('SPOTIFY_CLIENT_SKEY')

spotify = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        spotify_client_id, spotify_client_skey
    )
)

def search_song(query):
    spotify_result = spotify.search(query,limit=5,type='track',market=None,offset=0)
    
    result = []

    for each in spotify_result['tracks']['items']:
        if each is not None:
            single_result = {}

            single_result['title'] = each['name']
            single_result['url'] = each['external_urls']['spotify']
            single_result['creators'] = [singer['name'] for singer in each['artists']]
            single_result['image'] = each['album']['images'][0]['url']
            single_result['medium'] = 'song'

            result.append(single_result)
            del single_result

    return result


def search_album(query):
    spotify_result = spotify.search(query,limit=5,type='album',market=None,offset=0)
    
    result = []

    for each in spotify_result['albums']['items']:
        if each is not None:
            single_result = {}

            single_result['title'] = each['name']
            single_result['url'] = each['external_urls']['spotify']
            single_result['creators'] = [singer['name'] for singer in each['artists']]
            single_result['image'] = each['images'][0]['url']
            single_result['medium'] = 'album'

            result.append(single_result)
            del single_result

    return result

def search_music(query):

    pool = ThreadPoolExecutor(max_workers=4)
    tracks = pool.submit(search_song, query).result()
    albums = pool.submit(search_album, query).result()

    main_result = tracks+albums

    if main_result:
        result_size = len(main_result)
    else:
        result_size = 1

    relevance_sort = difflib.get_close_matches(
        query, [x["title"] for x in main_result], n=result_size, cutoff=0
    )

    final = []
    added = []

    for rel_sorted in relevance_sort:
        for result in main_result:
            if (
                result["title"] == rel_sorted
                and len(final) < 10
                and rel_sorted not in added
            ):
                final.append(result)
                added.append(rel_sorted)
                break

    del relevance_sort
    del added

    return final