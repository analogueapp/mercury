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
        if "og:" in str(meta):
            graph_data[meta["property"]] = meta["content"]

    return graph_data


def twitter_tags(request_object):
    twitter_data = {}

    parse_only = SoupStrainer("meta")
    head_content = BeautifulSoup(
        request_object, "lxml", parse_only=parse_only
    ).find_all("meta")

    for meta in head_content:

        if "twitter:" in str(meta):
            try:
                twitter_data[meta["name"]] = meta["content"]
            except:
                twitter_data[meta["property"]] = meta["content"]

    return twitter_data


def main_generic(request_object):

    generic_data = open_graph(request_object)
    generic_data.update(twitter_tags(request_object))

    return generic_data
