import requests
from bs4 import BeautifulSoup, SoupStrainer
import concurrent.futures
from typing import Dict
from constants import goodreads_api_url , goodreads_search_url
from utils.tag_parsers import main_generic
import os

goodreads_key = os.getenv('GOODREADS_KEY')

def search_enrich_book(idd):
    enrich_book = {}
    book_url = f"{goodreads_search_url}?id={idd}&key={goodreads_key}"
    print(book_url)
    parse_only = ['publication_year','publication_month','publication_day','publisher','language_code', 'description','average_rating']
    soup_object = BeautifulSoup(
        requests.get(book_url).text, "lxml", parse_only=SoupStrainer(parse_only)
    )

    # print(requests.get(book_url).text)
    publication_year = soup_object.find('publication_year').get_text()
    publication_month = soup_object.find('publication_month').get_text()
    publication_day = soup_object.find('publication_day').get_text()
    publisher = soup_object.find('publisher').get_text()
    language = soup_object.find('language_code').get_text()
    description = soup_object.find('description').get_text()

    enrich_book['publication_date'] = f"{publication_day} {publication_month} {publication_year}"
    enrich_book['publisher'] = publisher
    enrich_book['language'] = language
    enrich_book['description'] = description

    return enrich_book


def search_books(query):
    results = []
    api_url = goodreads_api_url + query +"&key=" + goodreads_key

    soup_object = BeautifulSoup(
        requests.get(api_url).text, "lxml", parse_only=SoupStrainer("results")
    )

    for result in soup_object.find_all("work"):
        single_result = {}

        single_result['id'] = result.find('best_book').find('id').get_text()
        single_result['title'] = result.find('best_book').find('title').get_text()
        single_result['image'] = result.find('best_book').find('image_url').get_text()
        single_result['author'] = result.find('best_book').find('author').find('name').get_text()
        single_result['url'] = f"https://www.goodreads.com/book/show/{single_result['id']}"
        single_result['medium'] = 'book'
        single_result['form'] = 'text'
        
    
        results.append(single_result)
        del single_result

    return results