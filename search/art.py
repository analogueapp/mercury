import requests
from typing import Dict
from constants import wikiart_search_url, wikiart_painting_url
from concurrent.futures import ThreadPoolExecutor
import logging

def refine_wikiart_results(api_data: Dict) -> list:
    results = []

    if 'data' in api_data:
        for i in api_data['data']:
            response = {
                    "form": 'image',
                    "image": None,
                    "medium": "art",
                    "title": None,
                    "url": None,
                    'year': None,
                    'artist_url': None,
                    'id': None,
                    'creators': []
                }

            response['image'] = i['image']
            response['title'] = i['title']
            response['year'] = i['completitionYear']
            response['artist_url'] = i['artistUrl']
            response['id'] = i['id']
            response['creators'].append(i['artistName'])

            results.append(response)
    
    return results

def single_result(obj: Dict) -> Dict:
    target = wikiart_painting_url + obj['id']
    data = requests.get(target).json()

    obj['url'] = 'https://www.wikiart.org/en/' + obj['artist_url'] + '/' + data['url']
    obj.pop('artist_url', None)
    obj.pop('id', None)

    return obj

def refine_wikiart_more(api_data: Dict) -> list:
    result = []

    with ThreadPoolExecutor(max_workers=len(api_data)) as executor:
        for each in executor.map(single_result, api_data):
            if each is not None:
                result.append(each)

    return result

def search_art(query: str) -> Dict:

    target = wikiart_search_url + query
    api_data = requests.get(target).json()
    
    api_data = refine_wikiart_results(api_data)
    api_data_1 = refine_wikiart_more(api_data[:8])
    api_data_2 = []
    try:
        if len(api_data) >= 14:
            api_data_2 = refine_wikiart_more(api_data[8:14])

        elif len(api_data) > 8:
            api_data_2 = refine_wikiart_more(api_data[8:])
    
    except Exception as e:
        logging.error(e)
    
    api_data = api_data_1 + api_data_2

    return api_data