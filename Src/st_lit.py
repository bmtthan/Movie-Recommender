import streamlit as st
import pandas as pd
import pickle
import numpy as np
import requests

page_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://qpet.vn/wp-content/uploads/2023/04/anh-cho-cuoi.jpg");
    background-size: cover;
    }
    </style>
'''
st.markdown(page_img, unsafe_allow_html=True)

############################################
st.title("Movie Recommender System ")
st.title("Choose movie genre")
action_movie = st.checkbox("Action Movie")
horror_movie = st.checkbox("Horror Movie")
comedy = st.checkbox("Comedy")
romcom = st.checkbox("Romcom")
drama = st.checkbox("Drama")
science_fiction = st.checkbox("Science Fiction")
historical = st.checkbox("Historical Film")
epic_movie = st.checkbox("Epic Movie")
documentary = st.checkbox("Documentary")
romance_movie = st.checkbox("Romance Movie")
blockbuster = st.checkbox("Blockbuster")
adaptation = st.checkbox("Adaptation")
musical_movie = st.checkbox("Musical Movie")
crime_gangster = st.checkbox("Crime & Gangster Films")

genre = []
if action_movie:
    genre.append("Action Movie")
if horror_movie:
    genre.append("Horror Movie")
if comedy:
    genre.append("Comedy")
if romcom:
    genre.append("Romcom")
if drama:
    genre.append("Drama")
if science_fiction:
    genre.append("Science Fiction")
if historical:
    genre.append("Historical Film")
if epic_movie:
    genre.append("Epic Movie")
if documentary:
    genre.append("Documentary")
if romance_movie:
    genre.append("Romance Movie")
if blockbuster:
    genre.append("Blockbuster")
if adaptation:
    genre.append("Adaptation")
if musical_movie:
    genre.append("Musical Movie")
if crime_gangster:
    genre.append("Crime & Gangster Films")
st.header("Your choose:")
st.write(genre)


#####################################
movies_dict = pd.read_pickle("../Arts/indices.pkl")
# movies_dict = pickle.load(open('indices.pkl','rb'))
indices = pd.DataFrame(movies_dict)#=indices
st.write(indices)
selected_movie_name = st.selectbox(
"Type or select a movie from the dropdown",
 indices['title'].values
)



####################################
# indices = smovies[['id','title','poster_path']]
cosine_sim = pd.read_pickle("../../cosine_sim.pkl")

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

def get_recommendations(title):
    idx = indices[indices.title == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:10]
    movie_indices = [i[0] for i in sim_scores]
    return indices.iloc[movie_indices].title,indices.iloc[movie_indices].id


#/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg
#/rhIRbceoE9lR4veEXuwCC2wARtG.jpg
#https://api.themoviedb.org/3/movie/862?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US
# st.image('https://www.themoviedb.org/t/p/w300_and_h450_bestv2/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg')
n,p = get_recommendations(selected_movie_name)
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