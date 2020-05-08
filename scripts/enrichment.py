import requests
from bs4 import BeautifulSoup, SoupStrainer
from fetch_spotify import spotify_get
from fetch_imdb import *
from fetch_goodreads import *
from fetch_artsy import *

APIs = ["www.goodreads.com", "www.imdb.com", "open.spotify.com", "www.artsy.net"]


def enrich_test(url):
    site_name = url.split("/")[2]
    print(site_name)
    enrich_data = {}

    if site_name in APIs:

        if site_name == "www.goodreads.com":
            enrich_data = fetch_goodreads(url)

        elif site_name == "www.imdb.com":
            enrich_data = fetch_imdb(url)

        elif site_name == "open.spotify.com":
            enrich_data = spotify_get(url)

        elif site_name == "www.artsy.net":
            enrich_data = fetch_artsy(url)

    return enrich_data