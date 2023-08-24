import requests
from bs4 import BeautifulSoup


def fetch_topics(title, author):
    db_results = fetch_db_topics(title, author)
    ol_results = fetch_ol_topics(title, author)
    topics = db_results + ol_results
    return topics


def fetch_db_topics(title, author):
    # Define the endpoint
    endpoint = "https://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=book&MaxHits=3&QueryString="

    # Construct the query URL
    query_url = f"{endpoint}{title}"

    # Fetch the data from DBpedia
    headers = {"Accept": "application/xml"}
    response = requests.get(query_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch data from DBpedia. Status code: {response.status_code}")
        return []

    data = response.text

    # Parse the XML data using BeautifulSoup
    parsed_data = BeautifulSoup(data, "xml")

    # Fetch the first three results
    top_results = parsed_data.find_all("Result", limit=3)

    if not top_results:
        print("No results found on DBpedia.")
        return []

    # Iterate through the results and find the first valid one
    for result in top_results:
        result_title = result.Label.string
        result_description = result.Description.string if result.Description else ""

        if (
            title.lower() in result_title.lower()
            and author.lower() in result_description.lower()
        ):
            # Extract categories for the valid result
            category_uris = [
                category.URI.string for category in result.find_all("Category")
            ]
            # Extract category names from the URIs
            category_names = [
                uri.split("/")[-1].replace("_", " ").replace("Category:", "")
                for uri in category_uris
            ]
            return category_names

    print(
        f"No exact match found on DBpedia for title: '{title}' and author: '{author}'"
    )
    return []


def fetch_ol_topics(title, author):
    search_url = f'https://openlibrary.org/search.json?title={title.replace(" ", "+")}&author={author.replace(" ", "+")}'
    s_resp = requests.get(search_url).json()
    docs = s_resp["docs"]
    if len(docs) > 0:
        key = docs[0].get("key", "")
    else:
        return []
    works_url = f"https://openlibrary.org{key}.json"
    w_resp = requests.get(works_url).json()

    places = w_resp.get("subject_places", [])
    times = w_resp.get("subject_times", [])
    people = w_resp.get("subject_people", [])
    subjects = w_resp.get("subjects", [])

    topics = places + times + people + subjects
    return topics
