import requests
from bs4 import BeautifulSoup, SoupStrainer
from fetch_spotify import spotify_get
from fetch_imdb import *
from fetch_goodreads import *

APIs = ["www.goodreads.com", "www.imdb.com", "open.spotify.com"]


def enrich_test(url):
    site_name = url.split("/")[2]

    enrich_data = {}

    if site_name in APIs:

        if site_name == "www.goodreads.com":
            enrich_data = fetch_goodreads(url)

        elif site_name == "www.imdb.com":
            enrich_data = fetch_imdb(url)

        elif site_name == "open.spotify.com":
            enrich_data = spotify_get(url)

    return enrich_data
