import requests
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict
from apis.wikipedia import get_short_details, search_google, WikiUrlTitle
from constants import imdb_api_url , wikipedia_url
import os

movieDB_key = os.getenv("MOVIEDB_KEY")

def parse_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)

def parse_wiki_url(title: str, category: str) -> str:
    
    if category == WikiUrlTitle.movie:
        title = title + ' movie wikipedia'
    
    elif category == WikiUrlTitle.tv:
        title = title + ' series wikipedia'
    
    url = search_google(title)
    
    return url

def parse_external_id(url: str) -> str:
    url = url.split('/')
    external_id = url.index('www.imdb.com') + 2
    return url[external_id]

def fetch_imdb(url: str) -> Dict:
    api_data = {}

    external_id = parse_external_id(url)
    internal_id = ""

    IMDB_data = requests.get(
        imdb_api_url + 'find/' + external_id, params={"api_key": movieDB_key, "external_source": "imdb_id"}
    ).json()

    if IMDB_data["movie_results"]:
        api_data['movie results'] = IMDB_data["movie_results"][0]
        internal_id = IMDB_data["movie_results"][0]['id']
        title = api_data['movie results']['title']

        url_movie = "%smovie/%s/videos" % (imdb_api_url,internal_id)
        Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        
        api_data["trailer"] = Trailer

        wiki_url = parse_wiki_url(title, WikiUrlTitle.movie)
        api_data['wiki data'] = parse_data_from_wiki(wiki_url)

    elif IMDB_data["tv_results"]:
        api_data["tv_results"] = IMDB_data["tv_results"][0]
        internal_id = IMDB_data["tv_results"][0]["id"]
        title = api_data["tv_results"]['name']

        url_tv = "%stv/%s/videos" % (imdb_api_url,internal_id)

        Trailer = requests.get(url_tv, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer
        
        wiki_url = parse_wiki_url(title, WikiUrlTitle.tv)
        api_data['wiki data'] = parse_data_from_wiki(wiki_url)

    elif IMDB_data["person_results"]:
        IMDB_data = IMDB_data["person_results"][0]
        internal_id = IMDB_data["id"]

        url_person = "%sperson/%s" % (imdb_api_url,internal_id)
        person_data = requests.get(url_person, params={"api_key": movieDB_key,}).json()
        api_data["person data"] = person_data
        title = person_data['name']
        
        wiki_url = parse_wiki_url(title, WikiUrlTitle.person)
        api_data['wiki data'] = parse_data_from_wiki(wiki_url)

    else:
        return api_data

    
    return api_data
