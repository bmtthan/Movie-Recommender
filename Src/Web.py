#21280016 Trần Minh Hiển 
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process

st.set_page_config(
    page_title = "Movie recommender system"
)
st.title("Movie recommender system.")


path = ''
movies_dict = pd.read_pickle(path + "indices.pkl")
# movies_dict = pickle.load(open('indices.pkl','rb'))
indices = pd.DataFrame(movies_dict)#=indices
selected_movie_name = st.selectbox(
"Type or select a movie from the dropdown",
 indices['title'].values
)


movies_model = pd.read_pickle('movies_model_knn.pkl')
model_knn= NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
movie_names = pd.read_pickle('movie_name.pkl')


def Recommender(movie_name, data, model, n_recommendations):
    model.fit(data)
    movie_index = process.extractOne(movie_name, movie_names['title'])[2]
    print('Movie Selected: ',movie_names['title'][movie_index], ', Index: ', movie_index)
    print('Searching for recommendations.....')
    distances, indices = model.kneighbors(data[movie_index], n_neighbors=n_recommendations)
    recc_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
    recommend_frame = []
    for val in recc_movie_indices:
#         print(movie_names['title'][val[0]])
        recommend_frame.append({'Title':movie_names['title'][val[0]],'Distance':val[1],'id':movie_names['id'][val[0]]})
    df = pd.DataFrame(recommend_frame, index = range(1,n_recommendations))
    return df.Title , df.id

def fetch_poster(movie_id):
    f = "https://api.themoviedb.org/3/movie/"
    e = "?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    url =f + str(movie_id) + e
    #url = "https://api.themoviedb.org/3/movie/"+"2522"+"?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

n,p = Recommender(selected_movie_name, movies_model, model_knn, 11)
names = []
posters = []
for i in n:
    names.append(i)
for i in p:
    posters.append(fetch_poster(i))

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.text(names[0])
    st.image(posters[0])
with col2:
    st.text(names[1])
    st.image(posters[1])
with col3:
    st.text(names[2])
    st.image(posters[2])
with col4:
    st.text(names[3])
    st.image(posters[3])
with col5:
    st.text(names[4])
    st.image(posters[4])
col6, col7, col8, col9, col10 = st.columns(5)
with col6:
    st.text(names[5])
    st.image(posters[5])
with col7:
    st.text(names[4])
    st.image(posters[4])
with col8:
    st.text(names[7])
    st.image(posters[7])
with col9:
    st.text(names[8])
    st.image(posters[8])
with col10:
    st.text(names[9])
    st.image(posters[9])

