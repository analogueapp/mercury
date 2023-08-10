import re
import requests
from requests.sessions import should_bypass_proxies
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict
from apis.wikipedia import get_short_details, search_google
from constants import goodreads_author_url, goodreads_search_url
from PIL import Image
import os

goodreads_key = os.getenv("GOODREADS_KEY")


def parse_data_from_wiki(url: str) -> Dict:
    return get_short_details(url)


def parse_wiki_url(title: str) -> str:

    title = title + " book wikipedia"
    url = search_google(title)
    return url


def title_check(title: str) -> str:
    if title[-1] == ")":
        title = title[::-1]
        return title[title.index("(") + 1 :][::-1].strip()
    return title


def get_title(url: str) -> str:
    request_object = requests.get(url).text

    title_soup = BeautifulSoup(
        request_object,
        "lxml",
        parse_only=SoupStrainer("meta", attrs={"property": "og:title"}),
    ).find("meta")
    title = title_soup["content"]

    return title


def get_goodreads_isbn(goodreads_id: str) -> str:    
    isbn_data = {}
    book_url = f"{goodreads_search_url}?id={goodreads_id}&key={goodreads_key}"
    parse_only = ["isbn", "isbn13"]
    soup_object = BeautifulSoup(requests.get(book_url).text, "html.parser")

    isbn_data["isbn"] = soup_object.find("isbn").get_text(strip=True)
    isbn_data["isbn13"] = soup_object.find("isbn13").get_text(strip=True)

    return isbn_data


def enrich_author(goodreads_id):
    author_data = {}
    author_url = f"{goodreads_author_url}?id={goodreads_id}&key={goodreads_key}"
    author_soup = BeautifulSoup(requests.get(author_url).text, "html.parser")

    author_data["about"] = author_soup.find("about").get_text(strip=True)
    author_data["born_at"] = author_soup.find("born_at").get_text(strip=True)
    author_data["died_at"] = author_soup.find("died_at").get_text(strip=True)
    author_data["hometown"] = author_soup.find("hometown").get_text(strip=True)
    author_data["large_image_url"] = author_soup.find("large_image_url").get_text(strip=True)
    author_data["name"] = author_soup.find("name").get_text(strip=True)

    return author_data


def fetch_goodreads(url: str) -> Dict:
    api_data = {}
    # split by . or -
    # https://stackoverflow.com/a/4998688/13178719
    gid = re.split("\.|\-", url.split("show/", 1)[1])[0]
    book_url = f"{goodreads_search_url}?id={gid}&key={goodreads_key}"
    soup_object = BeautifulSoup(requests.get(book_url).text, "html.parser")

    authors_data = soup_object.find("authors")
    isbn = soup_object.find("isbn").get_text(strip=True)
    original_publication_year = soup_object.find("original_publication_year").get_text(strip=True)
    original_publication_month = soup_object.find(
        "original_publication_month"
    ).get_text(strip=True)
    original_publication_day = soup_object.find("original_publication_day").get_text(strip=True)
    publication_year = soup_object.find("publication_year").get_text(strip=True)
    publication_month = soup_object.find("publication_month").get_text(strip=True)
    publication_day = soup_object.find("publication_day").get_text(strip=True)

    api_data["asin"] = soup_object.find("asin").get_text(strip=True)
    api_data["authors"] = [enrich_author(id.text) for id in authors_data.find_all("id")]
    api_data["description"] = soup_object.find("description").get_text(strip=True)
    api_data["edition_information"] = soup_object.find("edition_information").get_text(strip=True)
    api_data["form"] = "text"
    api_data["goodreads_id"] = gid
    api_data["image_url"] = get_image_url(
        isbn, soup_object.find("image_url").get_text(strip=True)
    )
    api_data["isbn"] = isbn
    api_data["isbn13"] = soup_object.find("isbn13").get_text(strip=True)
    api_data["kindle_asin"] = soup_object.find("kindle_asin").get_text(strip=True)
    api_data["language"] = soup_object.find("language_code").get_text(strip=True)
    api_data["medium"] = "book"
    api_data["origin"] = "amazon.com"
    api_data["origin_url"] = f"https://www.amazon.com/dp/{isbn}"
    api_data[
        "original_publication_date"
    ] = f"{original_publication_year}/{original_publication_month}/{original_publication_day}"  if original_publication_year else ''
    api_data["popular_shelves"] = [
        shelf["name"] for shelf in soup_object.find_all("shelf")
    ]
    api_data["publisher"] = soup_object.find("publisher").get_text(strip=True)
    api_data[
        "publication_date"
    ] = f"{publication_year}/{publication_month}/{publication_day}" if publication_year else ''
    api_data["title"] = soup_object.find("title").get_text(strip=True)

    return api_data


def get_image_url(isbn, goodreads_image_url):
    image_url = f"http://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
    with Image.open(requests.get(image_url, stream=True).raw) as img:
        size = img.size
    if size == (1, 1):
        image_url = goodreads_image_url
    if "nophoto" in image_url:
        image_url = (
            "https://ik.imagekit.io/analogue/content_placeholder_1_85wLgUnbx.jpg"
        )

    return image_url

