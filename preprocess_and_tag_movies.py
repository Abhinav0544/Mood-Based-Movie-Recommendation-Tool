import pandas as pd
from tqdm import tqdm
from nltk.sentiment import SentimentIntensityAnalyzer

def get_mood_from_plot_vader(plot):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(plot)['compound']
    if score >= 0.5:
        return 'uplifting'
    elif score <= -0.5:
        return 'dark'
    else:
        return 'neutral'
def load_and_tag_movies(csv_path='netflix_data.csv', output_path='tagged_movies_vader.csv'):
    df = pd.read_csv(csv_path)

    # Keep only rows with 'Movie' or 'TV Show' type
    df = df[df['type'].str.lower().isin(['movie', 'tv show'])]

    # Drop rows without description
    df = df.dropna(subset=['description'])

    # Keep only required columns including 'type' and 'listed_in'
    df = df[['title', 'listed_in', 'description', 'release_year', 'duration', 'director', 'type','country']].copy()

    # Rename columns (keep 'listed_in' intact)
    df.rename(columns={
        'description': 'plot',
        'release_year': 'year'
    }, inplace=True)

    # Set language as unknown for now
    df['language'] = 'Unknown'

    # Mood tagging
    print("Tagging moods with VADER (sentiment analysis):")
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    from tqdm import tqdm
    tqdm.pandas()

    def get_mood_from_plot_vader(plot):
        score = sia.polarity_scores(plot)['compound']
        if score >= 0.5:
            return 'uplifting'
        elif score <= -0.5:
            return 'dark'
        else:
            return 'neutral'

    df['mood_tags'] = df['plot'].progress_apply(get_mood_from_plot_vader)

    # Save
    df.to_csv(output_path, index=False)
    print(f"Saved tagged movies to {output_path}")
    return df


if __name__ == '__main__':
    # For example, to tag movies only:
    load_and_tag_movies()
