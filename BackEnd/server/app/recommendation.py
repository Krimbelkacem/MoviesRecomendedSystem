import pandas as pd
from flask import jsonify

# Example recommendation logic in perform_recommendation function


def perform_recommendation(query, movies, ratings):
    # Filter movies by the specified genre (query)
    filtered_movies = movies[movies['genres'].str.contains(query, case=False)]

    # Join with ratings data to get user ratings
    rated_movies = filtered_movies.merge(ratings, on='movieId')

    # Group by movie and calculate average rating
    recommended_movies = rated_movies.groupby(
        'movieId')['rating'].mean().reset_index()

    # Sort by average rating in descending order
    recommended_movies = recommended_movies.sort_values(
        by='rating', ascending=False)

    # Get the top N recommended movies
    top_n_recommendations = recommended_movies.head(10)['movieId']

    # Convert movie IDs to movie titles
    top_n_recommendations_list = top_n_recommendations.map(
        lambda movie_id: movies[movies['movieId']
                                == movie_id]['title'].values[0]
    ).tolist()

    return top_n_recommendations_list
