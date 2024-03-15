import streamlit as st
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load data and preprocess
@st.cache_data()
def load_data():
    movies_data = pd.read_csv('movies.csv')
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')
    return movies_data

movies_data = load_data()

# Function to recommend similar movies
@st.cache_data()
def recommend_similar_movies(selected_movie, num_recommendations=20):
    combined_feature = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_feature)
    similarity = cosine_similarity(feature_vectors)
    find_close_match = difflib.get_close_matches(selected_movie, movies_data['title'].tolist())
    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data['title'] == close_match].index[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        similar_movies = []
        for i, movie in enumerate(sorted_similar_movies[:num_recommendations]):
            index = movie[0]
            title_from_index = movies_data.loc[index, 'title']
            similar_movies.append(title_from_index)
        return similar_movies

# Function to fetch movie poster using TMDb API
@st.cache_data()
def fetch_movie_poster(movie_title):
    # Get TMDb API key from your TMDb account: https://www.themoviedb.org/documentation/api
    api_key = "ffc42ca6e427cdb9fa3a287ab41c970d"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        # Get the first movie's poster path (if available)
        poster_path = data['results'][0]['poster_path']
        if poster_path:
            # Construct the full poster URL
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            return poster_url
    return None

# Sidebar - Movie Selection
st.sidebar.title('List of Movies')
selected_movie = st.sidebar.selectbox('Select a movie:', movies_data['title'].tolist())

if selected_movie:
    # Recommended Movies
    st.title(f"Movies similar to {selected_movie}:")
    similar_movies = recommend_similar_movies(selected_movie)
    for i, movie in enumerate(similar_movies):
        movie_poster = fetch_movie_poster(movie)
        if movie_poster:
            st.image(movie_poster, caption=movie, use_column_width=True)
        else:
            st.write(f"{i + 1}. {movie}")
