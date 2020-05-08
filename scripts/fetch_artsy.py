import requests


def fetch_artsy(url):

    client_id = '77e9422bdf38d3bc0179'
    client_secret = '7eec7ad1ebb0b01272ae4eec0e71170a'
    starting_url = 'https://api.artsy.net/api'    
    
    
    artsy_id = url.split('/')[-1]
    artsy_type = url.split('/')[-2]
    
    api_data = {}
    #authentication
    auth_url = '/tokens/xapp_token'
    payload = {"client_id" : client_id,
    "client_secret" : client_secret}
    auth = requests.post(starting_url+auth_url, data=payload).json() #getting token
    
    headers = {
        'accept': 'application/json',
        'X-Xapp-Token': auth['token']
    }

    if artsy_type == 'artist':
        target = starting_url+'/artists/'+artsy_id
        api_data = requests.get(target, headers=headers).json()
        try:
            api_data.update(requests.get(api_data['_links']['artworks']['href'], headers=headers).json())
        except:
            pass
    
    elif artsy_type == 'artwork':
        target = starting_url + '/artworks/' + artsy_id
        api_data = requests.get(target, headers = headers).json()
        try:
            api_data.update(requests.get(api_data['_links']['artists']['href'], headers=headers).json())
        except:
            pass
    
    elif artsy_type == 'show':
        artsy_id = artsy_id.split('?')[0]
        target = starting_url+'/shows/'+artsy_id
        api_data = requests.get(target, headers = headers).json()
        try:
            api_data.update(requests.get(api_data['_links']['images']['href'], headers=headers).json())
        except:
            pass
    
    elif artsy_type == 'www.artsy.net': #profile
        target = starting_url+'/profiles/'+artsy_id
        api_data = requests.get(target, headers = headers).json()
    
    else:
        return api_data
    
    return api_data