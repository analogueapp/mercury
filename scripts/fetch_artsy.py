import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

Name = 'Analogue'
client_id = '77e9422bdf38d3bc0179'
client_secret = '7eec7ad1ebb0b01272ae4eec0e71170a'
starting_url = 'https://api.artsy.net/api'


def fetch_artsy(url):
    #authentication
    artsy_id = url.split('/')[-1]
    artsy_type = url.split('/')[-2]
    # print(artsy_type, artsy_id)

    api_data = {}
    auth_url = '/tokens/xapp_token'
    payload = {"client_id" : '77e9422bdf38d3bc0179',
    "client_secret" : '7eec7ad1ebb0b01272ae4eec0e71170a'}
    auth = requests.post(starting_url+auth_url, data=payload).json()
    # token = auth['token']
    
    payload = {'X-Xapp-Token' : auth['token'], 'Content-Type': 'application/json', "client_id" : '77e9422bdf38d3bc0179',
    "client_secret" : '7eec7ad1ebb0b01272ae4eec0e71170a'}
    # newreq = requests.post(starting_url+auth_url, data=payload).json()
    # print(newreq)

    if artsy_type == 'artists': #
        pass
    elif artsy_type == 'artworks': #
        pass
    elif artsy_type == 'collections': #
        pass
    elif artsy_type == 'images':
        pass
    elif artsy_type == 'profiles':
        pass
    elif artsy_type == 'sale_artworks':
        pass
    elif artsy_type == 'sales':
        pass
    elif artsy_type == 'search': #
        pass
    elif artsy_type == 'shows': #
        pass
    else:
        return api_data
    return api_data