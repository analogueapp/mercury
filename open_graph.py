import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

def request_and_filter(url):
    start= time.time()
    Graph_data = {}
    parseonly = SoupStrainer('meta')
    head_content = BeautifulSoup(requests.get(url).text,'lxml', parse_only=parseonly).find_all('meta')
    for meta in head_content:
        try:
            Graph_data[meta['property'][3:]] = meta['content']
        except:
            continue
    end  = time.time()
    Graph_data['response_time'] = '%s seconds'%(end-start)
    return Graph_data
