import re
import requests
import json
from typing import Dict
import os
from search.book import search_isbn
from constants import google_api_url

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


def get_google_isbn(google_id: str) -> str:    
    isbn_data = {}
    g_url = f'{google_api_url}/{google_id}?key={google_key}'
    resp = requests.get(g_url)    
    data = resp.json()["volumeInfo"]
    
    isbn_data["isbn10"] = data["industryIdentifiers"][0]["identifier"]
    isbn_data["isbn13"] = data["industryIdentifiers"][1]["identifier"]

    return isbn_data


def fetch_amazon(url: str) -> Dict:    
    isbn = url.split("/")[-1]
    volume_url = search_isbn(isbn)
    api_data = fetch_google(volume_url)    

    return api_data


def fetch_google(url: str) -> Dict:
    # get isbn from amazon url    
    api_data = {}
    gid = url.split("/")[-1]    
    g_url = f'{google_api_url}/{gid}?key={google_key}'
    resp = requests.get(g_url)
    metadata = resp.json()    
    data = metadata["volumeInfo"]

    if "description" in data:
        api_data["description"] = data["description"]
    api_data["canonicalVolumeLink"] = data["canonicalVolumeLink"]
    api_data["google_id"] = gid
    api_data["google_url"] = data["infoLink"]
    api_data["form"] = "text"
    api_data["image_url"] = data["imageLinks"]["extraLarge"] if "extraLarge" in data[
        "imageLinks"] else data["imageLinks"]["large"] if "large" in data[
            "imageLinks"] else data["imageLinks"]["medium"] if "medium" in data[
                "imageLinks"] else data["imageLinks"]["small"] if "small" in data[
                    "imageLinks"] else "https://ik.imagekit.io/analogue/content_placeholder_1_85wLgUnbx.jpg"
    api_data["isbn10"] = data["industryIdentifiers"][0]["identifier"]
    api_data["isbn13"] = data["industryIdentifiers"][1]["identifier"]
    api_data["language"] = data["language"]
    #api_data["medium"] = data["printType"]
    api_data["medium"] = "book"
    api_data["publisher"] = data["publisher"]
    api_data[
        "publication_date"
    ] = data["publishedDate"].replace('-', '/')
    api_data["title"] = data["title"]
    api_data["origin"] = "amazon.com"
    api_data["origin_url"] = f"https://www.amazon.com/dp/{api_data['isbn10']}"

    ol_url = f'http://openlibrary.org/api/volumes/brief/isbn/{api_data["isbn10"]}.json'    
    ol_resp = requests.get(ol_url).json()
    if ol_resp != []:
        ol_metadata = ol_resp["records"]
        ol_key = list(ol_metadata.keys())[0]
        ol_data = ol_metadata[ol_key]

        api_data["ol_work_id"] = ol_data["details"]["details"]["works"][0]["key"].split(
            "/")[-1]
        api_data["ol_edition_id"] = ol_data["details"]["details"]["key"].split(
            "/")[-1]
        api_data["authors"] = [enrich_author(author["url"]) for author in ol_data['data']['authors']] if 'authors' in ol_data['data'] else [
            search_author(name) for name in data["authors"]]        
    else:
        api_data["authors"] = [search_author(name) for name in data["authors"]]    

    return api_data
