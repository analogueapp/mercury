from search.book import search_books, search_enrich_book
from search.film_tv import search_film
from search.song_album import search_music
from search.podcast import search_podcast


def search(query, medium):
    
    if medium == 'book':
        results = search_books(query)

    elif medium == 'film':
        results = search_film(query)

    elif medium == 'music':
        results = search_music(query)

    elif medium == 'podcast':
        results = search_podcast(query)
    
    else: 
        results = {"error": "Search failed to load"}

    return results