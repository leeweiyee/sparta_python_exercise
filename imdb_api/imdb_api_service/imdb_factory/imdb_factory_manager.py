from imdb_api_service.sql_management.query_manager import IMDBQueryManager
from imdb_api_service.json_management.json_encoding import IMDBJsonEncoder

class IMDBFactory:

    def __init__(self):
        self.json_encoder = IMDBJsonEncoder()
        self.imdb_query_manager = IMDBQueryManager()

    def get_all_movie_data_json(self):
        return self.json_encoder.create_imdb_dict_array(self.imdb_query_manager.get_all_movie_data())

    def get_all_movies_over_half_billion_json(self):
        return self.json_encoder.create_imdb_dict_array(self.imdb_query_manager.get_all_movies_over_half_billion())