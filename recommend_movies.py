# recommend_movies.py

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = 'data/'
TOP_N = 10

# Load preprocessed data
df = pd.read_pickle(DATA_PATH + 'movies_df.pkl')
movie_embeddings = np.load(DATA_PATH + 'movie_embeddings.npy')

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_movies(user_mood_prompt, genre=None, language=None, country=None, content_type=None, threshold=0.75, top_n=TOP_N):

    user_embedding = model.encode([user_mood_prompt])
    similarities = cosine_similarity(user_embedding, movie_embeddings)[0]

    df['similarity'] = similarities
    df_filtered = df.copy()

    if content_type:
        content_type = content_type.strip().lower()
        df_filtered = df_filtered[df_filtered['type'].str.lower() == content_type]

    if genre:
        # Split comma-separated genres, strip spaces, lowercase
        genres = [g.strip().lower() for g in genre.split(',')]
        # Create regex pattern for OR match
        pattern = '|'.join(genres)
        df_filtered = df_filtered[df_filtered['listed_in'].str.lower().str.contains(pattern, regex=True, na=False)]

    if language:
        language = language.strip().lower()
        df_filtered = df_filtered[df_filtered['language'].str.lower().str.contains(language, na=False)]

    if country:
        country = country.strip().lower()
        df_filtered = df_filtered[df_filtered['country'].str.lower().str.contains(country, na=False)]

    # Filter by minimum similarity score threshold
    df_filtered = df_filtered[df_filtered['similarity'] >= threshold]

    top_recs = df_filtered.sort_values(by='similarity', ascending=False).head(top_n)

    return top_recs[['title', 'listed_in', 'plot', 'year', 'duration', 'director', 'language', 'country', 'similarity']]
