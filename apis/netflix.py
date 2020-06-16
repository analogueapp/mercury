import requests
from constants import netflix_url, netflix_query
from typing import Dict
from concurrent.futures import ThreadPoolExecutor
import os

rapidapi_host = os.getenv("RAPID_API_HOST")
rapidapi_key = os.getenv("RAPID_API_KEY")

def parse_netflix_id(url: str) -> str:
    
    netflix_id = ''

    for i in range(len(url)-7):
        if url[i:i+9].isnumeric():
            netflix_id = url[i:i+9]
            break
    
    return netflix_id


def get_title_details(id: str) -> Dict:

    netflix_query['t'] = 'loadvideo'
    netflix_query['q'] = id

    headers = {
        'x-rapidapi-host': rapidapi_host,
        'x-rapidapi-key': rapidapi_key
        }
    
    try:
        response = requests.request(
            "GET", netflix_url, headers=headers, params=netflix_query
            ).json()
    
    except Exception as e:
        return {}

    return response


def get_images(id: str) -> Dict:
    
    netflix_query['t'] = 'images'
    netflix_query['q'] = id

    headers = {
        'x-rapidapi-host': rapidapi_host,
        'x-rapidapi-key': rapidapi_key
        }
    
    try:
        response = requests.request(
            "GET", netflix_url, headers=headers, params=netflix_query
            ).json()

    except Exception as e:
        return {}

    return response


def fetch_netflix(url: str) -> Dict:

    netflix_id = parse_netflix_id(url)
    api_data = {}

    pool = ThreadPoolExecutor(max_workers=3)

    title_details = pool.submit(get_title_details,netflix_id)
    images = pool.submit(get_images,netflix_id)
    
    api_data['title_details'] = title_details.result()
    api_data['images'] = images.result()
    
    return api_data