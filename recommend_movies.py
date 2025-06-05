# import pandas as pd
# import requests
# from mood_classifier import get_mood_from_plot

# TMDB_API_KEY = "bf52e37b5b0680c7b23be082af3bbdc3"

# def fetch_tmdb_poster(title, year=None):
#     """Search TMDB and return poster URL"""
#     try:
#         query = f"https://api.themoviedb.org/3/search/movie"
#         params = {
#             "api_key": TMDB_API_KEY,
#             "query": title,
#             "year": year,
#         }
#         res = requests.get(query, params=params)
#         data = res.json()
#         if data["results"]:
#             poster_path = data["results"][0].get("poster_path")
#             if poster_path:
#                 return f"https://image.tmdb.org/t/p/w500{poster_path}"
#     except:
#         pass
#     return None

# def load_and_tag_movies(csv_path='netflix_data.csv'):
#     df = pd.read_csv(csv_path)

#     # Only keep movies
#     df = df[df['type'].str.lower() == 'movie']
#     df = df.dropna(subset=['description'])

#     # Select and rename columns
#     df = df[['title', 'listed_in', 'description', 'release_year', 'duration', 'director']].copy()
#     df.rename(columns={
#         'listed_in': 'genre',
#         'description': 'plot',
#         'release_year': 'year'
#     }, inplace=True)

#     # Add placeholder language
#     df['language'] = 'Unknown'

#     # Add mood tags
#     df['mood_tags'] = df['plot'].apply(get_mood_from_plot)

#     # Add poster URLs
#     df['poster_url'] = df.apply(lambda row: fetch_tmdb_poster(row['title'], row['year']), axis=1)

#     return df

# def recommend_movies(df, mood=None, genre=None, language=None):
#     filtered = df.copy()

#     if mood:
#         filtered = filtered[filtered['mood_tags'].str.contains(mood, case=False, na=False)]
#     if genre:
#         filtered = filtered[filtered['genre'].str.contains(genre, case=False, na=False)]
#     if language and 'language' in filtered.columns:
#         filtered = filtered[filtered['language'].str.contains(language, case=False, na=False)]

#     return filtered[['title', 'genre', 'language', 'mood_tags', 'plot', 'poster_url']]

# recommend_movies.py

import pandas as pd

def load_and_tag_movies(csv_path='tagged_movies.csv'):
    return pd.read_csv(csv_path)

def recommend_movies(df, mood=None, genre=None, language=None):
    filtered = df.copy()

    if mood:
        filtered = filtered[filtered['mood_tags'].str.contains(mood, case=False, na=False)]
    if genre:
        filtered = filtered[filtered['genre'].str.contains(genre, case=False, na=False)]
    if language and 'language' in filtered.columns:
        filtered = filtered[filtered['language'].str.contains(language, case=False, na=False)]

    return filtered[['title', 'genre', 'language', 'mood_tags', 'plot', 'poster_url']]

# TMDB Poster API (used only in tagging step)
import requests
import os
from dotenv import load_dotenv
load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # safer than hardcoding

def fetch_tmdb_poster(title, year):
    try:
        url = f"https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "query": title,
            "year": year
        }
        response = requests.get(url, params=params)
        data = response.json()
        if data["results"]:
            poster_path = data["results"][0].get("poster_path")
            return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
    except:
        pass
    return ""
