from apiclient.discovery import build
import os
from typing import Dict
from constants import youtube_watch_url
from urllib.parse import urlparse


youtube_api_key = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def parse_category(url: str) -> str:
    category = None

    if 'watch' in url:
        category = 'video'
    elif 'channel' in url:
        category = 'channel'
    else:
        category = 'video'
    
    return category


def parse_id(url: str, category: str) -> str:
    yt_id = ''

    parsed = urlparse(url)

    if category == 'video':
        if parsed.query:
            yt_id = parsed.query.split('?')[0]
            yt_id = yt_id[2:]
        else:
            yt_id = parsed.path[1:]
    
    elif category == 'channel':
        yt_id = parsed.path.split('/')[2]
    
    elif category == 'playlist':
        yt_id = parsed.query.split('?')[0]
        yt_id = yt_id[5:]
    
    return yt_id


def clean_response(response):
    result = {}

    if 'video' in response['items'][0]['kind'] and response['items'][0]['id']:
        result['url'] = 'https://www.youtube.com/watch?v=' + response['items'][0]['id']

    response = response['items'][0]['snippet']

    result['title'] = response['title']
    result['description'] = response['description']

    if 'maxres' in response['thumbnails']:
        result['image'] = response['thumbnails']['maxres']['url']

    elif 'standard' in response['thumbnails']:
        result['image'] = response['thumbnails']['standard']['url']
    
    elif 'high' in response['thumbnails']:
        result['image'] = response['thumbnails']['high']['url']
    
    elif 'medium' in response['thumbnails']:
        result['image'] = response['thumbnails']['medium']['url']
    
    elif 'default' in response['thumbnails']:
        result['image'] = response['thumbnails']['default']['url']
    
    return result


def get_video(yt_id: str) -> Dict:
    try:
        req = youtube.videos().list(
            part="snippet",
            id=yt_id
        )
        response = req.execute()
    except Exception as e:
        return {}
    print(response)
    result = clean_response(response)
    return result


def get_channel(yt_id: str) -> Dict:
    try:
        req = youtube.channels().list(
                part="snippet",
                id=yt_id
            )
        response = req.execute()
    except Exception as e:
        return {}

    result = clean_response(response)
    return result
    

def get_youtube(url: str) -> Dict:

    response = {
        "description": None,
        "form": None,
        "image": None,
        "medium": None,
        "title": None,
        "url": url
    }
    
    category = parse_category(url)
    yt_id = parse_id(url, category)

    if category == 'video':
        response['form'] = 'video'
        response['medium'] = 'video_link'
        video_response = get_video(yt_id)
        response.update(video_response)

    elif category == 'channel':
        response['form'] = 'text'
        response['medium'] = 'link'
        channel_response = get_channel(yt_id)
        response.update(channel_response)

    else:
        response['form'] = 'text'
        response['medium'] = 'link'
    
    return response
