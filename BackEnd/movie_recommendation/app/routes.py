from flask import request, jsonify
from . import app
from .recommendation import perform_recommendation
from preprocess import load_movie_data

movies, ratings = load_movie_data()


@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/recommend', methods=['POST'])
def recommend_movies():
    data = request.json  # Receive data from the request body as JSON
    query = data.get('query')

    if query is None:
        return jsonify({'error': 'Missing or invalid "query" parameter'}), 400

    # Log the data received from the request
    print(f'Received query: {query}')

    recommendations = perform_recommendation(query, movies, ratings)

    # Log the response data before sending it
    print(f'Response recommendations: {recommendations}')

    return jsonify(recommendations)
