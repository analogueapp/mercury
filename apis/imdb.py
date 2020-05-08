import requests
from bs4 import BeautifulSoup, SoupStrainer
from constants import movieDB_key, imdb_api_url
from typing import Dict

def fetch_imdb(url: str) -> Dict:
    api_data = {}

    external_id = url.split("/")[-2]
    internal_id = ""

    IMDB_data = requests.get(
        imdb_api_url + external_id, params={"api_key": movieDB_key, "external_source": "imdb_id"}
    ).json()

    if len(IMDB_data["movie_results"]) > 0:
        IMDB_data = IMDB_data["movie_results"][0]
        internal_id = IMDB_data["id"]

        url_movie = "http://api.themoviedb.org/3/movie/%s/videos" % (internal_id)
        Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer

    elif len(IMDB_data["tv_results"]) > 0:
        IMDB_data = IMDB_data["tv_results"][0]
        internal_id = IMDB_data["id"]

        url_tv = "http://api.themoviedb.org/3/tv/%s/videos" % (internal_id)

        Trailer = requests.get(url_tv, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer

    elif len(IMDB_data["person_results"]) > 0:
        IMDB_data = IMDB_data["person_results"][0]
        internal_id = IMDB_data["id"]

        url_person = "http://api.themoviedb.org/3/person/%s?api_key=d439c85fec54360684f9d222bddb2153" % (internal_id)
        person_data = requests.get(url_person, params={"api_key": movieDB_key,}).json()
        api_data["person data"] = person_data

    else:
        return api_data

    api_data.update(IMDB_data)
    return api_data
