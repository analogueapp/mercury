import requests
from bs4 import BeautifulSoup, SoupStrainer
from utils.enrichment import get_url
from typing import Dict
import logging

def none_check(object):
    for item in object.keys():
        if object[item] is None:
            return True
    return False

def medium_check(get_data, form_type) -> str:
    if get_data["form"] == "video":

        if "movie" in form_type or "film" in form_type:
            return "film"
        elif "tv_show" in form_type or "tv" in form_type:
            return "tv"
        elif "episode" in form_type:
            return "tv_episode"
        else:
            return "video_link"

    elif get_data["form"] == "audio":

        if "song" in form_type:
            return "song"
        elif "album" in form_type:
            return "album"
        elif "playlist" in form_type:
            return "playlist"
        elif "show" in get_data["url"]:
            return "show"
        elif "episode" in get_data["url"]:
            return "episode"
        else:
            return "audio_link"


# getting Open graph tags data
def open_graph(request_object, get_data) -> dict:

    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")

    for meta in head_content:
        
        if "og:" in str(meta):

            if meta["property"][3:] == "title":
                get_data["title"] = meta["content"]

            elif meta["property"][3:] == "description":
                get_data["description"] = meta["content"]

            elif meta["property"][3:] == "url" :
                get_data["url"] = meta["content"]

            elif meta["property"][3:] == "image":
                get_data["image"] = meta["content"]

            elif meta["property"][3:] == "type":

                if "video" in str(meta["content"]):
                    get_data["form"] = "video"
                    get_data["medium"] = medium_check(get_data, meta["content"])

                elif "audio" in str(meta["content"]) or "music" in str(meta["content"]):
                    get_data["form"] = "audio"
                    get_data["medium"] = medium_check(get_data, meta["content"])

                elif "book" in str(meta["content"]):
                    get_data["form"] = "text"
                    get_data["medium"] = "book"

                else:
                    get_data["form"] = "text"
                    get_data["medium"] = "link"

    return get_data


def twitter_tags(request_object, get_data):

    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")

    for meta in head_content:

        if "twitter:" in str(meta):

            if get_data["title"] is None:
                if meta["property"][9:] == "title":
                    get_data["title"] = meta["content"]
                continue

            if get_data["description"] is None:
                if (
                    meta["property"][9:20] == "description"
                    and len(meta["property"]) == 20
                ):
                    get_data["description"] = meta["content"]
                continue

            if get_data["image"] is None:
                if meta["property"][3:8] == "image" and len(meta["property"]) == 8:
                    get_data["image"] = meta["content"]
                continue

    return get_data


def fallback(request_object, get_data):

    parse_only = SoupStrainer(["title", "image", "p"])
    content = BeautifulSoup(request_object, "lxml", parse_only=parse_only)

    if get_data["title"] is None:
        try:
            title = content.find("title").get_text()
            get_data["title"] = title
        except Exception as e:
            logging.error(e)
            get_data["title"] = 'No title available'
            
    if get_data["description"] is None:
        try:
            description = content.find("p").get_text()
            get_data["description"] = description
        except Exception as e:
            logging.error(e)
            get_data["description"] = 'No description available'

    if get_data['image'] is None:
        try:
            image = content.find("img")['src']
            get_data['image'] = image
        except Exception as e:
            logging.error(e)
            get_data['image'] = 'No image available'

    if get_data['form'] is None:
        get_data['form'] = 'text'

    if get_data['medium'] is None:
        get_data['medium'] = 'link'
        
    return get_data


def main_generic(request_object, URL) -> dict:

    get_data = {
        "title": None,
        "url": None,
        "medium": None,
        "form": None,
        "image": None,
        "description": None,
    }

    get_data = open_graph(request_object, get_data)

    if none_check(get_data):
        get_data = twitter_tags(request_object, get_data)
    if none_check(get_data):
        get_data = fallback(request_object, get_data)

    get_data["url"] = get_url(URL) #using the link with params as an identifier

    return get_data
