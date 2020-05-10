from imdb_api_service.sql_management.pg_conn_mgr import IMDBConnManager

class IMDBQueryManager(IMDBConnManager):

    def __init__(self):
        super().__init__()

    def get_all_movie_data(self):
        self.query_execution('SELECT * FROM moviedata')
        return self.all_data_from_query()

    def get_all_movies_over_half_billion(self):
        self.query_execution('SELECT * FROM moviedata WHERE gross > 500000000')
        return self.all_data_from_query()

if __name__ == '__main__':
    x = IMDBQueryManager()
    print(x.get_all_movie_data())