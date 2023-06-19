import psycopg2
import sys

#TO DO: check other function than connect
class Database:
    def __init__(self, dbname, user, password, host, port,environment):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.env = environment
        self.connection = None
        self.cursor = None

    def connect(self):
        environment = self.env
        valid_environments = ['dev','test','prod']
        if environment in valid_environments:
            dbname_full = self.dbname + '_' + environment
        else:
            print("No valid environment defined!")
            sys.exit()

        try:
            self.connection = psycopg2.connect(
                dbname=dbname_full,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully")
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def fetch_data(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            print("Fetched data successfully")
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error fetching data:", error)
            return None