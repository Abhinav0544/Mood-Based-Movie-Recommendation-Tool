 # preprocess_movies.py

import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import os

def preprocess_and_embed(csv_path='tagged_movies_vader.csv', save_path='data/'):
    # Load CSV
    df = pd.read_csv(csv_path)
    
    # Basic check for required columns
    required_cols = ['title', 'listed_in', 'plot', 'year', 'duration', 'director', 'language', 'country', 'type']

    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in CSV: {missing_cols}")
    
    # Fill missing plots with empty string to avoid errors
    df['plot'] = df['plot'].fillna('')
    
    # Initialize SBERT model (you can pick any pre-trained model here)
    model = SentenceTransformer('all-MiniLM-L6-v2')  # fast and small model
    
    print("Generating embeddings for movie plots...")
    embeddings = model.encode(df['plot'].tolist(), show_progress_bar=True)
    
    # Save processed dataframe and embeddings
    os.makedirs(save_path, exist_ok=True)
    df.to_pickle(os.path.join(save_path, 'movies_df.pkl'))
    np.save(os.path.join(save_path, 'movie_embeddings.npy'), embeddings)
    
    print(f"Preprocessing and embedding done. Data saved to {save_path}")

if __name__ == '__main__':
    preprocess_and_embed()



    
