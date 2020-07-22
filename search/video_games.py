import requests
from concurrent.futures import ThreadPoolExecutor
from constants import giantbomb_search_url, giantbomb_game_url
from dotenv import load_dotenv
import os

load_dotenv()

GIANTBOMB_KEY = os.getenv('GIANTBOMB_API_KEY')


def get_game(guid):
    get_response = {}

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }

    game_result = requests.get(
        f"{giantbomb_game_url}{guid}/?api_key={GIANTBOMB_KEY}&format=json", 
        headers = headers
    ).json()

    get_response['title'] = game_result['results']['name']
    get_response['image'] = game_result['results']['image']['original_url']
    get_response['url'] = game_result['results']['site_detail_url']

    if game_result['results']['developers'] is not None:
        get_response['creators'] = [dev['name'] for dev in game_result['results']['developers']]
    else:
        get_response['creators'] = []

    get_response['medium'] = 'video_game'

    return get_response
 

def search_video_games(query):
    results = []

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }

    game_results = requests.get(
        f"{giantbomb_search_url}{GIANTBOMB_KEY}&format=json&query={query}&resources=game", 
        headers = headers
    ).json()


    ids =  [each['id'] for each in game_results['results']]

    if ids:
        workers = len(ids)
    else:
        workers = 1

    with ThreadPoolExecutor(max_workers=workers) as executor:

        for each in executor.map(get_game, ids):
            results.append(each)
        
    return results