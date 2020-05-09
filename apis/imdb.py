import requests
from bs4 import BeautifulSoup, SoupStrainer
from constants import movieDB_key, imdb_api_url
from typing import Dict

def fetch_imdb(url: str) -> Dict:
    api_data = {}

    external_id = url.split("/")[-2]
    internal_id = ""

    IMDB_data = requests.get(
        imdb_api_url + 'find/' + external_id, params={"api_key": movieDB_key, "external_source": "imdb_id"}
    ).json()

    if len(IMDB_data["movie_results"]) > 0:
        IMDB_data = IMDB_data["movie_results"][0]
        internal_id = IMDB_data["id"]

        url_movie = "%smovie/%s/videos" % (imdb_api_url,internal_id)
        Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer

    elif len(IMDB_data["tv_results"]) > 0:
        IMDB_data = IMDB_data["tv_results"][0]
        internal_id = IMDB_data["id"]

        url_tv = "%stv/%s/videos" % (imdb_api_url,internal_id)

        Trailer = requests.get(url_tv, params={"api_key": movieDB_key,}).json()[
            "results"
        ][0]
        api_data["trailer"] = Trailer

    elif len(IMDB_data["person_results"]) > 0:
        IMDB_data = IMDB_data["person_results"][0]
        internal_id = IMDB_data["id"]

        url_person = "%sperson/%s" % (imdb_api_url,internal_id)
        person_data = requests.get(url_person, params={"api_key": movieDB_key,}).json()
        api_data["person data"] = person_data

    else:
        return api_data

    api_data.update(IMDB_data)
    return api_data
