import requests
from bs4 import BeautifulSoup, SoupStrainer

APIs =['www.goodreads.com','www.imdb.com']

def fetch_goodreads(isbn, current_data):
    url = 'https://www.goodreads.com/search/index.xml?q=%s&key=skZt3eIo68igzAikdSJkQ'%(isbn)
    soup_object = BeautifulSoup(requests.get(url).text, 'lxml', parse_only=SoupStrainer('work'))
    current_data['original_publication_year']  = soup_object.find('original_publication_year').get_text()
    current_data['original_publication_month'] =  soup_object.find('original_publication_month').get_text()
    current_data['original_publication_day'] = soup_object.find('original_publication_day').get_text()
    current_data['average_rating'] = soup_object.find('average_rating').get_text()
    current_data['author_name'] = soup_object.find('name').get_text()
    return current_data

def fetch_imdb(current_data):
    
    url_movie = 'http://api.themoviedb.org/3/movie/%s/videos?api_key=d439c85fec54360684f9d222bddb2153'%(current_data['url'].split('/')[-2])
    # url_tv_show = 
    del current_data['description']

    current_data['title'] = current_data['title'].split(' (')[0]
    title = '+'.join(current_data['title'].split(' '))
    url = 'http://www.omdbapi.com/?apikey=4318c4eb&t=%s&plot=full'%(title)
    API_data = requests.get(url).json()
    #TODO: IMDB trailers are remaining. 
    #TODO: Create a CLass for enrichment
    #TODO: FInd a proper way
    for key in API_data.keys():
        current_data[key] = API_data[key]
    API_data = requests.get(url_movie).json()

    current_data['trailer'] = API_data['results'][0]

    return current_data

def Enrich_test(url, current_data):
    site_name = url.split('/')[2]
    if site_name in APIs:
        if site_name == 'www.goodreads.com':
            current_data =  (fetch_goodreads(current_data["title"], current_data))
        elif site_name == 'www.imdb.com':
            current_data = fetch_imdb(current_data)

    return current_data
        
    


