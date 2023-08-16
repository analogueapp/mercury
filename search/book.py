import requests
from typing import Dict
from constants import google_api_url
from apis import google_books
import json
import os

google_key = os.getenv("GOOGLE_KEY")


def search_isbn(isbn: str) -> str:
    url = f"{google_api_url}?q=isbn:{isbn}&key={google_key}"
    resp = requests.get(url)
    data = resp.json()
    volume_url = data["items"][0]["selfLink"]

    return volume_url


def search_books(query):
    results = []
    api_url = f"{google_api_url}?q=intitle:{query}&key={google_key}"
    resp = requests.get(api_url)
    data = resp.json()

    items = data.get("items", [])    

    for result in items:                     
        enriched_result = google_books.parse_google(result)

        results.append(enriched_result)

    return results
