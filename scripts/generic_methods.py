import requests
from bs4 import BeautifulSoup, SoupStrainer

# getting Open graph tags data
def open_graph(request_object):
    graph_data = {}
    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")
    for meta in head_content:
        try:
            if "og:" in meta["property"]:
                graph_data[meta["property"][3:]] = meta["content"]
        except:
            continue
    return graph_data


def twitter_tags(request_object):
    data = {}
    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")
    for meta in head_content:
        try:
            if "twitter:" in meta["property"]:
                data[meta["property"][8:]] = meta["content"]
        except:
            continue
    return data


def main_generic(request_object):

    generic_data = open_graph(request_object)
    generic_data.update(twitter_tags(request_object))

    return generic_data

