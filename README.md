# 🎬 Dynamic Mood-Based Movie Recommender

A smart and interactive movie/TV show recommendation system that adapts to your **mood**, genre, and content preferences. Powered by **local LLaMA 3**, **Sentence-BERT**, **VADER sentiment analysis**, and enhanced with **TMDB poster & rating API**, this Streamlit-based app feels like your personal Netflix assistant.

---

## 📌 What It Does

- 🧠 Understands your **mood or free-text description**
- 🎭 Uses **VADER** to tag moods from movie plots
- 🧮 Embeds text using **Sentence-BERT** for similarity search
- 🧑‍💻 Powered by **LLaMA 3** (running locally) for mood classification
- 🌐 Filters by **genre, country, language, and type (Movie/TV Show)**
- 🖼️ Fetches **posters and ratings** via TMDB API
- 🎯 Ranks by semantic **similarity score**
- 🧨 Built with **Streamlit** – easy to run and customize

---

## 🖼️ Screenshot

![Screenshot](images/screenshot1.png)

---

## 🧰 Tech Stack

| Component        | Library/Tool                      |
|------------------|-----------------------------------|
| Frontend         | Streamlit                         |
| Mood Classifier  | LLaMA 3 (via `llama-cpp-python`)  |
| Embedding Model  | Sentence-BERT (`all-MiniLM-L6-v2`)|
| Plot Sentiment   | NLTK + VADER                      |
| Poster & Ratings | TMDB API                          |
| Data             | Netflix Open Data (CSV format)    |

---

## 🗂️ Project Structure

.
├── app.py # Main Streamlit app
├── mood_classifier.py # LLaMA 3 prompt-based mood inference
├── preprocess_and_tag_movies.py # Preprocess data using VADER mood tagging
├── preprocess_movies.py # Generate SBERT embeddings
├── recommend_movies.py # Core recommendation logic
├── tmdb_posters.py # Fetch posters/ratings via TMDB API
├── data/
│ ├── movies_df.pkl # Preprocessed DataFrame
│ └── movie_embeddings.npy # Embedding matrix
├── images/
│ └── screenshot1.png # App screenshot
├── netflix_data.csv # Source dataset
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

### 1. Clone the repository

bash
git clone https://github.com/yourusername/movie-mood-recommender.git
cd movie-mood-recommender

2. Create and activate a virtual environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Download the LLaMA 3 model
Visit TheBloke's LLaMA model collection on Hugging Face

Download a .gguf version like Llama-3-8B-Instruct.Q4_K_M.gguf

Place it in a directory (e.g., /models)

Update the path in mood_classifier.py accordingly

python
Copy
Edit
llm = Llama(model_path="/absolute/path/to/Llama-3-8B-Instruct.Q4_K_M.gguf")
🧪 Data Preprocessing Steps
Step 1: Tag moods using VADER
bash
Copy
Edit
python preprocess_and_tag_movies.py
Step 2: Generate SBERT plot embeddings
bash
Copy
Edit
python preprocess_movies.py
This saves:

data/movies_df.pkl

data/movie_embeddings.npy

🚀 Run the App
bash
Copy
Edit
streamlit run app.py
Then open http://localhost:8501 in your browser.

🔑 TMDB API Key
To get posters and IMDb-style ratings:

Create a free account on https://www.themoviedb.org/

Go to your account → Settings → API → Create key

Paste the API key inside tmdb_posters.py:

python
Copy
Edit
TMDB_API_KEY = "your_api_key_here"
🎯 Example Use Case
Prompt: "I'm in the mood for something romantic and emotional."

Filters: Genre = "Romance", Country = "France"

→ Returns top 10 matches with posters, ratings, and plot summaries sorted by similarity.

📋 requirements.txt
txt
Copy
Edit
streamlit
pandas
numpy
nltk
tqdm
requests
sentence-transformers
scikit-learn
llama-cpp-python
Install them:

bash
Copy
Edit
pip install -r requirements.txt
☁️ Deployment (Optional)
To deploy publicly, consider:

Streamlit Cloud – Easiest for this setup (but may not support LLaMA locally)

Render / Hugging Face Spaces – Use if you shift LLaMA to API-based inference

Docker – For full control in local/remote server setup

💡 Future Enhancements
🔄 Dynamic mood detection using multiple LLMs

👤 User login & saved preferences

🎵 Mood-to-music integration (Spotify API)

🧬 Visualize movie embedding clusters

📊 Add review sentiment alongside VADER mood

🙋 About the Author
Abhinav Kallooramana
🎓 MS in Business Analytics – UIUC
💼 Data Scientist | Movie buff & Tech enthusiast

📝 License
This project is open-source under the MIT License.
You are free to use, modify, and distribute it — just give credit.

⭐ If you find this useful
Please consider ⭐ starring the repo and sharing it!
