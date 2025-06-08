import streamlit as st
from recommend_movies import recommend_movies
from tmdb_posters import get_poster_and_rating



st.set_page_config(page_title="Dynamic Mood-Based Movie Recommender", page_icon="🎬")
# # Apply custom CSS for Netflix-style UI
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #e50914;
    }

    .stApp {
        background-color: #000000;
    }

    /* Text input fields */
    input[type="text"], input[type="search"] {
        color: red !important;
    }

    /* Dropdown (select box) display */
    .stSelectbox div[data-baseweb="select"] > div {
        color: red !important;
    }

    /* Button */
    .stButton button {
        background-color: #e50914;
        color: white;
    }

    /* Text area, if any */
    textarea {
        color: red !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 DynamicMood-Based Movie Recommendation System")
st.markdown("Describe your mood or what kind of movie you're in the mood for:")

mood_prompt = st.text_input("Mood or description", placeholder="e.g., I want something exciting and adventurous")
country = st.text_input("🌎 Preferred country (optional)", placeholder="e.g., India, USA,Korea,Spain,Turkey")

genre = st.text_input("Preferred genre (optional)", placeholder="e.g., drama, comedy, thriller")
language = st.text_input("Preferred language (optional)", placeholder="e.g., English, Hindi")

content_type = st.selectbox(
    "🎬 What do you want to watch?",
    options=["Movie", "TV Show"]
)

threshold = st.slider(
    "🔍 Minimum Similarity Threshold", 
    min_value=0.01, 
    max_value=0.95, 
    value=0.75, 
    step=0.05
)



if st.button("Recommend Movies"):
    if not mood_prompt.strip():
        st.warning("Please enter your mood or description.")
    else:
        with st.spinner("Finding movies matching your mood..."):
            recommendations = recommend_movies(mood_prompt, genre, language, country, content_type,threshold)



        if recommendations.empty:
            st.info("No matching titles found. Try changing your prompt or filters.")
        else:
            # Sort recommendations by similarity (should already be sorted, but ensure it here)
            recommendations = recommendations.sort_values(by='similarity', ascending=False).reset_index(drop=True)

            for idx, row in recommendations.iterrows():
                similarity = row['similarity']

                poster_url, rating = get_poster_and_rating(row['title'])

                if poster_url:
                    st.image(poster_url, width=200)

                if rating:
                    st.markdown(f"**TMDB Rating:** {rating:.1f}/10 ⭐")


                
                if poster_url:
                    st.image(poster_url, width=250)

                # Color based on similarity
                if similarity >= 0.9:
                    color = "lime"
                elif similarity >= 0.75:
                    color = "orange"
                else:
                    color = "red"
    
                # Add Top Pick badge for the first result
                if idx == 0:
                    st.markdown(f"""
                                    <div style='background-color: #e50914; color: white; padding: 8px; border-radius: 8px; font-size: 20px;'>
                                            🌟 Top Pick: <strong>{row['title']} ({row['year']})</strong>
                                    </div>
                                """, unsafe_allow_html=True)
                else:
                    st.markdown(f"### {row['title']} ({row['year']})")
    
                st.markdown(f"**Genre:** {row['listed_in']}")
                st.markdown(f"**Language:** {row['language']}")
                st.markdown(f"**Duration:** {row['duration']}")
                st.markdown(f"**Director:** {row['director']}")
                st.markdown(f"**Similarity Score:** <span style='color:{color}'>{similarity:.3f}</span>", unsafe_allow_html=True)
                st.write(row['plot'])
                st.markdown("---")
            for idx, row in recommendations.iterrows():
                st.markdown(f"### {row['title']} ({row['year']})")
                st.markdown(f"**Genre:** {row['listed_in']}")
                st.markdown(f"**Language:** {row['language']}")
                st.markdown(f"**Duration:** {row['duration']}")
                st.markdown(f"**Director:** {row['director']}")
                # st.markdown(f"**Similarity Score:** {row['similarity']:.3f}")
                similarity = row['similarity']
                if similarity >= 0.9:
                    color = "lime"
                elif similarity >= 0.75:
                    color = "orange"
                else:
                    color = "red"
                st.markdown(f"**Similarity Score:** <span style='color:{color}'>{similarity:.3f}</span>", unsafe_allow_html=True)

                st.write(row['plot'])
                st.markdown("---")
