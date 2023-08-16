import urllib
from bs4 import BeautifulSoup, SoupStrainer
import requests
import logging
from typing import Dict
import http.cookiejar as cj
from utils.get_twitter import get_twitter
from utils.get_youtube import get_youtube

def handle_params(param_dict: dict) -> str:
    values = list(param_dict.values())
    keys = list(param_dict.keys())
    URL = ""

    for v, k in zip(values, keys):
        URL += f"{k}={v}&"

    URL = URL[4:-1]

    return URL


def send_request(param_dict: dict):

    URL = handle_params(param_dict)
    
    if 'http' not in URL:
        URL = "https://"+URL
    
    print(f"sending request to this URL: {URL}")

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        cookie = cj.CookieJar()
        if 'twitter.com' in URL:
            return get_twitter(URL)
        requested = requests.get(URL, headers=headers, cookies=cookie, timeout=10)

        print(f"Status code: {requested.status_code}")
        print(f"Request Type: {type(requested)}")
        
        if requested.status_code != 200:
            if 'youtube' in URL or 'youtu.be' in URL:
                return get_youtube(URL)
            return {"error": "URL failed to load"}
        return requested.text

    except Exception as e:
        logging.error(f"Error loading page: {e}")
        return {"error": "URL failed to load"}
