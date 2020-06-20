test_tag_parser_output = {
    "description": "An extended version of the documentary from the series finale of Silicon Valley. #HBO #SiliconValleyHBO Subscribe to HBO on YouTube: https://goo.gl/wtFYd7 Fr...",
    "form": "video",
    "image": "https://i.ytimg.com/vi/ab1H602yc_Y/maxresdefault.jpg",
    "medium": "video_link",
    "title": "Silicon Valley | Ten Years Later: The Extended Pied Piper Documentary | HBO",
    "url": "https://www.youtube.com/watch?v=ab1H602yc_Y",
}

test_get_without_og_twitter_output = {
    "description": "This site is supported by donations to The OEIS Foundation.\n",
    "form": "text",
    "image": "https://i.ibb.co/",
    "medium": "link",
    "title": "List of LaTeX mathematical symbols - OeisWiki",
    "url": "https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols",
}

test_get_params_url_output = {
    "title": "Flash Sale",
    "url": "https://www.creativelive.com/flash-sale",
    "medium": "link",
    "form": "text",
    "image": "https://downloads.creativelive.com/social/Facebook_1600x1227.jpg",
    "description": "photo & video ",
}


test_get_imdb_movie_output = {
    "title": "The Shawshank Redemption (1994) - IMDb",
    "url": "http://www.imdb.com/title/tt0111161/",
    "medium": "film",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
    "description": "Directed by Frank Darabont.  With Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler. Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
}

test_enrich_imdb_movie_output = "The Shawshank Redemption"


test_get_imdb_tv_output = {
    "title": "Game of Thrones (TV Series 2011–2019) - IMDb",
    "url": "http://www.imdb.com/title/tt0944947/",
    "medium": "tv",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_UY1200_CR126,0,630,1200_AL_.jpg",
    "description": "Created by David Benioff, D.B. Weiss.  With Emilia Clarke, Peter Dinklage, Kit Harington, Lena Headey. Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
}
test_enrich_imdb_tv_output = "Game of Thrones"


test_get_imdb_person_output = {
    "title": "Christopher Nolan - IMDb",
    "url": "http://www.imdb.com/name/nm0634240/",
    "medium": "link",
    "form": "text",
    "image": "https://m.media-amazon.com/images/M/MV5BNjE3NDQyOTYyMV5BMl5BanBnXkFtZTcwODcyODU2Mw@@._V1_UY1200_CR118,0,630,1200_AL_.jpg",
    "description": "Christopher Nolan, Writer: Interstellar. Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan was born on July 30, 1970, in London, England. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made. At 7 years old, Nolan began making short movies ...",
}
test_enrich_imdb_person_output = "Christopher Nolan"


test_get_goodreads_output = {
    "title": "The Bad Beginning (A Series of Unfortunate Events, #1)",
    "url": "https://www.goodreads.com/work/best_book/1069597-the-bad-beginning",
    "medium": "book",
    "form": "text",
    "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436737029i/78411._SR1200,630_.jpg",
    "description": "Dear Reader,  I'm sorry to say that the book you are holding in your hands is extremely unpleasant. It tells an unhappy tale about three ...",
}
test_enrich_goodreads_output = "Lemony Snicket"


test_get_wikiart_artwork_output = {
    "title": "The Chess Player, 1876 - Thomas Eakins - WikiArt.org",
    "url": "https://www.wikiart.org/en/thomas-eakins/the-chess-player-1876",
    "medium": "link",
    "form": "text",
    "image": "https://uploads6.wikiart.org/images/thomas-eakins/the-chess-player-1876.jpg!Large.jpg",
    "description": "‘The Chess Player’ was created in 1876 by Thomas Eakins in Realism style. Find more prominent pieces of genre painting at Wikiart.org – best visual art database.",
}
test_enrich_wikiart_artwork_output = {
    "data": [
        {
            "id": "57726f82edc2cb3880bb105d",
            "title": "Chess-Players",
            "url": None,
            "artistUrl": "honore-daumier",
            "artistName": "Honore Daumier",
            "artistId": "57726d7fedc2cb3880b481f6",
            "completitionYear": 1867,
            "width": 750,
            "image": "https://uploads8.wikiart.org/images/honore-daumier/chess-players.jpg!Large.jpg",
            "height": 585,
        },
        {
            "id": "577272a0edc2cb3880c5ebd3",
            "title": "Egyptian Chess Players",
            "url": None,
            "artistUrl": "sir-lawrence-alma-tadema",
            "artistName": "Sir Lawrence Alma-Tadema",
            "artistId": "57726d84edc2cb3880b48a2b",
            "completitionYear": 1865,
            "width": 750,
            "image": "https://uploads1.wikiart.org/images/alma-tadema-lawrence/egyptian-chess-players-1865.jpg!Large.jpg",
            "height": 511,
        },
        {
            "id": "57727661edc2cb3880d14ee1",
            "title": "Portrait of Chess Players",
            "url": None,
            "artistUrl": "marcel-duchamp",
            "artistName": "Marcel Duchamp",
            "artistId": "57726d87edc2cb3880b49292",
            "completitionYear": 1911,
            "width": 573,
            "image": "https://uploads7.wikiart.org/images/marcel-duchamp/portrait-of-chess-players-1911.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727663edc2cb3880d150c9",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "marcel-duchamp",
            "artistName": "Marcel Duchamp",
            "artistId": "57726d87edc2cb3880b49292",
            "completitionYear": 1911,
            "width": 706,
            "image": "https://uploads8.wikiart.org/images/marcel-duchamp/the-chess-players-1911.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727903edc2cb3880d9e170",
            "title": "Portrait of chess player A. D.  Petrova",
            "url": None,
            "artistUrl": "grigoriy-myasoyedov",
            "artistName": "Grigoriy Myasoyedov",
            "artistId": "57726d8bedc2cb3880b49aea",
            "completitionYear": None,
            "width": 384,
            "image": "https://uploads8.wikiart.org/images/grigoriy-myasoyedov/portrait-of-chess-player-a-d-petrova.jpg",
            "height": 550,
        },
        {
            "id": "57727e43edc2cb3880ea56d9",
            "title": "Sketch for The Chess Players",
            "url": None,
            "artistUrl": "thomas-eakins",
            "artistName": "Thomas Eakins",
            "artistId": "57726d9aedc2cb3880b4b6e8",
            "completitionYear": None,
            "width": 493,
            "image": "https://uploads4.wikiart.org/images/thomas-eakins/sketch-for-the-chess-players.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "57727e45edc2cb3880ea599c",
            "title": "The Chess Player",
            "url": None,
            "artistUrl": "thomas-eakins",
            "artistName": "Thomas Eakins",
            "artistId": "57726d9aedc2cb3880b4b6e8",
            "completitionYear": 1876,
            "width": 750,
            "image": "https://uploads6.wikiart.org/images/thomas-eakins/the-chess-player-1876.jpg!Large.jpg",
            "height": 544,
        },
        {
            "id": "57728019edc2cb3880f004dd",
            "title": "The Chess Player",
            "url": None,
            "artistUrl": "corneliu-baba",
            "artistName": "Corneliu Baba",
            "artistId": "57726da3edc2cb3880b4c802",
            "completitionYear": 1948,
            "width": 348,
            "image": "https://uploads5.wikiart.org/images/corneliu-baba/the-chess-player-1948.jpg",
            "height": 400,
        },
        {
            "id": "57728380edc2cb3880fabf99",
            "title": "Chess Players",
            "url": None,
            "artistUrl": "ernest-meissonier",
            "artistName": "Ernest Meissonier",
            "artistId": "57726dbbedc2cb3880b4ed63",
            "completitionYear": 1853,
            "width": 750,
            "image": "https://uploads7.wikiart.org/images/ernest-meissonier/chess-players-1853.jpg!Large.jpg",
            "height": 588,
        },
        {
            "id": "577283a6edc2cb3880fb4eef",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "john-lavery",
            "artistName": "John Lavery",
            "artistId": "57726dbcedc2cb3880b4ef5b",
            "completitionYear": 1929,
            "width": 750,
            "image": "https://uploads5.wikiart.org/images/john-lavery/the-chess-players-1929.jpg!Large.jpg",
            "height": 480,
        },
        {
            "id": "5772842bedc2cb3880fd1a37",
            "title": "Chess Players III",
            "url": None,
            "artistUrl": "willi-baumeister",
            "artistName": "Willi Baumeister",
            "artistId": "57726dc1edc2cb3880b4f87c",
            "completitionYear": 1924,
            "width": 355,
            "image": "https://uploads0.wikiart.org/images/willi-baumeister/chess-players-iii-1924.jpg",
            "height": 451,
        },
        {
            "id": "5772893dedc2cb38800d231b",
            "title": "The Chess Players",
            "url": None,
            "artistUrl": "william-orpen",
            "artistName": "William Orpen",
            "artistId": "57726dfbedc2cb3880b552a2",
            "completitionYear": 1902,
            "width": 464,
            "image": "https://uploads7.wikiart.org/images/william-orpen/the-chess-players-1902.jpg!Large.jpg",
            "height": 600,
        },
        {
            "id": "5c7f810cedc2c95a04e53552",
            "title": "Chess Player",
            "url": None,
            "artistUrl": "max-oppenheimer",
            "artistName": "Max Oppenheimer",
            "artistId": "5c7bc0f9edc2c911c8eaf361",
            "completitionYear": 1916,
            "width": 576,
            "image": "https://uploads1.wikiart.org/00226/images/max-oppenheimer/chess-player-1916.jpg",
            "height": 450,
        },
    ],
    "paginationToken": "mYYKCPvUlMCe%2bm%2bFr5oqhRUwpA2NgYOK%2fqurC%2bhv3IPFO0G5x7nxRaZ3JcZqONEG2ICeCVS8n78enlsBEi8VqA%3d%3d",
    "hasMore": False,
}


test_get_handleparams_sample = {
    "url": "https://www.google.com/search?sxsrf=ALeKk008Cq1wh8s7ndSr8aRtsSUp9zw1hg:1592632411112",
    "ei": "W6TtXvurBpKuUpOxiOgP",
    "q": "flask travis continuous deployment heroku",
    "oq": "flask travis continuous deployment heroku",
    "gs_lcp": "CgZwc3ktYWIQAzoECCMQJzoGCAAQFhAeOgIIADoFCCEQoAE6BAghEBU6BwghEAoQoAE6CAghEBYQHRAeUPrSB1iVmQhggJsIaABwAHgAgAHjAYgBmSOSAQQyLTIxmAEAoAEBqgEHZ3dzLXdpeg",
    "sclient": "psy-ab",
    "ved": "0ahUKEwi7xfyI2o_qAhUSlxQKHZMYAv0Q4dUDCAw",
    "uact": "5",
}

test_get_handleparams_output = "https://www.google.com/search?sxsrf=ALeKk008Cq1wh8s7ndSr8aRtsSUp9zw1hg:1592632411112&ei=W6TtXvurBpKuUpOxiOgP&q=flask travis continuous deployment heroku&oq=flask travis continuous deployment heroku&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoGCAAQFhAeOgIIADoFCCEQoAE6BAghEBU6BwghEAoQoAE6CAghEBYQHRAeUPrSB1iVmQhggJsIaABwAHgAgAHjAYgBmSOSAQQyLTIxmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwi7xfyI2o_qAhUSlxQKHZMYAv0Q4dUDCAw&uact=5"

test_enrich_netflix_series_output = 'The 100'

test_get_netflix_series_output = {
    "description":"A century after Earth was devastated by a nuclear apocalypse, 100 space station residents are sent to the planet to determine whether it's habitable.",
    "form":"text",
    "medium":"link",
    "title":"The 100 | Netflix",
    "url":"https://www.netflix.com/title/70283264"
}

test_enrich_netflix_movie_output = 'The Boss Baby: Back in Business'


test_get_netflix_movie_output = {
"description": "The Boss Baby brings his big brother Tim to the office to teach him the art of business in this animated series sprung from the hit film.",
"form": "text",
"medium": "link",
"title": "The Boss Baby: Back in Business | Netflix Official Site",
"url": "https://www.netflix.com/title/80178943"
}


test_get_spotify_album_output = {
"description": "Een Klein Beetje Geluk, an album by Ali B on Spotify",
"form": "audio",
"image": "https://i.scdn.co/image/ab67616d0000b273d90474e6a8ae2d8599334921",
"medium": "album",
"title": "Een Klein Beetje Geluk",
"url": "https://open.spotify.com/album/6yIEe1y08bqC5LFEctRdTf"
}


test_enrich_spotify_album_output = {
    'album_details': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'copyrights': [{'text': '2016 TRIFECTA', 'type': 'C'}, {'text': '2016 Warner Music Benelux B.V.', 'type': 'P'}], 'external_ids': {'upc': '190296982033'}, 'external_urls': {'spotify': 'https://open.spotify.com/album/6yIEe1y08bqC5LFEctRdTf'}, 'genres': [], 'href': 'https://api.spotify.com/v1/albums/6yIEe1y08bqC5LFEctRdTf', 'id': '6yIEe1y08bqC5LFEctRdTf', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273d90474e6a8ae2d8599334921', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02d90474e6a8ae2d8599334921', 'width': 300}, 
{'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851d90474e6a8ae2d8599334921', 'width': 64}], 'label': 'WM Benelux BV', 'name': 'Een Klein Beetje Geluk', 'popularity': 59, 'release_date': '2016-11-25', 'release_date_precision': 'day', 'total_tracks': 15, 'tracks': {'href': 'https://api.spotify.com/v1/albums/6yIEe1y08bqC5LFEctRdTf/tracks?offset=0&limit=50', 'items': [{'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 
'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 
'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 
'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 25507, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/7F16PfviI1tUEKIIv4zuUy'}, 'href': 'https://api.spotify.com/v1/tracks/7F16PfviI1tUEKIIv4zuUy', 'id': '7F16PfviI1tUEKIIv4zuUy', 'is_local': False, 'name': 'Intro', 'preview_url': None, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:7F16PfviI1tUEKIIv4zuUy'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0O0Hr8JCTPqXyPLdN6kzdC'}, 'href': 'https://api.spotify.com/v1/artists/0O0Hr8JCTPqXyPLdN6kzdC', 'id': '0O0Hr8JCTPqXyPLdN6kzdC', 
'name': 'Glen Faria', 'type': 'artist', 'uri': 'spotify:artist:0O0Hr8JCTPqXyPLdN6kzdC'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 272842, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/0hTT6rkSBf5JoeyYW5m5V9'}, 'href': 'https://api.spotify.com/v1/tracks/0hTT6rkSBf5JoeyYW5m5V9', 'id': '0hTT6rkSBf5JoeyYW5m5V9', 'is_local': False, 'name': 'Gekke Kleine Jongen (feat. Glen Faria)', 'preview_url': 'https://p.scdn.co/mp3-preview/ed0b137f343fb8f3a2244aa50e84a94c2dcbd2ca?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 2, 'type': 'track', 'uri': 'spotify:track:0hTT6rkSBf5JoeyYW5m5V9'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0Jsk5iYMr5aNjHury7blm1'}, 'href': 'https://api.spotify.com/v1/artists/0Jsk5iYMr5aNjHury7blm1', 'id': '0Jsk5iYMr5aNjHury7blm1', 'name': 'Boef', 'type': 'artist', 'uri': 'spotify:artist:0Jsk5iYMr5aNjHury7blm1'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0HDMwoCS316xhKCZlJPBnc'}, 'href': 'https://api.spotify.com/v1/artists/0HDMwoCS316xhKCZlJPBnc', 'id': '0HDMwoCS316xhKCZlJPBnc', 'name': 'Sevn Alias', 'type': 'artist', 'uri': 'spotify:artist:0HDMwoCS316xhKCZlJPBnc'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 
'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 
'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 
'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 210344, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/5PzEv1KC5lpndbo6CPIftT'}, 'href': 'https://api.spotify.com/v1/tracks/5PzEv1KC5lpndbo6CPIftT', 'id': '5PzEv1KC5lpndbo6CPIftT', 'is_local': False, 'name': 'Een Klein Beetje Geluk (feat. Boef & Sevn Alias)', 'preview_url': 'https://p.scdn.co/mp3-preview/5ea5b0c870344d032fc5a65a7d20da0a639c8f66?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 3, 'type': 'track', 'uri': 'spotify:track:5PzEv1KC5lpndbo6CPIftT'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5eir5zFJpES4j7gsymbVyl'}, 'href': 'https://api.spotify.com/v1/artists/5eir5zFJpES4j7gsymbVyl', 'id': '5eir5zFJpES4j7gsymbVyl', 'name': 'Ronnie Flex', 'type': 'artist', 'uri': 'spotify:artist:5eir5zFJpES4j7gsymbVyl'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 201189, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/6IziItlMuSIuVEeKIWDbSK'}, 'href': 'https://api.spotify.com/v1/tracks/6IziItlMuSIuVEeKIWDbSK', 'id': '6IziItlMuSIuVEeKIWDbSK', 'is_local': False, 'name': 'Dat Is Money (feat. Ronnie Flex)', 'preview_url': 'https://p.scdn.co/mp3-preview/92c7c6c25070c5ee42c567029666fd157e8b9d03?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 4, 'type': 'track', 'uri': 'spotify:track:6IziItlMuSIuVEeKIWDbSK'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1A6HQzOvtGaCYihOuIKjE6'}, 'href': 'https://api.spotify.com/v1/artists/1A6HQzOvtGaCYihOuIKjE6', 'id': '1A6HQzOvtGaCYihOuIKjE6', 'name': 'Mr. Polska', 'type': 'artist', 'uri': 'spotify:artist:1A6HQzOvtGaCYihOuIKjE6'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 196579, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/1Maq6N9PbuEEWPdYdVCptw'}, 'href': 'https://api.spotify.com/v1/tracks/1Maq6N9PbuEEWPdYdVCptw', 'id': '1Maq6N9PbuEEWPdYdVCptw', 'is_local': False, 'name': 'Pimp Ze (feat. Mr. Polska)', 'preview_url': 'https://p.scdn.co/mp3-preview/407e6b66b817320e34edb2021a6be54160624336?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 5, 'type': 'track', 'uri': 'spotify:track:1Maq6N9PbuEEWPdYdVCptw'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5erZiBCKPxe9FaTiXHO00m'}, 'href': 'https://api.spotify.com/v1/artists/5erZiBCKPxe9FaTiXHO00m', 'id': '5erZiBCKPxe9FaTiXHO00m', 'name': 'Adje', 'type': 'artist', 'uri': 'spotify:artist:5erZiBCKPxe9FaTiXHO00m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1wFoE1RwBMWoWkXcFrCgsx'}, 'href': 'https://api.spotify.com/v1/artists/1wFoE1RwBMWoWkXcFrCgsx', 'id': '1wFoE1RwBMWoWkXcFrCgsx', 'name': 'Josylvio', 'type': 'artist', 'uri': 'spotify:artist:1wFoE1RwBMWoWkXcFrCgsx'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0HDMwoCS316xhKCZlJPBnc'}, 'href': 'https://api.spotify.com/v1/artists/0HDMwoCS316xhKCZlJPBnc', 'id': '0HDMwoCS316xhKCZlJPBnc', 'name': 'Sevn Alias', 'type': 'artist', 'uri': 'spotify:artist:0HDMwoCS316xhKCZlJPBnc'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 
'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 
'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 
'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 184908, 
'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/17bYFKHY3u2i2wuMsPPLW6'}, 'href': 'https://api.spotify.com/v1/tracks/17bYFKHY3u2i2wuMsPPLW6', 'id': '17bYFKHY3u2i2wuMsPPLW6', 'is_local': False, 'name': 'Douane (feat. Adje, Josylvio & Sevn Alias)', 'preview_url': 'https://p.scdn.co/mp3-preview/7e8b90415da4195e4c7247ff72dccaaae4fa6c91?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 6, 'type': 'track', 'uri': 'spotify:track:17bYFKHY3u2i2wuMsPPLW6'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 
'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 
'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 
'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 26622, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/1LcCUZtzuOG6YfhsEpBqkC'}, 'href': 'https://api.spotify.com/v1/tracks/1LcCUZtzuOG6YfhsEpBqkC', 'id': '1LcCUZtzuOG6YfhsEpBqkC', 'is_local': False, 'name': 'Interlude', 'preview_url': None, 'track_number': 7, 'type': 'track', 'uri': 'spotify:track:1LcCUZtzuOG6YfhsEpBqkC'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/7hofCdl9njgv82JjU0HPwI'}, 'href': 'https://api.spotify.com/v1/artists/7hofCdl9njgv82JjU0HPwI', 'id': '7hofCdl9njgv82JjU0HPwI', 'name': 'Jandro', 'type': 'artist', 'uri': 'spotify:artist:7hofCdl9njgv82JjU0HPwI'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1EYdbYpGAuJy6uZo4sVMoM'}, 'href': 'https://api.spotify.com/v1/artists/1EYdbYpGAuJy6uZo4sVMoM', 'id': '1EYdbYpGAuJy6uZo4sVMoM', 'name': 'Idaly', 'type': 'artist', 'uri': 'spotify:artist:1EYdbYpGAuJy6uZo4sVMoM'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 204187, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/0zyPYDOWxSO6LGPyGuepD8'}, 'href': 'https://api.spotify.com/v1/tracks/0zyPYDOWxSO6LGPyGuepD8', 'id': '0zyPYDOWxSO6LGPyGuepD8', 'is_local': False, 'name': 'Laten Vallen (feat. Jandro & Idaly)', 'preview_url': 'https://p.scdn.co/mp3-preview/ef563d2ae0fd6729133c0902271cff9e0dde624f?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 8, 'type': 'track', 'uri': 'spotify:track:0zyPYDOWxSO6LGPyGuepD8'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/2NX52zvQRp4AxVzhp2cMiP'}, 'href': 'https://api.spotify.com/v1/artists/2NX52zvQRp4AxVzhp2cMiP', 'id': '2NX52zvQRp4AxVzhp2cMiP', 'name': 'Kenny B', 'type': 'artist', 'uri': 'spotify:artist:2NX52zvQRp4AxVzhp2cMiP'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/6INEFmHKLhMIJAQzHUBAMd'}, 'href': 'https://api.spotify.com/v1/artists/6INEFmHKLhMIJAQzHUBAMd', 'id': '6INEFmHKLhMIJAQzHUBAMd', 'name': 'Lijpe', 'type': 'artist', 'uri': 'spotify:artist:6INEFmHKLhMIJAQzHUBAMd'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 243971, 'explicit': True, 'external_urls': {'spotify': 'https://open.spotify.com/track/7wGHeo3FH2PpeI0bCFaRor'}, 'href': 'https://api.spotify.com/v1/tracks/7wGHeo3FH2PpeI0bCFaRor', 'id': '7wGHeo3FH2PpeI0bCFaRor', 'is_local': False, 'name': 'Mensen Redden (feat. Lijpe & Kenny B)', 'preview_url': 'https://p.scdn.co/mp3-preview/a6ecb57ad6e080a5fef652df11a5422e3d1f7adb?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 9, 'type': 'track', 'uri': 'spotify:track:7wGHeo3FH2PpeI0bCFaRor'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 
'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0O0Hr8JCTPqXyPLdN6kzdC'}, 'href': 'https://api.spotify.com/v1/artists/0O0Hr8JCTPqXyPLdN6kzdC', 'id': '0O0Hr8JCTPqXyPLdN6kzdC', 'name': 'Glen Faria', 'type': 'artist', 'uri': 'spotify:artist:0O0Hr8JCTPqXyPLdN6kzdC'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 180211, 'explicit': False, 'external_urls': {'spotify': 'https://open.spotify.com/track/7i0f8iE9Qujn2zPHHVWiXY'}, 'href': 'https://api.spotify.com/v1/tracks/7i0f8iE9Qujn2zPHHVWiXY', 'id': '7i0f8iE9Qujn2zPHHVWiXY', 'is_local': False, 
'name': 'Waarheid Op Straat (feat. Glen Faria)', 'preview_url': 'https://p.scdn.co/mp3-preview/ed6ae1e156b0dd59a26b2d3a548211e6e86e6499?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 10, 'type': 'track', 'uri': 'spotify:track:7i0f8iE9Qujn2zPHHVWiXY'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/4XQhU3S4TyPkiPIsSu2hmA'}, 'href': 'https://api.spotify.com/v1/artists/4XQhU3S4TyPkiPIsSu2hmA', 'id': '4XQhU3S4TyPkiPIsSu2hmA', 'name': 'Diggy Dex', 'type': 'artist', 'uri': 'spotify:artist:4XQhU3S4TyPkiPIsSu2hmA'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 192123, 'explicit': False, 'external_urls': {'spotify': 'https://open.spotify.com/track/4IGlXv0WwGQmAkMLIEfbA0'}, 'href': 'https://api.spotify.com/v1/tracks/4IGlXv0WwGQmAkMLIEfbA0', 'id': '4IGlXv0WwGQmAkMLIEfbA0', 'is_local': False, 'name': 'Ik Huil Alleen Bij Jou (feat. Diggy Dex)', 'preview_url': 'https://p.scdn.co/mp3-preview/d147257c6dbf531dcfbbf721838c85b10f2ee84e?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 11, 'type': 'track', 'uri': 'spotify:track:4IGlXv0WwGQmAkMLIEfbA0'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5m5Fh8zrb0uHM85qwkIkVT'}, 'href': 'https://api.spotify.com/v1/artists/5m5Fh8zrb0uHM85qwkIkVT', 'id': '5m5Fh8zrb0uHM85qwkIkVT', 'name': 'Nielson', 'type': 'artist', 'uri': 'spotify:artist:5m5Fh8zrb0uHM85qwkIkVT'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 168539, 'explicit': False, 'external_urls': {'spotify': 'https://open.spotify.com/track/5IfgA1gKbLK1aK0V1AyonR'}, 'href': 'https://api.spotify.com/v1/tracks/5IfgA1gKbLK1aK0V1AyonR', 'id': '5IfgA1gKbLK1aK0V1AyonR', 'is_local': False, 'name': 'Glimp Van De Duivel (feat. Nielson)', 'preview_url': 'https://p.scdn.co/mp3-preview/78138e6f9ae5154f394b0266be1da1edb380e1e2?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 12, 'type': 'track', 'uri': 'spotify:track:5IfgA1gKbLK1aK0V1AyonR'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5eir5zFJpES4j7gsymbVyl'}, 'href': 'https://api.spotify.com/v1/artists/5eir5zFJpES4j7gsymbVyl', 'id': '5eir5zFJpES4j7gsymbVyl', 'name': 'Ronnie Flex', 'type': 'artist', 'uri': 'spotify:artist:5eir5zFJpES4j7gsymbVyl'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/1fTPAgBH6gCQZU9bBWVaOf'}, 'href': 'https://api.spotify.com/v1/artists/1fTPAgBH6gCQZU9bBWVaOf', 'id': '1fTPAgBH6gCQZU9bBWVaOf', 'name': 'I am Aisha', 'type': 'artist', 'uri': 'spotify:artist:1fTPAgBH6gCQZU9bBWVaOf'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 168195, 'explicit': False, 'external_urls': {'spotify': 'https://open.spotify.com/track/35M8wQUqtPzH7dQaR8KF29'}, 'href': 'https://api.spotify.com/v1/tracks/35M8wQUqtPzH7dQaR8KF29', 'id': '35M8wQUqtPzH7dQaR8KF29', 'is_local': False, 'name': 'Als Ik Met Je Ben (feat. Ronnie Flex & I Am Aisha)', 'preview_url': 'https://p.scdn.co/mp3-preview/19ca80c35095697ce82073711d6856324f5309b4?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 13, 'type': 'track', 'uri': 'spotify:track:35M8wQUqtPzH7dQaR8KF29'}, {'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/2eHZ1Vns5972fZNdhnjopG'}, 'href': 'https://api.spotify.com/v1/artists/2eHZ1Vns5972fZNdhnjopG', 'id': '2eHZ1Vns5972fZNdhnjopG', 'name': 'Brace', 'type': 'artist', 'uri': 'spotify:artist:2eHZ1Vns5972fZNdhnjopG'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/2NX52zvQRp4AxVzhp2cMiP'}, 'href': 'https://api.spotify.com/v1/artists/2NX52zvQRp4AxVzhp2cMiP', 'id': '2NX52zvQRp4AxVzhp2cMiP', 'name': 'Kenny B', 'type': 'artist', 'uri': 'spotify:artist:2NX52zvQRp4AxVzhp2cMiP'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 
'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 
'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 
'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 183936, 'explicit': 
False, 'external_urls': {'spotify': 'https://open.spotify.com/track/0uGWI6gl1vKgb44oR9PtTM'}, 'href': 'https://api.spotify.com/v1/tracks/0uGWI6gl1vKgb44oR9PtTM', 'id': '0uGWI6gl1vKgb44oR9PtTM', 'is_local': False, 'name': "Let's Go (feat. Kenny B & Brace)", 'preview_url': 'https://p.scdn.co/mp3-preview/2f54a5cd76a0faaf1d3b6fba93187053765a03c4?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 14, 'type': 'track', 'uri': 'spotify:track:0uGWI6gl1vKgb44oR9PtTM'}, 
{'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5quv5QEyL2XAloebaau69m'}, 'href': 'https://api.spotify.com/v1/artists/5quv5QEyL2XAloebaau69m', 'id': '5quv5QEyL2XAloebaau69m', 'name': 'Ali B', 'type': 'artist', 'uri': 'spotify:artist:5quv5QEyL2XAloebaau69m'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/0qZWRrQj38rwkxeRQ3HowZ'}, 'href': 'https://api.spotify.com/v1/artists/0qZWRrQj38rwkxeRQ3HowZ', 'id': '0qZWRrQj38rwkxeRQ3HowZ', 'name': 'Ruben Annink', 'type': 'artist', 'uri': 'spotify:artist:0qZWRrQj38rwkxeRQ3HowZ'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 179163, 'explicit': False, 'external_urls': {'spotify': 'https://open.spotify.com/track/6TARDLpAVAL3pvvbYkFhq9'}, 'href': 'https://api.spotify.com/v1/tracks/6TARDLpAVAL3pvvbYkFhq9', 'id': '6TARDLpAVAL3pvvbYkFhq9', 'is_local': False, 'name': 'Terwijl Jullie Nog Bij Me Zijn (feat. Ruben Annink)', 'preview_url': 'https://p.scdn.co/mp3-preview/567f8de912708c7e0b87ba8392bef6c39333faa3?cid=cc05b898faef4c89b0e9ad87e37b8158', 'track_number': 15, 'type': 'track', 'uri': 'spotify:track:6TARDLpAVAL3pvvbYkFhq9'}], 'limit': 50, 'next': None, 'offset': 0, 'previous': None, 'total': 15}, 'type': 'album', 'uri': 'spotify:album:6yIEe1y08bqC5LFEctRdTf'}
}