#  Mercury [![CodeFactor](https://www.codefactor.io/repository/github/analogue-app/mercury/badge)](https://www.codefactor.io/repository/github/analogue-app/mercury)

Mercury is a data enrichment service for [Analogue](https://analogue.app). It's primarily used to extract rich data and images for use on Analogue (people, topics, information etc)

### Endpoint
Live endpoint can be found: https://analogue-mercury.herokuapp.com/get

Pass in the parameter `url` with a valid URL to get data.

```
GET https://analogue-mercury.herokuapp.com/get?url=https://www.youtube.com/watch?v=dzqpfu5izjE
```

### Running locally

Install Python3 ([setup guide](https://docs.python-guide.org/starting/install3/osx/)) and follow the [Flask installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/).

1) Create `virtualenv`
```bash
python3 -m venv mercury
```

2) Activate `virtualenv`
```bash
source mercury/bin/activate
```

3) Install requirements
```bash
pip install -r requirements.txt
```

4) Add to `.env` locally to run in debugger mode
```bash
FLASK_ENV=development
```

5) Run `app.py` from the root to start Flask
```
python3 app.py
```

6) Copy paste [these keys](https://www.notion.so/Mercury-API-keys-2bcae4d6433d477d8c5cb89f732afcfe) into your `.env` file


## Project Scope
From a UX perspective, the idea solution is to get back data as fast as possible when someone adds a URL. So it would spit back the simple data first (url, image, description, medium type), and if it's new and needs to be enriched, we enrich it in the background by hitting the appropriated APIs.

So maybe there are two endpoints, one with a quick response (no enriching) and one that does the full enrichment. We can discuss and figure out the best solution together.

Supports the following URLs and APIs. Example URLs linked.

| Medium | URLs | APIs |
| :-- | :-- | :-- |
| Book | https://goodreads.com <br> https://amazon.com | [Google Books API](https://developers.google.com/books) for data, authors, topics<br>[OpenLibrary](https://openlibrary.org/developers/api) for image covers<br>Amazon solution TBD |
| Music<br>Podcast | Spotify ([song](https://open.spotify.com/track/7sd72KZS8D59g5NmhxyHpJ), [album](https://open.spotify.com/album/2xkZV2Hl1Omi8rk2D7t5lN)) <br>Apple ([show](https://podcasts.apple.com/us/podcast/the-tim-ferriss-show/id863897795), [episode](https://podcasts.apple.com/us/podcast/429-nick-kokonas-on-resurrecting-restaurants-skin-in/id863897795)) | [Spotify API](https://developer.spotify.com/documentation/web-api/)<br>Apple TBD |
| Film<br>TV | IMDB ([film](https://www.imdb.com/title/tt0051808/), [show](https://www.imdb.com/title/tt0475784/), [episode](https://www.imdb.com/title/tt4227538/)) | OMDB API for data<br>[TMDB API](https://www.themoviedb.org/documentation/api) for people, trailers, etc |
| Art<br>WikiArt | [Artsy](https://www.artsy.net/artwork/evan-nesbit-lemon-drift)<br>[WikiArt](https://www.wikiart.org/en/caravaggio/calling-of-saint-matthew) | [Artsy API](https://developers.artsy.net/v2/)<br>[WikiArt API](https://docs.google.com/document/d/1T926unU7mx9Blmx3c8UE0UQTnO3MrDbXTGYVerVQFDU/edit) |

### Quick response endpoint `/get`
This endpoint will be used to get the initial data as quickly as possible. Ideally it doesn't even hit APIs, as to save time for the user. But you might have to hit APIs to get the specific medium and form type (e.g. for IMDB links, films vs TV shows)

JSON response:
```javascript
{
  title: 'url title from og or twitter or <title> tag'
  url: 'CANONICAL_URL_NORMALIZED', // shouldn't have query params, except for youtube (e.g. ?v=afdsafxxx)
  medium: 'one of the medium types mapped below',
  form: 'one of the form types mapped below',
  image: 'url to image from og or twitter tags or first image in html',
  description: 'short description from og or twitter or meta tags or first paragraph of html'
}
```

#### Medium mapping
| Form | Medium | URLs |
| :-- | :-- | :-- |
| `video` | `video_link` | youtube.com, vimeo.com, ted.com |
| `video` | `film` | imdb.com film url ([example](https://www.imdb.com/title/tt6751668/))
| `video` | `tv` | imdb.com show url ([example](https://www.imdb.com/title/tt0475784/))
| `video` | `tv_episode` | imdb.com episode url ([example](https://www.imdb.com/title/tt4227538/))
| `audio` | `song` | spotify.com song url ([example](https://open.spotify.com/track/1O6Nh2WvqKtH0uIkUuHTP3)) |
| `audio` | `album` | spotify.com album url ([example](https://open.spotify.com/album/58GlwqGojobPco2fTlpRB0)) |
| `audio` | `playlist` | spotify.com playlist url ([example](https://open.spotify.com/playlist/37i9dQZF1E8JIR7JqWUbRk)) |
| `audio` | `podcast` | spotify.com podcast show url ([example](https://open.spotify.com/show/4M55t5J54fENnEK2A8mzTB)) |
| `audio` | `podcast_episode` | spotify.com podcast episode url ([example](https://open.spotify.com/episode/2tuoVpTiiSKG0ybEwKdsum)) |
| `audio` | `audio_link` | soundcloud.com |
| `text` | `book` | amazon.com |
| `text` | `link` | default form and medium (most urls) |

### Rich response endpoint: `/enrich`
This endpoint will be used to enrich the data (through a background job in Rails). So this will provide full rich responses, including related data (e.g. authors for books from Google, director for films from IMDB).


## Additional Notes

- Leverages Open Graph and Twitter meta tags
- The scraper will do selective parsing which means it will create a parsing tree only for some specific tags, not for all the tags in the HTML doc.
- A link url will be sent using the GET Method only as it is faster than POST and PUT.
