from utils.tag_parsers import main_generic
from utils.get_facebook import get_facebook_API
from typing import Dict

def get_main(requests_object ,url) -> dict:

    response = get_facebook_API(url)

    if None in [response[x] for x in response.keys()]:
        tag_parser_response = main_generic(requests_object, url)

        for key in response.keys():
            if response[key] is None:
                response[key] = tag_parser_response[key]
        
        return response

    return response
