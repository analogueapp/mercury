import requests
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict
from apis.wikipedia import get_short_details
import os

movieDB_key = os.getenv("MOVIEDB_KEY")
imdb_api_url = os.getenv("IMDB_API_URL")
wikipedia_url = os.getenv("WIKIPEDIA_URL")

def parse_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)


def parse_wiki_url(title: str) -> str:
    
    title = title.replace(" ", "_")
    return wikipedia_url+title


def fetch_imdb(url: str) -> Dict:
    api_data = {}

    external_id = url.split("/")[-2]
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

        wiki_url = parse_wiki_url(title)
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

        wiki_url = parse_wiki_url(title)
        api_data['wiki data'] = parse_data_from_wiki(wiki_url)

    elif IMDB_data["person_results"]:
        IMDB_data = IMDB_data["person_results"][0]
        internal_id = IMDB_data["id"]

        url_person = "%sperson/%s" % (imdb_api_url,internal_id)
        person_data = requests.get(url_person, params={"api_key": movieDB_key,}).json()
        api_data["person data"] = person_data
        title = person_data['name']

        wiki_url = parse_wiki_url(title)
        api_data['wiki data'] = parse_data_from_wiki(wiki_url)

    else:
        return api_data

    
    return api_data
