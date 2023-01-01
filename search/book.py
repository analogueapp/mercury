import requests
from typing import Dict
from constants import google_api_url
import json
import os

google_key = os.getenv('GOOGLE_KEY')

def search_isbn(isbn: str) -> str:
    url = f'{google_api_url}?q=isbn:{isbn}&key={google_key}'
    resp = requests.get(url)
    data = resp.json()
    volume_url = data["items"][0]["selfLink"]

    return volume_url

def search_books(query):    
    results = []    
    api_url = f'{google_api_url}?q=intitle:{query}&key={google_key}'    
    resp = requests.get(api_url)
    data = resp.json()            

    for result in data["items"]:        
        single_result = {}        
        
        single_result['title'] = result["volumeInfo"]["title"]
        single_result['image'] = result["volumeInfo"]["imageLinks"]["thumbnail"]
        single_result['creators'] = result["volumeInfo"]["authors"]
        single_result['url'] = result["selfLink"]
        single_result['medium'] = 'book'

        results.append(single_result)
        del single_result
    
    return results