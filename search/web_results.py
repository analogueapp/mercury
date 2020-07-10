from search.google import get_google_links_and_titles
from typing import Dict

def search_web(query):
    result = get_google_links_and_titles(query)
    return result