import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    
    recommend_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_posters

# Load the movie data from the pickle file
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity_movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app
st.title('Movie Recommendation System')

# Create a selectbox to choose a movie from the list of titles
movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

# Display the selected movie
st.write('You selected:', movie_name)

if st.button('Recommend'):
    names, posters = recommend(movie_name)
    cols = st.columns(5)

    for i, col in enumerate(cols):
        col.text(names[i])
        col.image(posters[i])