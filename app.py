# app.py

import streamlit as st
from recommend_movies import load_and_tag_movies, recommend_movies

st.set_page_config(page_title="Mood-Based Movie Recommender", page_icon="🎬")
st.title("🎬 Mood-Based Movie Recommender")
st.markdown("Enter your current mood, and get movie recommendations that match!")

mood = st.text_input("Your mood (e.g., happy, emotional, dark, feel-good):")
genre = st.text_input("Preferred genre (optional):")
language = st.text_input("Language (e.g., English, Hindi) (optional):")

if st.button("Get Recommendations"):
    with st.spinner("Finding the best movies for your mood..."):
        df = load_and_tag_movies()
        recommendations = recommend_movies(df, mood, genre, language)

    if not recommendations.empty:
        st.success(f"Found {len(recommendations)} matching movie(s):")
        for _, row in recommendations.iterrows():
            st.subheader(row['title'])
            cols = st.columns([1, 3])
            if row.get('poster_url'):
                cols[0].image(row['poster_url'], width=120)
            with cols[1]:
                st.markdown(f"**Genre:** {row['genre']}")
                st.markdown(f"**Language:** {row['language']}")
                st.markdown(f"**Mood Tags:** {row['mood_tags']}")
                st.markdown(f"**Plot:** {row['plot']}")
            st.markdown("---")
    else:
        st.warning("No matching movies found. Try changing the filters.")


















# import streamlit as st
# from recommend_movies import load_and_tag_movies, recommend_movies

# st.title("🎬 Mood-Based Movie Recommender")

# st.markdown("Enter your current mood, and get movie recommendations that match!")

# mood = st.text_input("Your mood (e.g., happy, emotional, dark, feel-good):")
# genre = st.text_input("Preferred genre (optional):")
# language = st.text_input("Language (e.g., English, Hindi) (optional):")

# if st.button("Get Recommendations"):
#     with st.spinner("Classifying and recommending..."):
#         df = load_and_tag_movies()
#         recommendations = recommend_movies(df, mood, genre, language)

#     if not recommendations.empty:
#         st.success(f"Found {len(recommendations)} matching movie(s):")
#         for _, row in recommendations.iterrows():
#             st.subheader(row['title'])
#             st.markdown(f"**Genre:** {row['genre']} | **Language:** {row['language']}")
#             st.markdown(f"**Mood Tags:** {row['mood_tags']}")
#             st.markdown(f"**Plot:** {row['plot']}")
#             st.markdown("---")
#     else:
#         st.warning("No matching movies found. Try changing the filters.")

