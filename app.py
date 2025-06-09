import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox('Select a movie', movie_list)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)