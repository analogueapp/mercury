from typing import Dict
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer
from constants import twitter_api_url

def parse_id(url: str) -> str:
    parse_url = urlparse(url)
    twitter_id = parse_url.path.split('/')[-1]
    return twitter_id

def get_twitter(url: str) -> Dict:
    desired_response = {
        "description": None,#
        "form": 'text',#
        "image": None,
        "medium": 'link',#
        "title": None,#
        "url": None#
    }
    twitter_id = parse_id(url)

    api_url = twitter_api_url + twitter_id
    api_response = requests.get(api_url).json()

    desired_response['title'] = api_response['author_name'] + ' on Twitter'
    desired_response['url'] = api_response['url']
    html = str(api_response['html'].encode('ascii', 'ignore'))[2:-1]
    html = html.replace('\\n', '')
    html = html.replace('\\', '')
    bsoup = BeautifulSoup(html, 'lxml', parse_only=SoupStrainer("p")).find('p')
    desired_response['description'] = bsoup.text

    return desired_response