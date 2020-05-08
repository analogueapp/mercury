import requests
from bs4 import BeautifulSoup, SoupStrainer
import time
from constants import goodreads_key, goodreads_api_url
from typing import Dict


def title_check(title: str) -> str:
    if title[-1] == ")":
        title = title[::-1]
        return title[title.index("(") + 1:][::-1].strip()
    return title


def get_title(url: str) -> str:
    request_object = requests.get(url).text

    title_soup = BeautifulSoup(request_object, 'lxml', parse_only=SoupStrainer(
        'meta', attrs={'property': 'og:title'})).find('meta')
    title = title_soup['content']

    return title


def fetch_goodreads(url: str) -> Dict:
    api_data = {}

    title = get_title(url)
    title = title_check(title)

    api_url = (
        goodreads_api_url + title +"&key=" + goodreads_key
    )

    soup_object = BeautifulSoup(
        requests.get(api_url).text, "lxml", parse_only=SoupStrainer("work")
    )

    api_data["original_publication_year"] = soup_object.find(
        "original_publication_year"
    ).get_text()

    api_data["original_publication_month"] = soup_object.find(
        "original_publication_month"
    ).get_text()

    api_data["original_publication_day"] = soup_object.find(
        "original_publication_day"
    ).get_text()

    api_data["average_rating"] = soup_object.find("average_rating").get_text()

    api_data["author_name"] = soup_object.find("name").get_text()

    return api_data