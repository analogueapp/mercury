test_tag_parser_output = {
    "description": "An extended version of the documentary from the series finale of Silicon Valley. #HBO #SiliconValleyHBO Subscribe to HBO on YouTube: https://goo.gl/wtFYd7 Fr...",
    "form": "video",
    "image": "https://i.ytimg.com/vi/ab1H602yc_Y/maxresdefault.jpg",
    "medium": "video_link",
    "title": "Silicon Valley | Ten Years Later: The Extended Pied Piper Documentary | HBO",
    "url": "https://www.youtube.com/watch?v=ab1H602yc_Y",
}

test_get_params_url_output = {
    "url": "https://www.creativelive.com/flash-sale",
    "medium": "link",
    "form": "text",
    "description": "photo & video ",
}

test_get_imdb_movie_output = {
    "description": "Directed by Frank Darabont.  With Tim Robbins, Morgan Freeman, Bob Gunton, William Sadler. Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY1200_CR89,0,630,1200_AL_.jpg",
    "medium": "film",
    "title": "The Shawshank Redemption (1994) - IMDb",
    "url": "http://www.imdb.com/title/tt0111161/"
}

test_enrich_imdb_movie_output = "The Shawshank Redemption"

test_get_imdb_tv_output = {
    "description": "Created by David Benioff, D.B. Weiss.  With Emilia Clarke, Peter Dinklage, Kit Harington, Lena Headey. Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia.",
    "form": "video",
    "image": "https://m.media-amazon.com/images/M/MV5BYTRiNDQwYzAtMzVlZS00NTI5LWJjYjUtMzkwNTUzMWMxZTllXkEyXkFqcGdeQXVyNDIzMzcwNjc@._V1_UY1200_CR126,0,630,1200_AL_.jpg",
    "medium": "tv",
    "title": "Game of Thrones (TV Series 2011–2019) - IMDb",
    "url": "http://www.imdb.com/title/tt0944947/"
}

test_enrich_imdb_tv_output = "Game of Thrones"

test_get_imdb_person_output = {
    "description": "Christopher Nolan, Writer: Interstellar. Best known for his cerebral, often nonlinear, storytelling, acclaimed writer-director Christopher Nolan was born on July 30, 1970, in London, England. Over the course of 15 years of filmmaking, Nolan has gone from low-budget independent films to working on some of the biggest blockbusters ever made. At 7 years old, Nolan began making short movies ...",
    "form": "text",
    "image": "https://m.media-amazon.com/images/M/MV5BNjE3NDQyOTYyMV5BMl5BanBnXkFtZTcwODcyODU2Mw@@._V1_UY1200_CR118,0,630,1200_AL_.jpg",
    "medium": "link",
    "title": "Christopher Nolan - IMDb",
    "url": "http://www.imdb.com/name/nm0634240/"
}

test_enrich_imdb_person_output = "Christopher Nolan"

test_get_goodreads_output = {
    "description": "Dear Reader,  I'm sorry to say that the book you are holding in your hands is extremely unpleasant. It tells an unhappy tale about three ...",
    "form": "text",
    "image": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1436737029i/78411._SR1200,630_.jpg",
    "medium": "book",
    "title": "The Bad Beginning (A Series of Unfortunate Events, #1)",
    "url": "https://www.goodreads.com/work/best_book/1069597-the-bad-beginning"
}

test_enrich_goodreads_output = "Lemony Snicket"

test_get_wikiart_artwork_output = {
    "description": "‘The Chess Player’ was created in 1876 by Thomas Eakins in Realism style. Find more prominent pieces of genre painting at Wikiart.org – best visual art database.",
    "form": "text",
    "image": "https://uploads6.wikiart.org/images/thomas-eakins/the-chess-player-1876.jpg!Large.jpg",
    "medium": "link",
    "title": "The Chess Player, 1876 - Thomas Eakins - WikiArt.org",
    "url": "https://www.wikiart.org/en/thomas-eakins/the-chess-player-1876"
}

test_enrich_wikiart_artwork_output = {
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

test_get_netflix_series_output = {
    "description":"A century after Earth was devastated by a nuclear apocalypse, 100 space station residents are sent to the planet to determine whether it's habitable.",
    "form":"text",
    "image": "https://occ-0-2433-2705.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABSyRr1pavWg4aPlGU6FyjVIBJWexYTehdgzBVaIs4ZQ01eosSaMVE2zuv3I8HvFtcHnu9CsV76Siq1vaUXF69hqaDJWB.jpg?r=99e",
    "medium":"link",
    "title":"The 100 | Netflix",
    "url":"https://www.netflix.com/title/70283264"
}

test_enrich_netflix_series_output = 'The 100'

test_get_netflix_movie_output = {
    "description": "The Boss Baby brings his big brother Tim to the office to teach him the art of business in this animated series sprung from the hit film.",
    "form": "text",
    "image": "https://occ-0-2433-2705.1.nflxso.net/dnm/api/v6/Z-WHgqd_TeJxSuha8aZ5WpyLcX8/AAAABfmElnIKi4AXTddLZd6uMkLsNESXkTjihbtxVWq5AwdNLTO_lB7DbcIHbeAhmlHChCq-9Vi_LliTq547e03hrEPc5Bvi.jpg?r=b03",
    "medium": "link",
    "title": "The Boss Baby: Back in Business | Netflix Official Site",
    "url": "https://www.netflix.com/title/80178943"
}

test_enrich_netflix_movie_output = 'The Boss Baby: Back in Business'

test_get_spotify_track_output = {
    "description": "Unstoppable, a song by Sia on Spotify",
    "form": "audio",
    "image": "https://i.scdn.co/image/ab67616d0000b273754b2fddebe7039fdb912837",
    "medium": "song",
    "title": "Unstoppable",
    "url": "https://open.spotify.com/track/1yvMUkIOTeUNtNWlWRgANS"
}

test_enrich_spotify_track_output = {
    "id": "1yvMUkIOTeUNtNWlWRgANS",
    "name": "Unstoppable",
    "type": "track"
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
    'id': "6yIEe1y08bqC5LFEctRdTf",
    "name": "Een Klein Beetje Geluk",
    "release_date": "2016-11-25"
}


test_get_spotify_show_output = {
    "description": "Listen to Linear Digressions on Spotify. Linear Digressions is a podcast about machine learning and data science.  Machine learning is being used to solve a ton of interesting problems, and to accomplish goals that were out of reach even a few short years ago.",
    "form": "text",
    "image": "https://i.scdn.co/image/44e5b855038aea05acc317b99fbe713171997ee7",
    "medium": "link",
    "title": "Linear Digressions",
    "url": "https://open.spotify.com/show/1JdkD0ZoZ52KjwdR0b1WoT"
}

test_enrich_spotify_show_output = {
    "name": "Linear Digressions",
    "media_type": "audio",
    "publisher": "Ben Jaffe and Katie Malone",
    "type": "show"
}

test_get_spotify_artist_output = {
    "description": "Artist · 33.1M monthly listeners.",
    "form": "audio",
    "image": "https://i.scdn.co/image/63e7afb473ac268477b4436dc66510bebbc73791",
    "medium": "audio_link",
    "title": "Sia",
    "url": "https://open.spotify.com/artist/5WUlDfRSoLAfcVSX1WnrxN"
}

test_enrich_spotify_artist_output = {
    "id": "5WUlDfRSoLAfcVSX1WnrxN",
    "name": "Sia",
    "type": "artist"
}

test_get_spotify_playlist_output = {
    "description": "Spotify · Playlist · 50 songs · 4.5M likes",
    "form": "audio",
    "image": "https://i.scdn.co/image/ab67706f00000003488c19d1e35668647e8aa316",
    "medium": "playlist",
    "title": "Rock This",
    "url": "https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv"
}

test_enrich_spotify_playlist_output = {
    "name": "Rock This",
    "type": "playlist",
    "id": "37i9dQZF1DXcF6B6QPhFDv"
}

test_get_spotify_episode_output = {
    "description": "Listen to this episode from Andrew Schulz's Flagrant 2 with Akaash Singh on Spotify. This week Andrew Schulz, Akaash SIngh, and AlexxMedia discuss episodes 9 & 10 of the ESPN docuseries, The Last Dance (Michael Jordan Doc). INDULGE!  Want an extra episode a week? Join the Flagrant Army www.Patreon.com/FLAGRANT2",
    "form": "text",
    "image": "https://i.scdn.co/image/980355c2010a40f7c12d63d696d17ab501fe0a7b",
    "medium": "link",
    "title": "The Last Dance: Episodes 9 & 10",
    "url": "https://open.spotify.com/episode/467Uq5ZG2VJtaE6EZwnWNO"
}

test_enrich_spotify_episode_output = {
    "type": "episode",
    "description": "This week Andrew Schulz, Akaash SIngh, and AlexxMedia discuss episodes 9 & 10 of the ESPN docuseries, The Last Dance (Michael Jordan Doc). INDULGE!  Want an extra episode a week? Join the Flagrant Army www.Patreon.com/FLAGRANT2",
    "name": "The Last Dance: Episodes 9 & 10",
    "id": "467Uq5ZG2VJtaE6EZwnWNO"
}
