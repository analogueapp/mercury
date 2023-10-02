import requests
from urllib.parse import quote
from typing import Dict
from apis.creators import get_creator_bio

def enrich_author(name, a_key: str, work) -> Dict:
    author_data = {}    
    ol_url =  f"https://openlibrary.org/authors/{a_key}.json"
    data = requests.get(ol_url).json()   
    img_url = f"https://covers.openlibrary.org/a/olid/{a_key}-L.jpg"    

    author_data["name"] = data.get("name", None)
    author_data["alternate_names"] = data.get("alternate_names", None)     

    # Check if the name is not equal to author_data["name"] or not in "alternate_names"
    if name != author_data["name"] and (not author_data["alternate_names"] or name not in author_data["alternate_names"]):
        return get_creator_bio(name, work)

    author_data["born_at"] = data.get("birth_date", None)
    author_data["died_at"] = data.get("death_date", None)

    author_data[
        "large_image_url"
    ] = img_url if is_image_url(img_url) else None

    if isinstance(data.get("bio"), dict):
        author_data["about"] = data["bio"].get("value", None)
    else:
        author_data["about"] = data.get("bio", None)

    if len(author_data["about"]) < 100:
        author_data["about"] = get_creator_bio(author_data["name"], work)["about"]

    return author_data


def fetch_author(name: str, work: str) -> Dict:   
    name_param = quote(name)
    ol_url = f"https://openlibrary.org/search/authors.json?q={name_param}"
    ol_resp = requests.get(ol_url).json()    
    if ol_resp and ol_resp['numFound'] > 0:                
        author_key = ol_resp['docs'][0]['key']
        return enrich_author(name, author_key, work)
    else:
        return None

def is_image_url(url):
    try:
        response = requests.get(url, stream=True)
        # Ensure we don't download the entire image, just get headers
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        return content_type.startswith('image/')
    except requests.RequestException:
        return False