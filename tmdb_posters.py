import requests
import time

TMDB_API_KEY = "bf52e37b5b0680c7b23be082af3bbdc3"

def get_poster_and_rating(title, max_retries=5):
    url = "https://api.themoviedb.org/3/search/multi"
    params = {
        "api_key": TMDB_API_KEY,
        "query": title,
        "include_adult": False
    }

    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data["results"]:
                result = data["results"][0]
                poster_path = result.get("poster_path")
                rating = result.get("vote_average", None)

                poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
                return poster_url, rating

            return None, None

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)  # exponential backoff

    print(f"Failed to get poster and rating for {title} after {max_retries} attempts.")
    return None, None
