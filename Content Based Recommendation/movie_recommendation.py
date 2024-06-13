import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Title of the Streamlit app
st.title('Movie Recommendation System')

@st.cache_data
def load_data():
    df1 = pd.read_csv('datasets/tmdb_5000_credits.csv')
    df2 = pd.read_csv('datasets/tmdb_5000_movies.csv')
    df1.columns = ['id', 'title', 'cast', 'crew']
    df2 = df2.merge(df1, on='id')
    df2['genres'] = df2['genres'].apply(ast.literal_eval)
    df2['genres'] = df2['genres'].apply(lambda x: [d['name'] for d in x])
    df2['genres'] = df2['genres'].apply(lambda x: ' '.join(x))
    return df2

# Load data
df2 = load_data().copy()

# Preprocess data
C = df2['vote_average'].mean()
m = df2['vote_count'].quantile(0.9)
movies_list = df2.copy().loc[df2['vote_count'] >= m]
movies_list['score'] = movies_list.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)

# Function to get movie recommendations based on title and genre
def get_recommendations(title, genre, cosine_sim):
    indices = pd.Series(df2.index, index=df2['title_x']).drop_duplicates()
    idx = indices[title]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:]
    
    movie_indices = [i[0] for i in sim_scores if genre in df2['genres'].iloc[i[0]]]
    return df2.iloc[movie_indices[:10]]

# TF-IDF and cosine similarity
tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Streamlit sidebar
st.sidebar.title('Movie Recommender')
selected_movie = st.sidebar.selectbox('Select a movie:', df2['title_x'].values)
selected_genre = st.sidebar.selectbox('Select a genre:', df2['genres'].unique())

if st.sidebar.button('Recommend'):
    recommendations = get_recommendations(selected_movie, selected_genre, cosine_sim)
    st.write('Recommendations for "{}" in genre "{}":'.format(selected_movie, selected_genre))
    for i, row in recommendations.iterrows():
        st.write('{}. {}'.format(i+1, row['title_x']))
    
    # Popular and High Budget Movies based on recommendations
    st.subheader('Popular Movies among Recommendations')
    pop_rec = recommendations.sort_values('popularity', ascending=False)
    fig, ax = plt.subplots()
    ax.barh(pop_rec['title_x'].head(6), pop_rec['popularity'].head(6), color='skyblue')
    ax.invert_yaxis()
    ax.set_xlabel('Popularity')
    ax.set_title('Popular Movies')
    st.pyplot(fig)

    st.subheader('High Budget Movies among Recommendations')
    budget_rec = recommendations.sort_values('budget', ascending=False)
    fig, ax = plt.subplots()
    ax.barh(budget_rec['title_x'].head(10), budget_rec['budget'].head(10), color='skyblue')
    ax.invert_yaxis()
    ax.set_xlabel('Budget')
    ax.set_title('High Budget Movies')
    st.pyplot(fig)

