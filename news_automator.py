import requests
from sys import argv
import time

API_KEY = '5c39dc84da9a48799329249151d25228'
URL = 'https://newsapi.org/v2/everything'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "gb",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    max_retries = 3
    timeout = 10  # seconds

    for attempt in range(max_retries):
        try:
            response = requests.get(URL, params=params, timeout=timeout)
            if response.status_code == 200:
                articles = response.json().get('articles', [])
                results = [{"title": article["title"], "url": article["url"]} for article in articles]
                return results
            else:
                print(f"Error: Unable to fetch articles. Status code: {response.status_code}")
        except requests.exceptions.Timeout:
            print("Error: Request timed out. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred. {e}")
        
        time.sleep(2)  # wait before retrying

    return []

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    max_retries = 3
    timeout = 10  # seconds

    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=query_parameters, timeout=timeout)
            if response.status_code == 200:
                sources = response.json().get('sources', [])
                for source in sources:
                    print(source['name'])
                    print(source['url'])
                return
            else:
                print(f"Error: Unable to fetch sources. Status code: {response.status_code}")
        except requests.exceptions.Timeout:
            print("Error: Request timed out. Retrying...")
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred. {e}")
        
        time.sleep(2)  # wait before retrying

    print("No sources found.")

if __name__ == "__main__":
    if len(argv) > 1:
        category = argv[1]
        print(f"Getting news for {category}...\n")
        articles = get_articles_by_category(category)
    else:
        query = "ChatGPT"
        print(f"Getting news for query: {query}...\n")
        articles = get_articles_by_query(query)

    if articles:
        for article in articles:
            print(article['title'])
            print(article['url'])
            print('')
    else:
        print("No articles found.")
