import requests
from bs4 import BeautifulSoup, SoupStrainer
from constants import movieDB_key, imdb_api_url, wikipedia_url
from typing import Dict
from apis.wikipedia import get_short_details


def get_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)


def get_wiki_url(title: str) -> str:
    
    title = title.replace(" ", "_")
    return wikipedia_url+title


def fetch_imdb(url: str) -> Dict:
    api_data = {}

    external_id = url.split("/")[-2]
    internal_id = ""

    IMDB_data = requests.get(
        imdb_api_url + 'find/' + external_id, params={"api_key": movieDB_key, "external_source": "imdb_id"}
    ).json()

    if len(IMDB_data["movie_results"]) > 0:
        api_data['movie results'] = IMDB_data["movie_results"][0]
        internal_id = IMDB_data["movie_results"][0]['id']
        title = api_data['movie results']['title']

        url_movie = "%smovie/%s/videos" % (imdb_api_url,internal_id)
        Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        
        api_data["trailer"] = Trailer
        api_data.update(get_short_details(get_wiki_url(title)))

    elif len(IMDB_data["tv_results"]) > 0:
        api_data["tv_results"] = IMDB_data["tv_results"][0]
        internal_id = IMDB_data["tv_results"][0]["id"]
        title = api_data["tv_results"]['name']

        url_tv = "%stv/%s/videos" % (imdb_api_url,internal_id)

        Trailer = requests.get(url_tv, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer
        api_data.update(get_data_from_wiki(get_wiki_url(title)))

    elif len(IMDB_data["person_results"]) > 0:
        IMDB_data = IMDB_data["person_results"][0]
        internal_id = IMDB_data["id"]

        url_person = "%sperson/%s" % (imdb_api_url,internal_id)
        person_data = requests.get(url_person, params={"api_key": movieDB_key,}).json()
        api_data["person data"] = person_data
        api_data.update(get_short_details(get_wiki_url(person_data['name'])))

    else:
        return api_data

    
    return api_data
