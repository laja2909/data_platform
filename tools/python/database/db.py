import psycopg2
from helper import fetch_db_params

class Database:
    """
    Class database, holds db parameters as dictionary.
    Input: 
        filename -> filename from which database parameters are fetched
        section -> Section of the file that corresponds to specific database connection settings.
    """
    def __init__(self,filename,section):
        self.db_params = fetch_db_params(filename,section)
        
    def connect(self):
        """
        Connects to postgres database.
        Input: dictionary of database connection parameters. Should be bassed as unpacked operator (**)
        """
        try:
            self.connection = psycopg2.connect(**self.db_params)
            #dbname=self.dbname,
            #user=self.user,
            #password=self.password,
            #host=self.host,
            #port=self.port
            #)
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)


    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")
        else:
            print("Connection not found.")

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
        


"""
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
"""