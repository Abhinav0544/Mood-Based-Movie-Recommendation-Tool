import pandas as pd
from tqdm import tqdm
from mood_classifier import get_mood_from_plot

def load_and_tag_movies(csv_path='netflix_data.csv', output_path='tagged_movies.csv'):
    df = pd.read_csv(csv_path)
    df = df[df['type'].str.lower() == 'movie']
    df = df.dropna(subset=['description'])
    df = df[['title', 'listed_in', 'description', 'release_year', 'duration', 'director']].copy()
    df.rename(columns={
        'listed_in': 'genre',
        'description': 'plot',
        'release_year': 'year'
    }, inplace=True)
    df['language'] = 'Unknown'

    mood_tags_list = []

    print("Tagging moods with progress:")
    for plot in tqdm(df['plot'], total=len(df)):
        mood = get_mood_from_plot(plot)
        mood_tags_list.append(mood)

    df['mood_tags'] = mood_tags_list
    df.to_csv(output_path, index=False)

    print(f"Tagging complete! Saved to {output_path}")
    return df

# ADD THIS
if __name__ == '__main__':
    load_and_tag_movies()

