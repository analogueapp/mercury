import requests
from typing import Dict
import os
from search.book import search_isbn
from constants import google_api_url, google_image_url
from dotenv import load_dotenv

load_dotenv()

google_key = os.getenv("GOOGLE_KEY")


def search_author(name: str) -> Dict:
    author_data = {}

    s_url = f'http://openlibrary.org/search/authors.json?q={"+".join(name.split(" "))}'
    s_resp = requests.get(s_url)
    s_data = s_resp.json()

    olid = s_data.get("docs", [{}])[0].get("key", None)
    if olid:
        a_url = f"https://openlibrary.org/authors/{olid}.json"
        a_resp = requests.get(a_url)
        a_data = a_resp.json()

        author_data["about"] = a_data.get("bio", None)
        author_data["born_at"] = a_data.get("birth_date", None)
        author_data["died_at"] = a_data.get("death_date", None)
        author_data[
            "large_image_url"
        ] = f"https://covers.openlibrary.org/a/olid/{olid}-L.jpg"
        author_data["name"] = a_data.get("name", name)
    else:
        author_data["name"] = name

    return author_data


def enrich_author(a_url: str) -> Dict:
    author_data = {}
    url_params = a_url.split("/")
    url_params.pop()
    olid = url_params[-1]
    ol_url = f'{("/").join(url_params)}.json'
    resp = requests.get(ol_url)
    data = resp.json()

    author_data["about"] = data.get("bio", None)
    author_data["born_at"] = data.get("birth_date", None)
    author_data["died_at"] = data.get("death_date", None)
    author_data[
        "large_image_url"
    ] = f"https://covers.openlibrary.org/a/olid/{olid}-L.jpg"
    author_data["name"] = data.get("name", None)

    return author_data


def fetch_amazon(url: str) -> Dict:
    isbn = url.split("/")[-1]
    volume_url = search_isbn(isbn)
    api_data = fetch_google(volume_url)

    return api_data


def parse_google(result: Dict) -> Dict:
    api_data = {}
    data = result.get("volumeInfo", {})

    api_data["description"] = data.get("description", None)
    api_data["canonicalVolumeLink"] = data.get("canonicalVolumeLink", None)
    api_data["google_id"] = result.get("id", None)
    api_data["google_url"] = data.get("infoLink", None)
    api_data["url"] = result.get("selfLink", None)
    api_data["form"] = "text"
    api_data[
        "image_url"
    ] = f'{google_image_url}/{result.get("id", None)}?fife=w400-h600&source=gbs_api'
    api_data["language"] = data.get("language", None)
    api_data["medium"] = "book"
    api_data["publisher"] = data.get("publisher", None)
    api_data["publication_date"] = data.get("publishedDate", "").replace("-", "/")
    api_data["title"] = data.get("title", None)
    api_data["origin"] = "amazon.com"
    api_data["authors"] = [{"name": author} for author in data.get("authors", [])]
    api_data["topics"] = data.get("categories", [])

    for identifier in data.get("industryIdentifiers", []):
        if identifier.get("type") == "ISBN_10":
            api_data["isbn"] = identifier.get("identifier", None)
        elif identifier.get("type") == "ISBN_13":
            api_data["isbn13"] = identifier.get("identifier", None)

    api_data["origin_url"] = (
        f"https://www.amazon.com/dp/{api_data['isbn']}"
        if "isbn" in api_data
        else api_data.get("google_url", None)
    )

    return api_data


def fetch_google(url: str) -> Dict:
    gid = url.split("/")[-1]
    g_url = f"{google_api_url}/{gid}?key={google_key}"
    resp = requests.get(g_url)
    result = resp.json()
    parsed_data = parse_google(result)

    return parsed_data


def fetch_authors(isbn: str) -> Dict:
    ol_url = f"http://openlibrary.org/api/volumes/brief/isbn/{isbn}.json"
    ol_resp = requests.get(ol_url).json()
    if ol_resp:
        ol_metadata = ol_resp.get("records", {})
        ol_key = list(ol_metadata.keys())[0]
        ol_data = ol_metadata.get(ol_key, {})
        authors = [
            enrich_author(author.get("url", ""))
            for author in ol_data.get("data", {}).get("authors", [])
        ]
    else:
        authors = []

    return authors
