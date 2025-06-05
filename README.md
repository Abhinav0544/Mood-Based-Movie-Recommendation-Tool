# 🎬 Mood-Based Movie Recommendation System

This is a simple movie recommendation system that tags Netflix movies based on the **mood inferred from plot descriptions** using a custom NLP classifier.

## 📁 Project Structure

## 🧠 Features

- Reads raw movie data (`netflix_data.csv`)
- Filters only **movies** (not TV shows)
- Cleans and preprocesses text
- Applies mood classification on movie plots
- Saves the result as `tagged_movies.csv` with `mood_tags`

## 🔍 Sample Moods

The classifier may tag moods like:

- Happy
- Sad
- Exciting
- Romantic
- Suspenseful
- Dark

(*You can expand/customize this list in `mood_classifier.py`*)

## 🚀 How to Run

1. Make sure you have Python 3.11 and dependencies installed:
    ```bash
    pip install pandas tqdm
    ```

2. Run the preprocessing and tagging script:
    ```bash
    python preprocess_and_tag_movies.py
    ```

3. Output will be saved to `tagged_movies.csv`

## 📦 Dependencies

- `pandas`
- `tqdm`

## 🛠️ To-Do (Optional Enhancements)

- Use a trained NLP model (like HuggingFace) to classify mood dynamically
- Build a Streamlit UI to recommend movies by mood
- Add language detection and genre-based filtering

## 🙋‍♂️ Author

**Abhinav Jaikumar Kallooramana**  
Data Scientist | Python & SQL Expert | Movie Buff 🎥

---

