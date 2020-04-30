import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

#getting Open graph tags data
def open_graph(request_object):
    start= time.time()
    Graph_data = {}
    parse_only = SoupStrainer('meta')
    head_content = BeautifulSoup(request_object,'lxml', parse_only=parse_only).find_all('meta')
    for meta in head_content:
        try:
            Graph_data[meta['property'][3:]] = meta['content']
        except:
            continue
    end  = time.time()
    Graph_data['response_time'] = '%s seconds'%(round(end-start, 2))
    return Graph_data

# def simple_tags(request_object):
#     parse_only = SoupStrainer(['title',])
#     main_tags = BeautifulSoup(request_object, 'lxml',)