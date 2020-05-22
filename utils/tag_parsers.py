import requests
import base64
import strgen
from bs4 import BeautifulSoup, SoupStrainer
from concurrent.futures import ThreadPoolExecutor
from utils.enrichment import get_url
from typing import Dict
import logging
from constants import apiflash_key, apiflash_url_to_image, api_imgbb_url, imgbb_key, fullUrlsExceptions


def capture_webpage(url: str) -> str:
    site_name = get_url(url)
    image_url = "%s?access_key=%s&url=%s" % (apiflash_url_to_image, apiflash_key, url)
    upload_url = api_imgbb_url + "key=" + imgbb_key
    image_name = strgen.StringGenerator("[\d\c]{10}").render()

    # saving temporarily on heroku
    try:
        img_data = requests.get(image_url).content

        with open("%s.jpg" % (image_name), "wb") as handler:
            handler.write(img_data)

        with open("%s.jpg" % (image_name), "rb") as img_file:
            base64_image = base64.b64encode(img_file.read())

        base64_image = base64_image.decode("utf-8")
        params = {"image": base64_image}
        imgb_api = requests.post(upload_url, data=params).json()

        return imgb_api["data"]["url"]
        
    except Exception as e:
        logging.error("Unable to take a screenshot due to %s" % (e))
        return "No image"


def medium_check(get_data, form_type) -> str:
    if get_data["form"] == "video":

        if "movie" in form_type or "film" in form_type:
            return "film"
        elif "tv_show" in form_type or "tv" in form_type:
            return "tv"
        elif "episode" in form_type:
            return "tv_episode"
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
        return "audio_link"


# getting Open graph tags data
def open_graph(tupl) -> dict:
    request_object = tupl[0]

    get_data = {
        "title": None,
        "url": None,
        "medium": None,
        "form": None,
        "image": None,
        "description": None,
    }

    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")

    for meta in head_content:

        if "og:" in str(meta) and 'property' in meta.attrs.keys():

            if meta["property"][3:] == "title":
                
                get_data["title"] = meta["content"]

            elif meta["property"][3:] == "description":
                get_data["description"] = meta["content"]

            elif meta["property"][3:] == "url":
                get_data["url"] = meta["content"]

            elif meta["property"][3:] == "image":
                get_data["image"] = meta["content"]

            elif meta["property"][3:] == "type":

                if "video" in meta["content"]:
                    get_data["form"] = "video"
                    get_data["medium"] = medium_check(get_data, meta["content"])

                elif "audio" in meta["content"] or "music" in meta["content"]:
                    get_data["form"] = "audio"
                    get_data["medium"] = medium_check(get_data, meta["content"])

                elif "book" in str(meta["content"]):
                    get_data["form"] = "text"
                    get_data["medium"] = "book"

                else:
                    get_data["form"] = "text"
                    get_data["medium"] = "link"

    return get_data


def twitter_tags(tupl):
    request_object = tupl[0]

    get_data = {
        "title": None,
        "url": None,
        "medium": None,
        "form": None,
        "image": None,
        "description": None,
    }

    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")

    for meta in head_content:

        if "twitter:" in str(meta) and 'property' in meta.attrs.keys():

            if meta["property"][9:] == "title":
                get_data["title"] = meta["content"]
        
            elif meta["property"][9:] == "description":
                get_data["description"] = meta["content"]

            elif meta["property"][3:] == "image":
                get_data["image"] = meta["content"]

        elif "twitter:" in str(meta) and 'name' in meta.attrs.keys():

            if meta["name"][8:] == "title":
                get_data["title"] = meta["content"]
        
            elif meta["name"][8:] == "description":
                get_data["description"] = meta["content"]

            elif meta["name"][8:] == "image":
                get_data["image"] = meta["content"]

    return get_data


def fallback(tupl):
    request_object, url = tupl[0], tupl[1]

    get_data = {
        "title": None,
        "url": None,
        "medium": None,
        "form": None,
        "image": None,
        "description": None,
    }

    parse_only = SoupStrainer(["title", "p"])
    content = BeautifulSoup(request_object, "lxml", parse_only=parse_only)

    try:
        title = content.find("title").get_text()
        get_data["title"] = title
    except Exception as e:
        logging.error(e)
        get_data["title"] = "No title available"

    try:
        description = content.find("p").get_text()
        get_data["description"] = description
    except Exception as e:
        logging.error(e)
        get_data["description"] = "No description available"

    get_data['url'] = url
    get_data["form"] = "text"
    get_data["medium"] = "link"

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

    pool = ThreadPoolExecutor(max_workers=2)

    get_data_og = pool.submit(open_graph,(request_object,))
    get_data_twitter = pool.submit(twitter_tags,(request_object,))
    get_data_fallback = pool.submit(fallback,(request_object, URL))
 
    get_data_og = get_data_og.result()
    get_data_twitter = get_data_twitter.result()
    get_data_fallback = get_data_fallback.result()

    get_keys = list(get_data.keys())
    get_keys.sort()
    get_keys = get_keys[::-1]

    for main_keys in get_keys:
        if get_data_og[main_keys] is None:

            if get_data_twitter[main_keys] is None:

                if main_keys == "image":
                    get_data["image"] = capture_webpage(get_data["url"])

                else:
                    get_data[main_keys] = get_data_fallback[main_keys]

            else:
                get_data[main_keys] = get_data_twitter[main_keys]
        else:
            get_data[main_keys] = get_data_og[main_keys]


    if get_url(URL) in fullUrlsExceptions:
        get_data["url"] = URL
    else:
        get_data["url"] = get_url(URL)
                
    return get_data