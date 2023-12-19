import streamlit as st

st.set_page_config(page_title = "mymovie",page_icon="🎥", layout="centered", initial_sidebar_state = "auto")
import pandas as pd
import pickle
import numpy as np
import requests

page_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
</style>
'''
st.markdown(page_img, unsafe_allow_html=True)


############################################
st.title("Movie Recommender System ")
movies_dict = pd.read_pickle("indices.pkl")

indices = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
"Type or select a movie from the dropdown",
 indices['title'].values
)


cos_sim = pd.read_pickle('cos_sim.pkl')
hybrid_df = pd.read_pickle('hybrid_df.pkl')

def info(movie_id):
    f = "https://api.themoviedb.org/3/movie/"
    e = "?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    url =f + str(movie_id) + e
    #url = "https://api.themoviedb.org/3/movie/"+"2522"+"?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    overview = data["overview"]
    tagline = data["tagline"]
    runtime = data["runtime"]
    release_date = data["release_date"]
    vote_average = data["vote_average"]
    vote_count = data["vote_count"]
    return full_path, overview, tagline, runtime, release_date, vote_average, vote_count

def predict(title, similarity_weight=0.7, top_n=10):
    data = hybrid_df.reset_index()
    index_movie = data[data['original_title'] == title].index
    similarity = cos_sim[index_movie].T
    
    sim_df = pd.DataFrame(similarity, columns=['similarity'])
    final_df = pd.concat([data, sim_df], axis=1)
    # You can also play around with the number
    final_df['final_score'] = final_df['score']*(1-similarity_weight) + final_df['similarity']*similarity_weight
    
    final_df_sorted = final_df.sort_values(by='final_score', ascending=False).head(top_n)
    kq = final_df_sorted.rename(columns={'original_title': 'title'})
    merged_df = pd.merge(kq,indices , on='title')
    idx = []
    title = [] 
    
    idx = merged_df['id']
    title = merged_df['title']
    return title, idx


n,p = predict(selected_movie_name)
names = []
posters = []
posters = []
overview = []
tagline = []
runtime = []
release_day = []
vote_average = []
vote_count = []
for i in n:
    names.append(i)
count = 1
for i in p:
    if count == 1:
        fp, ov, tl, rt, rd, va, vc = info(i)
        posters.append(fp)
        overview.append(ov)
        tagline.append(tl)
        runtime.append(rt)
        release_day.append(rd)
        vote_average.append(va)
        vote_count.append(vc)
    else: 
        fp, ov, tl, rt, rd, va, vc = info(i)
        posters.append(fp)
        
        
st.title("Your film")
col1, col2 = st.columns(2)
with col1:
    st.image(posters[0])
with col2:
    with st.markdown(
        """
        <div style='border: 1px solid #e6e6e6; background-color: black; padding: 10px; border-radius: 5px;'>
        <p> <span style='font-weight: bold;'>{}</span></p>
        <p>Overview: <span style='font-weight: bold;'>{}</span></p>
        <p> <span style='font-weight: bold;'>{}</span></p>
        <p>Runtime: <span style='font-weight: bold;'>{}</span></p>
        <p>Release day: <span style='font-weight: bold;'>{}</span></p>
        <p>Vote average: <span style='font-weight: bold;'>{}</span></p>
        <p>Vote count: <span style='font-weight: bold;'>{}</span></p>
        </div>
        """.format(names[0], overview[0], tagline[0], runtime[0], release_day[0], vote_average[0], vote_count[0]),
        unsafe_allow_html=True
    ):
        pass
   
def write(n):
    with st.markdown(
            """
            <div style='border: 1px solid #e6e6e6; background-color: white; padding: 10px; border-radius: 5px;'>
            <p> <span style='font-weight: bold;'>{}</span></p>
            </div>
            """.format(n),
            unsafe_allow_html=True
        ):
            pass
    return 0
    
if st.button("Recommend"):
    st.write(" ")
    col1, col2, col3 = st.columns(3)
    with col1:
        write(names[0])
        st.image(posters[1])   
    
    with col2:
        write(names[2])
        st.image(posters[2])
    
    with col3:
        write(names[3])
        st.image(posters[3])
    
    col4, col5, col6 = st.columns(3)
    with col4:
        write(names[4])
        st.image(posters[4])
 
    with col5:
        write(names[5])
        st.image(posters[5])
 
    with col6:
        write(names[6])
        st.image(posters[6])

    col7, col8, col9 = st.columns(3)
    with col7:
        write(names[7])
        st.image(posters[7])
    
    with col8:
        write(names[8])
        st.image(posters[8])
  
    with col9:
        write(names[9])
        st.image(posters[9])
   