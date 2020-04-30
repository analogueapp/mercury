import requests
from bs4 import BeautifulSoup, SoupStrainer

class OpenGraph:

    def __init__(self, url):
        self.url = url
        self.tags = ['']

    def get_data(self):
