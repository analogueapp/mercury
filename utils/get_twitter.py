from typing import Dict
from urllib.parse import urlparse
import os
import tweepy

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET_KEY")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def parse_id(url: str) -> str:
    parse_url = urlparse(url)
    twitter_id = parse_url.path.split('/')[-1]
    return twitter_id

def get_description(status: Dict) -> str:
    return status['full_text']

def get_user_image(status: Dict) -> str:
    
    if 'user' in status:
        if 'profile_image_url_https' in status['user']:
            image = status['user']['profile_image_url_https']
    
        elif 'profile_image_url' in status['user']:
            image = status['user']['profile_image_url']
    
        elif 'profile_banner_url' in status['user']:
            image = status['user']['profile_banner_url']
    
        else:
            return None
    
    try:
        image = image.replace('_normal', '')
    except Exception as e:
        image = image[:63] + image[70:]
    
    return image


def get_image(status: Dict) -> str:
    if 'entities' in status.keys():
        if 'media' in status['entities']:
            
            if 'media_url_https' in status['entities']['media'][0]:
                return status['entities']['media'][0]['media_url_https']
            
            if 'media_url' in status['entities']['media'][0]:
                return status['entities']['media'][0]['media_url']

    return get_user_image(status)

def get_title(status: Dict) -> str:
    if 'user' in status:
        
        if 'screen_name' in status['user']:
            return status['user']['screen_name'] + ' on Twitter'
        
        if 'name' in status['user']:
            return status['user']['name'] + ' on Twitter'
    
    return 'Someone on Twitter'

def get_twitter(url: str) -> Dict:
    desired_response = {
        "description": None,
        "form": 'text',
        "image": None,
        "medium": 'link',
        "title": None,
        "url": None
    }
    
    twitter_id = parse_id(url)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    status = api.get_status(twitter_id, tweet_mode = 'extended')._json
    
    desired_response['description'] = get_description(status)
    desired_response['image'] = get_image(status)
    desired_response['title'] = get_title(status)
    desired_response['url'] = url
    
    return desired_response