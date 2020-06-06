import requests
from typing import Dict
import logging
from constants import artsy_api_url
import os

artsy_client_id = os.getenv("ARTSY_CLIENT_ID")
artsy_client_skey = os.getenv("ARTSY_CLIENT_SKEY")


def fetch_artsy(url: str) -> Dict:
    artsy_id = url.split('/')[-1]
    artsy_type = url.split('/')[-2]

    api_data = {}

    #authentication
    auth_url = '/tokens/xapp_token'
    payload = {"client_id" : artsy_client_id,
    "client_secret" : artsy_client_skey}
    auth = requests.post(artsy_api_url+auth_url, data=payload).json() #getting token

    headers = {
        'accept': 'application/json',
        'X-Xapp-Token': auth['token']
    }

    if artsy_type == 'artist':
        target = artsy_api_url+'/artists/'+artsy_id
        api_data = requests.get(target, headers=headers).json()

        try:
            api_data.update(requests.get(api_data['_links']['artworks']['href'], headers=headers).json())
        except Exception as e:
            logging.error(e)

    elif artsy_type == 'artwork':
        target = artsy_api_url + '/artworks/' + artsy_id
        api_data = requests.get(target, headers = headers).json()

        try:
            api_data.update(requests.get(api_data['_links']['artists']['href'], headers=headers).json())
        except Exception as e:
            logging.error(e)

    elif artsy_type == 'show':
        artsy_id = artsy_id.split('?')[0]
        target = artsy_api_url+'/shows/'+artsy_id
        api_data = requests.get(target, headers = headers).json()

        try:
            api_data.update(requests.get(api_data['_links']['images']['href'], headers=headers).json())
        except Exception as e:
            logging.error(e)

    elif artsy_type == 'www.artsy.net': #profile
        target = artsy_api_url+'/profiles/'+artsy_id
        api_data = requests.get(target, headers = headers).json()

    else:
        return api_data

    return api_data