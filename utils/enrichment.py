import requests
from bs4 import BeautifulSoup, SoupStrainer
from apis.spotify import spotify_get
from apis.imdb import fetch_imdb
from apis.goodreads import fetch_goodreads
from apis.artsy import fetch_artsy
from apis.wikiart import fetch_wikiart
from apis.wikipedia import fetch_wikipedia
from typing import Dict
from constants import APIs
import os


def get_url(url: str) -> str:
    url = url.split('/')

    if 'http' in url[0]:
        site_name = url[2]
    else:
        site_name = url[0]

    return site_name

def enrich_test(url: str) -> Dict:
    site_name = get_url(url)
    enrich_data = {}

    if site_name in APIs:

        if site_name in ("www.goodreads.com","goodreads.com"):
            enrich_data = fetch_goodreads(url)

        elif site_name in ("www.imdb.com","imdb.com"):
            enrich_data = fetch_imdb(url)

        elif site_name == "open.spotify.com":
            enrich_data = spotify_get(url)

        elif site_name in ("www.artsy.net","artsy.net"):
            enrich_data = fetch_artsy(url)

        elif site_name in ("www.wikiart.org","wikiart.org"):
            enrich_data = fetch_wikiart(url)

        elif site_name == "en.wikipedia.org":
            enrich_data = fetch_wikipedia(url)

    return enrich_data
