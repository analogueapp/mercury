from mediawiki import MediaWiki
from typing import Dict

def get_title(url: str) -> str:
    title = url.split('/')[-1]
    title = " ".join(title.split('_'))
    return title

def fetch_wikidata(title: str) -> Dict:
    api_data = {}

    wikipedia = MediaWiki()
    page_data = wikipedia.page(title)
    
    api_data['title'] = page_data.title
    api_data['summary'] = page_data.summary
    api_data['images'] = page_data.images
    api_data['categories'] = page_data.categories

    return api_data

def fetch_wikipedia(url: str) -> Dict:
    title = get_title(url)
    return fetch_wikidata(title)