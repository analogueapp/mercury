import requests
from typing import Dict
from constants import imdb_seach_url, imdb_poster_url, imdb_enrich_movie_url, imdb_api_url
import os

movieDB_key = os.getenv("MOVIEDB_KEY")

def movie_search(query):
    result = []
    imdb_url = f"{imdb_seach_url}api_key={movieDB_key}&query={query}&page=1"

    search_data = requests.get(imdb_url).json()

    for movie_result in search_data['results']:
        single_movie = {}
        single_movie['title'] = movie_result['title']
        single_movie['description'] = movie_result['overview']
        single_movie['vote_average'] = movie_result['vote_average']
        single_movie['release_date'] = movie_result['release_date']
        single_movie['original_language'] = movie_result['original_language']
        single_movie['id'] = movie_result['id']
        single_movie['medium'] = 'movie'


        if movie_result['poster_path'] is not None:
            single_movie['image'] = imdb_poster_url+movie_result['poster_path']
        else:
            movie_result['poster_path'] = "No image available"

        result.append(single_movie)
        del single_movie

    return result

def enrich_movie(internal_id):
    url = f"{imdb_enrich_movie_url}/{internal_id}?api_key={movieDB_key}&language=en-US"
    movie_result = requests.get(url).json()

    movie_data = {}
    movie_data['title'] = movie_result['title']
    movie_data['tagline'] = movie_result['tagline']
    movie_data['status'] = movie_result['status']
    movie_data['release_date'] = movie_result['release_date']
    movie_data['vote_average'] = movie_result['vote_average']
    movie_data['productions'] = [c['name'] for c in movie_result['production_companies']]
    movie_data['runtime'] = movie_result['runtime']
    movie_data['genres'] = [genre['name'] for genre in movie_result['genres']]
    movie_data['poster_path'] = imdb_poster_url+movie_result['poster_path']
    movie_data['official_website'] = movie_result['homepage']
    movie_data['overview'] = movie_result['overview']
    movie_data['imdb_link'] = 'https://www.imdb.com/title/'+movie_result['imdb_id']

    url_movie = "%smovie/%s/videos" % (imdb_api_url,internal_id)
    Trailer = requests.get(url_movie, params={"api_key": movieDB_key,}).json()[
        "results"
    ][0]

    movie_data['trailer'] = 'https://www.youtube.com/watch?v='+Trailer['key']


    return movie_data 
