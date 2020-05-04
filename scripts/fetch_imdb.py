import requests
from bs4 import BeautifulSoup, SoupStrainer

MovieDB_Key = "d439c85fec54360684f9d222bddb2153"

#TODO: add profile and other categories
def fetch_imdb(url):
    api_data = {}

    external_id = url.split("/")[-2]
    internal_id = ""

    api_url = "https://api.themoviedb.org/3/find/"

    IMDB_data = requests.get(
        api_url + external_id, params={"api_key": MovieDB_Key, "external_source": "imdb_id"}
    ).json()

    if IMDB_data["tv_results"] == [] and len(IMDB_data["movie_results"]) != 0:
        IMDB_data = IMDB_data["movie_results"][0]
        internal_id = IMDB_data["id"]

        url_movie = "http://api.themoviedb.org/3/movie/%s/videos" % (internal_id)
        Trailer = requests.get(url_movie, params={"api_key": MovieDB_Key,}).json()[
            "results"
        ][0]

    elif IMDB_data["movie_results"] == [] and len(IMDB_data["tv_results"]) != 0:
        IMDB_data = IMDB_data["tv_results"][0]
        internal_id = IMDB_data["id"]

        url_tv = "http://api.themoviedb.org/3/tv/%s/videos" % (internal_id)
        Trailer = requests.get(url_tv, params={"api_key": MovieDB_Key,}).json()[
            "results"
        ][0]

    for data in IMDB_data.keys():
        api_data[data] = IMDB_data[data]

    api_data["trailer"] = Trailer

    return api_data
