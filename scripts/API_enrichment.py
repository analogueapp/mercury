import requests
from bs4 import BeautifulSoup, SoupStrainer

def fetch_goodreads(isbn, current_data):
    url = 'https://www.goodreads.com/search/index.xml?q=%s&key=skZt3eIo68igzAikdSJkQ'%(isbn)
    soup_object = BeautifulSoup(requests.get(url).text, 'lxml', parse_only=SoupStrainer('work'))
    current_data['original_publication_year']  = soup_object.find('original_publication_year').get_text()
    current_data['original_publication_month'] =  soup_object.find('original_publication_month').get_text()
    current_data['original_publication_day'] = soup_object.find('original_publication_day').get_text()
    current_data['average_rating'] = soup_object.find('average_rating').get_text()
    current_data['author_name'] = soup_object.find('name').get_text()
    return current_data





