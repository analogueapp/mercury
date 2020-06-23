import urllib
from bs4 import BeautifulSoup, SoupStrainer
import requests
import logging
from typing import Dict


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
    
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        requested = requests.get(URL, headers=headers, timeout=10)

        if requested.status_code != 200:
            return {"error": "URL failed to load"}
        return requested.text

    except Exception as e:
        logging.error(f"Error loading page: {e}")
        return {"error": "URL failed to load"}
