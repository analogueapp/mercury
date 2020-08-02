import requests
from typing import Dict
from constants import facebook_srape_API_URL
from utils.tag_parsers import medium_check
import os

FACEBOOK_API_KEY = os.getenv("FACEBOOK_API_KEY")

def get_facebook_API(url : str) -> dict:
    fb_scraper_response = requests.post(
        f"{facebook_srape_API_URL}id={url}&access_token={FACEBOOK_API_KEY}"
    ).json()

    print(fb_scraper_response)
    get_data = {}

    try:
        get_data['url'] = fb_scraper_response['url']
    except Exception as e:
        get_data['url'] = None

    try:
        get_data['title'] = fb_scraper_response['title']
    except Exception as e:
        get_data['title'] = None
    
    try:
        get_data['description'] = fb_scraper_response['description']
    except Exception as e:
        get_data['description'] = None

    try:
        if fb_scraper_response['image']:
            get_data['image'] = fb_scraper_response['image'][0]['url']
    except Exception as e:
        get_data['image'] = None


    try:
        if "video" in fb_scraper_response["type"]:
            get_data["form"] = "video"
            get_data["medium"] = medium_check(get_data, fb_scraper_response["type"])

        elif "audio" in fb_scraper_response["type"] or "music" in fb_scraper_response["type"]:
            get_data["form"] = "audio"
            get_data["medium"] = medium_check(get_data, fb_scraper_response["type"])

        elif "book" in fb_scraper_response["type"]:
            get_data["form"] = "text"
            get_data["medium"] = "book"

        else:
            get_data["form"] = "text"
            get_data["medium"] = "link"
    except Exception as e:
        get_data["form"] = None
        get_data["medium"] = None

    return get_data