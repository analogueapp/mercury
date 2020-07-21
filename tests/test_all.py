import pytest
import requests
import app
from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test
from utils.request import handle_params
from tests.test_case_output import test_get_handleparams_output, test_get_handleparams_sample, test_tag_parser_output, test_enrich_wikiart_artwork_output, test_enrich_imdb_tv_output, test_enrich_imdb_person_output, test_enrich_imdb_movie_output, test_enrich_goodreads_output, test_get_imdb_person_output, test_get_goodreads_output, test_get_wikiart_artwork_output, test_get_imdb_tv_output, test_get_imdb_movie_output, test_get_params_url_output, test_enrich_spotify_album_output, test_get_spotify_album_output, test_get_netflix_series_output, test_enrich_netflix_series_output, test_get_netflix_movie_output, test_enrich_netflix_movie_output, test_get_spotify_show_output, test_enrich_spotify_show_output, test_get_spotify_artist_output, test_enrich_spotify_artist_output, test_enrich_spotify_track_output, test_get_spotify_track_output, test_enrich_spotify_playlist_output, test_get_spotify_playlist_output, test_enrich_spotify_episode_output, test_get_spotify_episode_output

def test_tag_parsers():
    URL = 'https://www.youtube.com/watch?v=ab1H602yc_Y'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    assert 'Silicon Valley' in get_data['description']
    assert get_data['form'] == 'video'
    assert get_data['image'] is not None
    assert get_data['medium'] == 'video_link'
    assert 'Silicon Valley' in get_data['title']
    assert 'ab1H602yc_Y' in get_data['url']

def test_get_params_url():
    URL = 'https://www.creativelive.com/flash-sale?utm_source=creativeLIVE&utm_medium=email&utm_campaign=20171110_All_12For19FlashSale'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    assert 'photo' in get_data['description'] or 'video' in get_data['description']
    assert get_data['form'] == test_get_params_url_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_params_url_output['medium']
    assert 'Flash Sale' in get_data['title']
    assert get_data['url'] == test_get_params_url_output['url']

def test_getrich_imdb_movie():
    URL = 'https://www.imdb.com/title/tt0111161/?ref_=hm_fanfav_tt_9_pd_fp1'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert ('Morgan Freeman' in get_data['description']) or ('Frank Darabont' in get_data['description']) or ('redemption' in get_data['description'])
    assert get_data['form'] == test_get_imdb_movie_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_imdb_movie_output['medium']
    assert 'Shawshank Redemption' in get_data['title']
    assert get_data['url'] == test_get_imdb_movie_output['url']
    assert enriched_data['movie results']['title'] == test_enrich_imdb_movie_output

def test_getrich_imdb_tv():
    URL = 'https://www.imdb.com/title/tt0944947/'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert ('David Benioff' in get_data['description']) or ('D.B. Weiss' in get_data['description']) or ('Emilia Clarke' in get_data['description'])
    assert get_data['form'] == test_get_imdb_tv_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_imdb_tv_output['medium']
    assert 'Game of Thrones' in get_data['title']
    assert get_data['url'] == test_get_imdb_tv_output['url']
    assert enriched_data['tv_results']['name'] == test_enrich_imdb_tv_output

def test_getrich_imdb_person():
    URL = 'https://www.imdb.com/name/nm0634240/?ref_=nv_sr_srsg_0'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert ('Christopher Nolan' in get_data['description']) or ('London' in get_data['description']) or ('England' in get_data['description']) or ('storytelling' in get_data['description'])
    assert get_data['form'] == test_get_imdb_person_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_imdb_person_output['medium']
    assert 'Christopher Nolan' in get_data['title']
    assert get_data['url'] == test_get_imdb_person_output['url']
    assert enriched_data['person data']['name'] == test_enrich_imdb_person_output

def test_getrich_goodreads():
    URL = 'https://www.goodreads.com/book/show/78411.The_Bad_Beginning'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert ('three' in get_data['description']) or ('unpleasant' in get_data['description']) or ('Reader' in get_data['description'])
    assert get_data['form'] == test_get_goodreads_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_goodreads_output['medium']
    assert 'The Bad Beginning' in get_data['title']
    assert get_data['url'] == test_get_goodreads_output['url']
    assert enriched_data['author_name'] == test_enrich_goodreads_output

def test_getrich_wikiart_artwork():
    URL = 'https://www.wikiart.org/en/thomas-eakins/the-chess-player-1876'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data['description'] == test_get_wikiart_artwork_output['description']
    assert get_data['form'] == test_get_wikiart_artwork_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_wikiart_artwork_output['medium']
    assert get_data['title'] == test_get_wikiart_artwork_output['title']
    assert get_data['url'] == test_get_wikiart_artwork_output['url']
    assert len(enriched_data['data']) > 5
    assert enriched_data['paginationToken'] == test_enrich_wikiart_artwork_output['paginationToken']
    assert enriched_data['hasMore'] == test_enrich_wikiart_artwork_output['hasMore']

def test_get_handle_params():
    assert handle_params(test_get_handleparams_sample) == test_get_handleparams_output

def test_getrich_netflix_series():
    URL = 'https://www.netflix.com/title/70283264'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    # enriched_data = enrich_test(URL)
    assert ('nuclear apocalypse' in get_data['description']) or ('Earth' in get_data['description']) or ('100' in get_data['description'])
    assert get_data['form'] == test_get_netflix_series_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_netflix_series_output['medium']
    assert get_data['title'] == test_get_netflix_series_output['title']
    assert '70283264' in get_data['url']
    # assert enriched_data['title_details']['RESULT']['nfinfo']['title'] == test_enrich_netflix_series_output

def test_getrich_netflix_movie():
    URL = 'https://www.netflix.com/title/80178943'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    # enriched_data = enrich_test(URL)
    assert ('Boss Baby' in get_data['description']) or ('big brother' in get_data['description']) or ('Tim' in get_data['description'])
    assert get_data['form'] == test_get_netflix_movie_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_netflix_movie_output['medium']
    assert 'The Boss Baby' in get_data['title']
    assert '80178943' in get_data['url']
    # assert enriched_data['title_details']['RESULT']['nfinfo']['title'] == test_enrich_netflix_movie_output

def test_getrich_spotify_track():
    URL = 'https://open.spotify.com/track/1yvMUkIOTeUNtNWlWRgANS'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    track_id = enriched_data['track_details']['id']
    name = enriched_data['track_details']['name']
    content_type = enriched_data['track_details']['type']
    enriched_data.clear()
    enriched_data["id"] = track_id
    enriched_data["type"] = content_type
    enriched_data["name"] = name
    assert 'Unstoppable' in get_data['description']
    assert get_data['form'] == test_get_spotify_track_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_spotify_track_output['medium']
    assert get_data['title'] == test_get_spotify_track_output['title']
    assert get_data['url'] == test_get_spotify_track_output['url']
    assert enriched_data == test_enrich_spotify_track_output

def test_getrich_spotify_album():
    URL = 'https://open.spotify.com/album/6yIEe1y08bqC5LFEctRdTf'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert ('Een Klein Beetje Geluk' in get_data['description']) or ('Ali B' in get_data['description'])
    assert get_data['form'] == test_get_spotify_album_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_spotify_album_output['medium']
    assert 'Een Klein Beetje Geluk' in get_data['title']
    assert '6yIEe1y08bqC5LFEctRdTf' in get_data['url']
    assert enriched_data["album_details"]['id'] == test_enrich_spotify_album_output['id']
    assert enriched_data["album_details"]['name'] == test_enrich_spotify_album_output['name']
    assert enriched_data["album_details"]['release_date'] == test_enrich_spotify_album_output['release_date']

def test_getrich_spotify_show():
    URL = 'https://open.spotify.com/show/1JdkD0ZoZ52KjwdR0b1WoT'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    name = enriched_data['show_details']['name']
    media = enriched_data['show_details']['media_type']
    publisher = enriched_data['show_details']['publisher']
    content_type = enriched_data['show_details']['type']
    enriched_data.clear()
    enriched_data['name'] = name
    enriched_data['media_type'] = media
    enriched_data['publisher'] = publisher
    enriched_data['type'] = content_type
    assert ('Linear Digressions' in get_data['description']) or ('machine learning' in get_data['description'])
    assert get_data['form'] == test_get_spotify_show_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_spotify_show_output['medium']
    assert 'Linear Digressions' in get_data['title']
    assert '1JdkD0ZoZ52KjwdR0b1WoT' in get_data['url']
    assert enriched_data == test_enrich_spotify_show_output

def test_getrich_spotify_artist():
    URL = 'https://open.spotify.com/artist/5WUlDfRSoLAfcVSX1WnrxN'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    artist_id = enriched_data['artist_details']['id']
    name = enriched_data['artist_details']['name']
    content_type = enriched_data['artist_details']['type']
    enriched_data.clear()
    enriched_data['name'] = name
    enriched_data['id'] = artist_id
    enriched_data['type'] = content_type
    assert get_data['form'] == test_get_spotify_artist_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_spotify_artist_output['medium']
    assert 'Sia' in get_data['title']
    assert '5WUlDfRSoLAfcVSX1WnrxN' in get_data['url']
    assert enriched_data == test_enrich_spotify_artist_output

def test_getrich_spotify_playlist():
    URL = 'https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    name = enriched_data['playlist_details']['name']
    content_type = enriched_data['playlist_details']['type']
    description = enriched_data['playlist_details']['description']
    playlist_id = enriched_data['playlist_details']['id']
    enriched_data.clear()
    enriched_data["id"] = playlist_id
    enriched_data["type"] = content_type
    enriched_data["name"] = name
    desc2 = description
    assert get_data['form'] == test_get_spotify_playlist_output['form']
    assert get_data['image'] is not None
    assert get_data['medium'] == test_get_spotify_playlist_output['medium']
    assert 'Rock' in get_data['title']
    assert '37i9dQZF1DXcF6B6QPhFDv' in get_data['url']
    assert enriched_data == test_enrich_spotify_playlist_output
    assert 'Rock' in desc2

def test_getrich_spotify_episode():
    URL = 'https://open.spotify.com/episode/467Uq5ZG2VJtaE6EZwnWNO'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    name = enriched_data['episode_details']['name']
    content_type = enriched_data['episode_details']['type']
    description = enriched_data['episode_details']['description']
    playlist_id = enriched_data['episode_details']['id']
    enriched_data.clear()
    enriched_data["id"] = playlist_id
    enriched_data["type"] = content_type
    enriched_data["name"] = name
    enriched_data["description"] = description
    assert enriched_data == test_enrich_spotify_episode_output
    assert 'Andrew Schulz' in get_data['description']
    assert get_data['form'] == test_get_spotify_episode_output['form']
    assert get_data['image'] == test_get_spotify_episode_output['image']
    assert get_data['medium'] == test_get_spotify_episode_output['medium']
    assert 'The Last Dance' in get_data['title']
    assert '467Uq5ZG2VJtaE6EZwnWNO' in get_data['url']
