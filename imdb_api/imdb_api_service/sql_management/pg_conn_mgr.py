from psycopg2 import connect

# config = connect(dbname='imdb', user='postgres', password='postgres', host='localhost', port=5432)
# config = connect(dbname='imdb', user='postgres', password='postgres', host='81.102.129.142', port=5432)
# cursor = config.cursor()
# cursor.execute('SELECT * FROM moviedata')
# all_movie_data = cursor.fetchall()
# all_rows = all_movie_data
# print(all_rows)

class IMDBConnManager:

    def __init__(self, dbname='imdb', user='postgres', password='postgres', host='81.102.129.142', port=5432):
        self.connection = connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()

    def query_execution(self, sql_query_string):
        return self.cursor.execute(sql_query_string)

    def all_data_from_query(self):
        return self.cursor.fetchall()

if __name__ == '__main__':
    api = IMDBConnManager()
    api.query_execution('SELECT * FROM moviedata')
    print(api.all_data_from_query())