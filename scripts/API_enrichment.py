import requests
from bs4 import BeautifulSoup, SoupStrainer
from fetch_spotify import spotify_get
from fetch_imdb import *
from fetch_goodreads import *

APIs = ["www.goodreads.com", "www.imdb.com", "open.spotify.com"]


def Enrich_test(url, current_data):
    site_name = url.split("/")[2]
    print(current_data)

    if site_name in APIs:

        if site_name == "www.goodreads.com":
            current_data = fetch_goodreads(current_data["title"], current_data)

        elif site_name == "www.imdb.com":
            current_data = fetch_imdb(current_data)

        elif site_name == "open.spotify.com":
            current_data = spotify_get(current_data)

    return current_data
