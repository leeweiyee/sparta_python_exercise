from flask import Flask
from imdb_api_service.imdb_factory.imdb_factory_manager import IMDBFactory as IMDBFactory

imdb_api = Flask(__name__)

@imdb_api.route('/')
def home_page():
    return 'Welcome to the IMDB API'

@imdb_api.route('/all-movie-data')
def all_movie_data():
    return IMDBFactory().get_all_movie_data_json()

@imdb_api.route('/all-movies-over-half-billion')
def all_movies_over_half_billion():
    return IMDBFactory().get_all_movies_over_half_billion_json()

if __name__ == '__main__':
    imdb_api.run()