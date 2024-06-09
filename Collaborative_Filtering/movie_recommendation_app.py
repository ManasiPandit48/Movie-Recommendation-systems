import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('Datasets/movies.csv')
ratings = pd.read_csv('Datasets/ratings.csv')

# Extract year from title and create a new column 'year'
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)').fillna(0).astype(int)
movies['title'] = movies['title'].str.replace(r'\s\(\d{4}\)', '', regex=True)

# Merge ratings with movie titles
df = pd.merge(ratings, movies, how='left', on='movieId')

# User-item matrix
user_item_matrix = df.pivot_table(index='userId', columns='title', values='rating')
user_item_matrix = user_item_matrix.fillna(0)

# Calculate the cosine similarity between movies
movie_similarity = cosine_similarity(user_item_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

def recommend_movies(fav_genre, fav_movie, n=8):
    # Filter movies by favorite genre
    genre_movies = df[df['genres'].str.contains(fav_genre)]
    
    # Check if any movies were filtered by genre
    if genre_movies.empty:
        return "No movies found matching the selected genre."
    
    # Filter movies similar to favorite movie
    if fav_movie in user_item_matrix.columns:
        similar_movies = movie_similarity_df[fav_movie].sort_values(ascending=False).index[1:n+1]
    else:
        return f"No similar movies found for '{fav_movie}'."
    
    # Combine and return recommended movies
    recommended_movies = genre_movies[genre_movies['title'].isin(similar_movies)]['title'].unique()
    
    # Explicitly checking if recommended_movies is not None and has elements
    if recommended_movies is not None and len(recommended_movies) > 0:
        return recommended_movies[:n]
    else:
        return "No recommendations found."


# Streamlit app
st.title("Movie Recommendation System")

fav_movie = st.text_input("Enter Your Favorite Movie:")
fav_genre = st.text_input("Enter Your Favorite Genre (optional):", key="genre")

if st.button("Get Recommendations"):
    if fav_movie:
        recommendations = recommend_movies(fav_genre, fav_movie)
        if isinstance(recommendations, str):
            st.write(recommendations)
        else:
            st.write("Recommended movies based on your favorite movie:")
            for movie in recommendations:
                st.write(movie)
    else:
        st.write("Please enter your favorite movie.")
