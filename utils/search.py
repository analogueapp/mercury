from search.book import search_books
from search.film_tv import search_film
from search.song_album import search_music
from search.podcast import search_podcast
from search.youtube import search_video
from search.web_results import search_web
from search.art import search_art
from search.video_games import search_video_games


def search(query, medium):
    results = []
    
    if medium == 'book':
        results = search_books(query)

    elif medium == 'film':
        results = search_film(query)

    elif medium == 'music':
        results = search_music(query)

    elif medium == 'podcast':
        results = search_podcast(query)

    elif medium == 'link':
        results = search_web(query)

    elif medium == 'video':
        results = search_video(query)
    
    elif medium == 'art':
        results = search_art(query)

    elif medium == 'video_game':
        results = search_video_games(query)
    
    else: 
        results = {"error": "Search failed to load"}

    return results