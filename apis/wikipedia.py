from mediawiki import MediaWiki
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict
import requests
from concurrent.futures import ThreadPoolExecutor
from constants import wikipedia_api_url
import os
from googlesearch import search
from enum import Enum


class WikiUrlTitle(Enum):
    movie = 1
    tv = 2
    person = 3
    artist = 4
    show = 5
    track = 6


def search_google(search_param: str) -> str:
    response = search(search_param, stop=6)
    
    for url in response:
        if 'wikipedia' in url:
            return url


def retrieve_short_description(data: str) -> str:

    if 'wikibase-shortdesc' in data.keys():
        return data['wikibase-shortdesc']

    for value in list(data.values()):
        if isinstance(value, dict):
            return retrieve_short_description(value)


def get_short_description(title: str) -> Dict:
    try:
        api_data = {}

        PARAMS = {
        "action": "query",
        "titles": title,
        "prop": "pageprops",
        "format": "json"
        }

        DATA = requests.get(url=wikipedia_api_url, params=PARAMS).json()
        api_data['short description'] = retrieve_short_description(DATA)

        return api_data
    
    except Exception as e:
        return {'message': '[wikipedia] error getting short description'}


def find_value(row):
    value = row.find('td')
    if value:
        return value.text
    return None

def clean_value(value):
    value = value.replace('\xa0', ' ')
    value = value.split('\n')
    
    while '' in value:
        value.remove('')
    
    if len(value) == 1:
        return value[0]

    return value
    
def find_key(row):
    key = row.find('th')
    if key:
        return key.text
    return None


def get_short_details(url: str) -> Dict:
    request_object = requests.get(url).text
    
    API_data = {}
    parse_only = SoupStrainer("tbody")
    
    boxes = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
        ).findAll("tbody")[:3]

    data = []

    for row in boxes:
        data = data + row.find_all("tr")

    for row in data:
        key = find_key(row)
        value = find_value(row)
        
        if key and value:
            value = clean_value(value)
            API_data[key] = value
    
    return API_data


def get_title(url: str) -> str:

    title = url.split('/')[-1]
    title = " ".join(title.split('_'))

    return title


def fetch_wikidata(title: str) -> Dict:

    api_data = {}
    wikipedia = MediaWiki()

    try:
        page_data = wikipedia.page(title)
    except Exception as e:
        return {'message': '[wikipedia] error getting wikidata'}

    pool = ThreadPoolExecutor(max_workers=6)

    poster = pool.submit(lambda :page_data.logos)
    content = pool.submit(lambda :page_data.sections)
    categories = pool.submit(lambda :page_data.categories)
    images = pool.submit(lambda :page_data.images)
    summary = pool.submit(lambda :page_data.summary)
    title_ = pool.submit(lambda :page_data.title)

    api_data['poster'] = poster.result()
    api_data['contents'] = content.result()
    api_data['categories'] = categories.result()
    api_data['images'] = images.result()
    api_data['summary'] = summary.result()
    api_data['title'] = title_.result()
    
    return api_data


def fetch_wikipedia(url: str) -> Dict:
    api_data = {}

    title = get_title(url)

    pool = ThreadPoolExecutor(max_workers=3)

    api_data_wiki = pool.submit(fetch_wikidata,title)
    api_data_short_data =  pool.submit(get_short_description,title)
    api_data_short_details = pool.submit(get_short_details,url)

    api_data['wikidata API'] = api_data_wiki.result()
    api_data['short description'] = api_data_short_data.result()
    api_data['box details'] = api_data_short_details.result()

    return api_data