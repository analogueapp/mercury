#  Mercury

Mercury is a data enrichment service for [Analogue](https://analogue.app). It's primarily used to extract rich data and images for use on Analogue (people, topics, information etc)

### Endpoint
Live endpoint can be found: https://enrich-data.herokuapp.com/get

Pass in the parameter `url` with a valid URL to get data.

```
GET https://enrich-data.herokuapp.com/get?url=https://www.youtube.com/watch?v=dzqpfu5izjE
```

### Running locally

TODO How to get this project up and running locally.

## Project Scope
From a UX perspective, the idea solution is to get back data as fast as possible when someone adds a URL. So it would spit back the simple data first (url, image, description, medium type), and if it's new and needs to be enriched, we enrich it in the background by hitting the appropriated APIs.

So maybe there are two endpoints, one with a quick response (no enriching) and one that does the full enrichment. We can discuss and figure out the best solution together.

Supports the following URLs and APIs. Example URLs linked.

| Medium | URLs | APIs |
| :-- | :-- | :-- |
| Book | https://goodreads.com <br> https://amazon.com | [GoodReads API](https://www.goodreads.com/api) for data, authors, topics<br>[OpenLibrary](https://openlibrary.org/developers/api) for image covers<br>Amazon solution TBD |
| Music<br>Podcast | Spotify ([song](https://open.spotify.com/track/7sd72KZS8D59g5NmhxyHpJ), [album](https://open.spotify.com/album/2xkZV2Hl1Omi8rk2D7t5lN)) <br>Apple ([show](https://podcasts.apple.com/us/podcast/the-tim-ferriss-show/id863897795), [episode](https://podcasts.apple.com/us/podcast/429-nick-kokonas-on-resurrecting-restaurants-skin-in/id863897795)) | [Spotify API](https://developer.spotify.com/documentation/web-api/)<br>Apple TBD |
| Film<br>TV | IMDB ([film](https://www.imdb.com/title/tt0051808/), [show](https://www.imdb.com/title/tt0475784/), [episode](https://www.imdb.com/title/tt4227538/)) | OMDB API for data<br>[TMDB API](https://www.themoviedb.org/documentation/api) for people, trailers, etc |
| Art | [Artsy](https://www.artsy.net/artwork/evan-nesbit-lemon-drift) | [Artsy API](https://developers.artsy.net/v2/) |

TODO (Joel will write this) add ideal JSON response object

## Project Milestones

### V1 Setup
- [x] Setup initial code base
- [x] Migrate to Analogue github org
- [x] Set up initial APIs
- [x] Deploy on Heroku
- [ ] Integrate [Sentry addon](https://elements.heroku.com/addons/sentry) for production errors
- [ ] Add todos and scope to README
- [ ] Add local setup to README

### V2 Optimize
- [ ] Research if existing API wrappers exist in Python ([for example](https://github.com/mdzhang/goodreads-api-client-python))
- [ ] Potentially turn APIs in objects
- [ ] Endpoint for a quick response
- [ ] Build Analogue specific JSON response object
- [ ] Using Streaming API/Fanner model to optimize speed and handle jobs in background
- [ ] Error handling
- [ ] URL normalization (should correctly handle/remove query params in the url string)
- [ ] Handle other URLs from same URL domain
- [ ] Secure solution for handling API keys using [dotenv](https://github.com/theskumar/python-dotenv)

### V3 Support more sources
- [ ] Amazon
- [ ] Podcast and Music from Apple Music
- [ ] Artsy APIs
- [ ] Soundcloud API

### V4 Connnect
TODO. We can plan through the integration with Rails app soon.

## Commit Guide
Emojis are fun and easier to quickly scan, so we've adopted a system for commits inspired by [Emoji-Log](https://github.com/ahmadawais/Emoji-Log).

### Guidlines ↓

- Make your Git commit messages **imperative**.
- Make git commits based on actions you take.
- Write commit message like you're **giving an order**.
  — e.g., Use `Add` instead of `Added`.

## Emoji Legend

| Emoji | Commit Type | Example |
| :-- | :-- | :-- |
| ⚡️ | General update or improvement | `⚡️ Update route for Topic page` |
| 💡 | Data related | `💡 Add new field to User model` |
| 💫 | User Experience change | `💫 Add loading indicator on change` |
| 🎨 | Style update | `🎨 Update Avatar halo colors` |
| 🐞 | Bug fix | `🐞 Fix LoadMore failing on Profile` |
| 🔥 | Remove or Refactor | `🔥 Remove ProfilePreview component` |
| ✨ | Add something new | `✨ Add ProfileAvatar component` |
| 🚚 | Move or rename files | `🚚 Move /client to /client_old` |
| 📖 | Documentation update | `📖 Update README with emoji legend` |
| 🚀 | Deployment related | `🚀 Add .slugignore for Heroku` |
| 🤖 | Testing related | `🤖 Mock User Login/Logout` |
| 📦 | Dependency related | `📦 Update ant design to 3.24.1` |
| ⚙️ | Configuration related | `⚙️ Add react_on_rails initializer` |
| 🔗 | Merge pull request or branch | `🔗 Merge pull request #221` |

### How to add to your workflow
- _Easy:_ Use Character Viewer on Mac (`CMD⌘` + `CRTL⌃` + `SPACE`). Save the emojis to "Favorites" for quicker access.
- _Harder:_ Add custom versions of the [following functions](https://github.com/ahmadawais/Emoji-Log#the-workflow--meanings) to your `.bashrc`/`.zshrc`/`.bash_profile` files

## Additional Notes

- Leverages Open Graph and Twitter meta tags
- The scraper will do selective parsing which means it will create a parsing tree only for some specific tags, not for all the tags in the HTML doc.
- A link url will be sent using the GET Method only as it is faster than POST and PUT.
