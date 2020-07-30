import requests
from concurrent.futures import ThreadPoolExecutor
import difflib
from typing import Dict
import logging
from constants import (
    imdb_search_movie_url,
    imdb_poster_url,
    imdb_enrich_movie_url,
    imdb_api_url,
    imdb_enrich_tv_url,
    imdb_search_tv_url,
    imdb_external_id_url,
)
import os

movieDB_key = os.getenv("MOVIEDB_KEY")


def film_single_result(idd):
    url = f"{imdb_enrich_movie_url}/{idd}?api_key={movieDB_key}&language=en-US"
    movie_result = requests.get(url).json()

    try:
        movie_data = {}
        movie_data["title"] = movie_result["title"]
        movie_data["image"] = imdb_poster_url + movie_result["poster_path"]
        movie_data["medium"] = "film"
        movie_data["url"] = "https://www.imdb.com/title/" + movie_result["imdb_id"]
        movie_data["creators"] = [
            production["name"] for production in movie_result["production_companies"]
        ]
        movie_data['published_at'] = movie_result['release_date']
        return movie_data

    except Exception as e:
        logging.error(e)
        return None


def movie_search(query):
    result = []
    imdb_url = f"{imdb_search_movie_url}api_key={movieDB_key}&query={query}&page=1"

    search_data = requests.get(imdb_url).json()
    result_ids = []

    if 'results' in list(search_data.keys()):
        for movie_result in search_data["results"]:
            result_ids.append(movie_result["id"])

        if result_ids:
            workers = len(result_ids)
        else:
            workers = 1

        with ThreadPoolExecutor(max_workers=workers) as executor:

            for each in executor.map(film_single_result, result_ids):
                if each is not None:
                    result.append(each)

    return result


def enrich_movie(internal_id):
    url = f"{imdb_enrich_movie_url}/{internal_id}?api_key={movieDB_key}&language=en-US"
    movie_result = requests.get(url).json()

    movie_data = {}
    movie_data["title"] = movie_result["title"]
    movie_data["tagline"] = movie_result["tagline"]
    movie_data["status"] = movie_result["status"]
    movie_data["release_date"] = movie_result["release_date"]
    movie_data["vote_average"] = movie_result["vote_average"]
    movie_data["productions"] = [
        c["name"] for c in movie_result["production_companies"]
    ]
    movie_data["runtime"] = movie_result["runtime"]
    movie_data["genres"] = [genre["name"] for genre in movie_result["genres"]]
    movie_data["poster_path"] = imdb_poster_url + movie_result["poster_path"]
    movie_data["official_website"] = movie_result["homepage"]
    movie_data["overview"] = movie_result["overview"]
    movie_data["imdb_link"] = "https://www.imdb.com/title/" + movie_result["imdb_id"]

    url_movie = "%smovie/%s/videos" % (imdb_api_url, internal_id)
    Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
        "results"
    ][0]

    movie_data["trailer"] = "https://www.youtube.com/watch?v=" + Trailer["key"]

    return movie_data


def tv_single_result(idd):
    url = f"{imdb_enrich_tv_url}/{idd}?api_key={movieDB_key}&language=en-US"
    get_id = (
        f"{imdb_external_id_url}{idd}/external_ids?api_key={movieDB_key}&language=en-US"
    )
    tv_result = requests.get(url).json()
    imdb_id = requests.get(get_id).json()["imdb_id"]
    try:
        tv_data = {}
        tv_data["title"] = tv_result["name"]
        tv_data["image"] = imdb_poster_url + tv_result["poster_path"]
        tv_data["medium"] = "tv"
        tv_data["url"] = "https://www.imdb.com/title/" + imdb_id
        tv_data["creators"] = [creator["name"] for creator in tv_result["created_by"]]
        tv_data['published_at'] = tv_result['first_air_date']
        return tv_data

    except Exception as e:
        logging.error(e)
        return None


def tv_search(query):
    result = []
    imdb_url = f"{imdb_search_tv_url}api_key={movieDB_key}&query={query}&page=1"

    search_data = requests.get(imdb_url).json()
    result_ids = []

    if "results" in list(search_data.keys()):
        for tv_result in search_data["results"]:
            result_ids.append(tv_result["id"])

        if result_ids:
            workers = len(result_ids)
        else:
            workers = 1

        with ThreadPoolExecutor(max_workers=workers) as executor:

            for each in executor.map(tv_single_result, result_ids):
                if each is not None:
                    result.append(each)

    return result


def search_film(query):

    pool = ThreadPoolExecutor(max_workers=2)
    movie_result = pool.submit(movie_search, query)
    tv_result = pool.submit(tv_search, query)

    movie_result = movie_result.result()
    tv_result = tv_result.result()

    main_result = tv_result+movie_result

    if main_result:
        result_size = len(main_result)
    else:
        result_size = 1

    relevance_sort = difflib.get_close_matches(
        query, [x["title"] for x in main_result], n=result_size, cutoff=0.4
    )
    final = []
    added = []

    for rel_sorted in relevance_sort:
        for result in main_result:
            if (
                result["title"] == rel_sorted
                and len(final) < 10
                and rel_sorted not in added
            ):
                final.append(result)
                added.append(rel_sorted)
                break
                
    del relevance_sort
    del added

    return final
