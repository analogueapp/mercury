import re
import requests
import json
from typing import Dict
import os
from search.book import search_isbn
from constants import google_api_url, google_image_url

google_key = os.getenv("GOOGLE_KEY")


def search_author(name: str) -> Dict:
    author_data = {}

    s_url = f'http://openlibrary.org/search/authors.json?q={"+".join(name.split(" "))}'
    s_resp = requests.get(s_url)
    s_data = s_resp.json()

    if s_data["numFound"] == 0:
        author_data["name"] = name
    else:
        olid = s_data["docs"][0]["key"]
        a_url = f'https://openlibrary.org/authors/{olid}.json'
        a_resp = requests.get(a_url)
        a_data = a_resp.json()        

        if "bio" in a_data:
            author_data["about"] = a_data["bio"]
        if "birth_date" in a_data:
            author_data["born_at"] = a_data["birth_date"]
        if "death_date" in a_data:
            author_data["died_at"] = a_data["death_date"]
        # might return Not Found
        author_data["large_image_url"] = f"https://covers.openlibrary.org/a/olid/{olid}-L.jpg"
        author_data["name"] = a_data["name"]

    return author_data


def enrich_author(a_url: str) -> Dict:
    author_data = {}
    url_params = a_url.split("/")
    url_params.pop()
    olid = url_params[-1]
    ol_url = f'{("/").join(url_params)}.json'
    resp = requests.get(ol_url)
    data = resp.json()
    if "bio" in data:
        author_data["about"] = data["bio"]
    if "birth_date" in data:
        author_data["born_at"] = data["birth_date"]
    if "death_date" in data:
        author_data["died_at"] = data["death_date"]
    author_data["large_image_url"] = f"https://covers.openlibrary.org/a/olid/{olid}-L.jpg"
    author_data["name"] = data["name"]

    return author_data


def fetch_amazon(url: str) -> Dict:    
    isbn = url.split("/")[-1]
    volume_url = search_isbn(isbn)
    api_data = fetch_google_ol(volume_url)    

    return api_data


def fetch_google(url: str) -> Dict:
    # get isbn from amazon url    
    api_data = {}
    gid = url.split("/")[-1]    
    g_url = f'{google_api_url}/{gid}?key={google_key}'
    resp = requests.get(g_url)
    metadata = resp.json()    
    data = metadata["volumeInfo"]    
    api_data["description"] = data["description"] if "description" in data else None
    api_data["canonicalVolumeLink"] = data["canonicalVolumeLink"]
    api_data["google_id"] = gid
    # api_data["google_url"] = data["infoLink"]
    api_data["google_url"] = g_url
    api_data["url"] = g_url
    api_data["form"] = "text"
    api_data["image_url"] = f'{google_image_url}/{gid}?fife=w400-h600&source=gbs_api' 
    if "industryIdentifiers" in data:
        for identifier in data["industryIdentifiers"]:
            if identifier["type"] == "ISBN_10":
                api_data["isbn"] = identifier["identifier"]
            elif identifier["type"] == "ISBN_13":
                api_data["isbn13"] = identifier["identifier"]
    api_data["language"] = data["language"]
    #api_data["medium"] = data["printType"]
    api_data["medium"] = "book"
    api_data["publisher"] = data["publisher"]
    api_data[
        "publication_date"
    ] = data["publishedDate"].replace('-', '/') if "publishedDate" in data else None
    api_data["title"] = data["title"]
    api_data["origin"] = "amazon.com"
    api_data["origin_url"] = f"https://www.amazon.com/dp/{api_data['isbn']}" if "isbn" in api_data else g_url
    api_data["authors"] = [{'name': author} for author in data['authors']] if "authors" in data else []
        
    return api_data    

def fetch_authors(isbn: str) -> Dict:
    ol_url = f'http://openlibrary.org/api/volumes/brief/isbn/{isbn}.json'
    ol_resp = requests.get(ol_url).json()
    if ol_resp != []:
        ol_metadata = ol_resp["records"]
        ol_key = list(ol_metadata.keys())[0]
        ol_data = ol_metadata[ol_key]
        authors = [enrich_author(author["url"]) for author in ol_data['data']['authors']] if 'authors' in ol_data['data'] else []
    else:
        authors = []

    return authors

def fetch_google_ol(url: str) -> Dict:
    api_data = fetch_google(url)
    api_data["authors"] = fetch_authors(api_data["isbn"]) if "isbn" in api_data else api_data["authors"]
    return api_data