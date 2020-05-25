from mediawiki import MediaWiki
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict
from constants import wikipedia_api_url
import requests
from concurrent.futures import ThreadPoolExecutor


def retrieve_short_description(data: str) -> str:

    if 'wikibase-shortdesc' in data.keys():
        return data['wikibase-shortdesc']

    for _, value in list(data.items()):
        if isinstance(value, dict):
            return retrieve_short_description(value)


def get_short_description(title: str) -> Dict:

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


def check_braces(val: str) -> str:

    if val.count('(') != val.count(')'):
        val = val.replace('(', '')
        val = val.replace(')', '')
    
    return val


def clean(val: str) -> str:
    
    val = val.strip()
    val = val.strip('.')
    val = val.lstrip(')')
    val = val.rstrip('(')
    val = val.strip()
    val = val.strip('.')
    return val


def get_box_data(item):

    item = str(item)
    ans = []
    item = item.replace('</a>', '')

    while item != '':
        try:
            start = item.index('>')
            stop = item.index('<')

            if stop-start > 1:
                val = item[start+1:stop]
                val = check_braces(val)
                val = clean(val)
                
                if '\xa0' in val:
                    val = val.replace('\xa0', ' ')
                
                if ('[' in val and ']' in val):
                    val = ''
                
                if val != '':
                    ans.append(val)
                
            item = item[stop+1:]

        except:
            break

    return ans


def get_short_details(url: str) -> Dict:

    request_object = requests.get(url).text

    API_data = {}
    parse_only = SoupStrainer("tbody")

    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
        ).find("tbody")

    for i in head_content:
        processed = get_box_data(i)

        if len(processed) > 1:
            API_data[processed[0]] = processed[1:]

    return API_data


def get_title(url: str) -> str:

    title = url.split('/')[-1]
    title = " ".join(title.split('_'))

    return title


def fetch_wikidata(title: str) -> Dict:

    api_data = {}

    wikipedia = MediaWiki()
    
    page_data = wikipedia.page(title)

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

    api_data.update(api_data_wiki.result())
    api_data.update(api_data_short_data.result())
    api_data.update(api_data_short_details.result())

    return api_data