from search.books import search_books, search_enrich_book
from search.movies import movie_search, enrich_movie
from search.music_podcasts import search_music, search_podcast
from search.web_results import search_web


def search(query, medium, medium_id):
    results = []
    if medium == 'book':
        if medium_id is None:
            results = search_books(query)
        else:
            results = search_enrich_book(medium_id)

    elif medium == 'movie':
        if medium_id is None:
            results = movie_search(query)
        else:
            results = enrich_movie(medium_id)

    elif medium == 'music':
        results = search_music(query)

    elif medium == 'podcast':
        results = search_podcast(query)
    
    elif medium == 'web':
        results = search_web(query)

    return results