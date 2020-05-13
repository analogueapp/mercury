import requests
from typing import Dict
from constants import art_artwork_url


def find_type(url: str) -> str:
    url = url.split('/')
    if url[-3] == 'en':
        return 'artwork'


def get_artwork(url: str) -> Dict:
    artwork_term = url.split('/')[-1]

    if '--' in artwork_term:
        artwork_term = artwork_term.split('--')[0]

    else:
        artwork_term = '-'.join(artwork_term.split('-')[0:-1])
    
    return requests.get(art_artwork_url+artwork_term).json()


def fetch_wikiart(url: str) -> Dict:
    api_data = {}

    art_type = find_type(url)

    if art_type == 'artwork':
        api_data = get_artwork(url)

    return api_data
