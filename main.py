import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')

import os
import joblib
obj = pd.read_pickle(r"D:/PREM_64/movie recommendation/movire rec 1/movie reccomdation using machine learning/similarity.pkl")
similarity1 = pd.DataFrame(obj)
obj2=pd.read_pickle(r"D:/PREM_64/movie recommendation/movire rec 1/movie reccomdation using machine learning/movies.pkl")
movie=pd.DataFrame(obj2)
# Load the pickle file using joblib
movies_new=movie['title'].values

#recommend function
def recommend(moviee):
    # Get the index of the movie in the dataframe
    movie_index = movie[movie['title'] == moviee].index[0]
    # Get the distances from the similarity matrix
    distances = similarity1[movie_index]  # This should be a 1D array of distances
    # Enumerate over distances and sort them
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Correct access
    recommended_movies = [movie.iloc[i[0]].title for i in movies_list]
    return recommended_movies

option = st.selectbox("Which movie would you like to search ?",movies_new)

if st.button("Suggest me !!"):
    r=recommend(option)
    for i in r:
        st.write(i)
