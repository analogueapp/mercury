import pytest
import requests
import app
from utils.tag_parsers import main_generic
from utils.enrichment import enrich_test
from utils.request import handle_params
from tests.test_case_output import test_get_handleparams_output, test_get_handleparams_sample, test_tag_parser_output, test_get_without_og_twitter_output, test_enrich_wikiart_artwork_output, test_enrich_imdb_tv_output, test_enrich_imdb_person_output, test_enrich_imdb_movie_output, test_enrich_goodreads_output, test_get_imdb_person_output, test_get_goodreads_output, test_get_wikiart_artwork_output, test_get_imdb_tv_output, test_get_imdb_movie_output, test_get_params_url_output, test_enrich_spotify_album_output, test_get_spotify_album_output, test_get_netflix_series_output, test_enrich_netflix_series_output, test_get_netflix_movie_output, test_enrich_netflix_movie_output


def test_tag_parsers():
    URL = 'https://www.youtube.com/watch?v=ab1H602yc_Y'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    assert get_data == test_tag_parser_output

def test_get_without_og_twitter():
    URL = 'https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    get_data['image'] = get_data['image'][:17] #hosting service generates a new url for every request
    assert get_data == test_get_without_og_twitter_output
    
def test_get_params_url():
    URL = 'https://www.creativelive.com/flash-sale?utm_source=creativeLIVE&utm_medium=email&utm_campaign=20171110_All_12For19FlashSale'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    assert get_data == test_get_params_url_output

def test_getrich_imdb_movie():
    URL = 'https://www.imdb.com/title/tt0111161/?ref_=hm_fanfav_tt_9_pd_fp1'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data == test_get_imdb_movie_output
    assert enriched_data['movie results']['title'] == test_enrich_imdb_movie_output

def test_getrich_imdb_tv():
    URL = 'https://www.imdb.com/title/tt0944947/'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data == test_get_imdb_tv_output
    assert enriched_data['tv_results']['name'] == test_enrich_imdb_tv_output

def test_getrich_imdb_person():
    URL = 'https://www.imdb.com/name/nm0634240/?ref_=nv_sr_srsg_0'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data == test_get_imdb_person_output
    assert enriched_data['person data']['name'] == test_enrich_imdb_person_output

def test_getrich_goodreads():
    URL = 'https://www.goodreads.com/book/show/78411.The_Bad_Beginning'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data == test_get_goodreads_output
    assert enriched_data['author_name'] == test_enrich_goodreads_output

def test_getrich_wikiart_artwork():
    URL = 'https://www.wikiart.org/en/thomas-eakins/the-chess-player-1876'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert get_data == test_get_wikiart_artwork_output
    assert enriched_data == test_enrich_wikiart_artwork_output

def test_get_handle_params():
    assert handle_params(test_get_handleparams_sample) == test_get_handleparams_output

def test_getrich_spotify_album():
    URL = 'https://open.spotify.com/album/6yIEe1y08bqC5LFEctRdTf'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    enriched_data = enrich_test(URL)
    assert enriched_data == test_enrich_spotify_album_output
    assert get_data == test_get_spotify_album_output

def test_getrich_netflix_series():
    URL = 'https://www.netflix.com/title/70283264'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    image1 = get_data.pop('image', None)
    enriched_data = enrich_test(URL)
    assert image1 is not None
    assert get_data == test_get_netflix_series_output
    assert enriched_data == test_enrich_netflix_series_output

def test_getrich_netflix_movie():
    URL = 'https://www.netflix.com/title/80178943'
    requested = requests.get(URL).text
    get_data = main_generic(requested, URL)
    image1 = get_data.pop('image', None)
    enriched_data = enrich_test(URL)
    assert image1 is not None
    assert get_data == test_get_netflix_movie_output
    assert enriched_data == test_enrich_netflix_movie_output
