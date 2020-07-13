from search.google import get_google_links_and_titles
from typing import Dict
import favicon
from concurrent.futures import ThreadPoolExecutor

def get_image(single_response: str) -> str:
    try:
        icon = favicon.get(single_response['url'])
        icon = icon[0].url
        return icon
    except Exception as e:
        return None

def search_web(query):
    result = get_google_links_and_titles(query)
    images = []
    
    with ThreadPoolExecutor(max_workers=len(result)) as executor:
        for image in executor.map(get_image, result):
            images.append(image)
    
    for image, response in zip(images, result):
        response['image'] = image
    
    return result