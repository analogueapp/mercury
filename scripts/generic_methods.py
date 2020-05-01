import requests
from bs4 import BeautifulSoup, SoupStrainer

#getting Open graph tags data
def open_graph(request_object):
    Graph_data = {}
    parse_only = SoupStrainer('meta')
    head_content = BeautifulSoup(request_object,'lxml', parse_only=parse_only).find_all('meta')
    for meta in head_content:
        try:
            if 'og:' in meta['property']:
                Graph_data[meta['property'][3:]] = meta['content']
        except:
            continue
    return Graph_data