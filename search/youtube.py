from apiclient.discovery import build
import os
from typing import Dict
from constants import youtube_watch_url

youtube_api_key = os.getenv("YOUTUBE_KEY")

def parse_response(api_response):
    desired = {
        'title': None,
        'description': None,
        'url': None,
        'medium': 'video_link',
        'image': None,
        'creators': None
    }

    desired['title'] = api_response['snippet']['title']
    desired['description'] = api_response['snippet']['description']

    if 'high' in api_response['snippet']['thumbnails']:
        desired['image'] = api_response['snippet']['thumbnails']['high']['url']
    elif 'medium' in api_response['snippet']['thumbnails']:
        desired['image'] = api_response['snippet']['thumbnails']['medium']['url']
    elif 'default' in api_response['snippet']['thumbnails']:
        desired['image'] = api_response['snippet']['thumbnails']['default']['url']
    
    desired['creators'] = api_response['snippet']['channelTitle']
    desired['url'] = youtube_watch_url + api_response['id']['videoId']
    
    return desired

def search_video(query: str) -> Dict:
    result = []

    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    
    req = youtube.search().list(q=query, part='snippet', type='video', maxResults=10)
    response = req.execute()
    response = response['items']

    for single_response in response:
        result.append(parse_response(single_response))

    return result