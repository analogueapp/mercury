import pytest
from search.film_tv import search_film, tv_search
from search.book import search_books
from search.song_album import search_music
from search.web_results import search_web
from search.youtube import search_video
from search.podcast import search_podcast
from search.video_games import search_video_games

def test_film():
    query = "batman"
    search_result = search_film(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5

def test_tv():
    query = "love"
    search_result = tv_search(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5

def test_book():
    query = "animal"
    search_result = search_books(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5

def test_music():
    query = "love"
    search_result = search_music(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5

def test_podcast():
    query = "daily"
    search_result = search_podcast(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5

def test_web():
    query = "climate"
    search_result = search_web(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 2

def test_youtube():
    query = "nature"
    search_result = search_video(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 6

def test_games():
    query = "far cry"
    search_result = search_video_games(query)
    assert isinstance(search_result, list)
    if len(search_result):
        assert isinstance(search_result[0], dict)
        assert len(list(search_result[0].keys())) == 5
