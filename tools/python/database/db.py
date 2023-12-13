import psycopg2
from helper import fetch_db_params

class Database:
    """
    Class database, holds db parameters as dictionary.
    Input: 
        filename -> filename from which database parameters are fetched
        section -> Section of the file that corresponds to specific database connection settings.
    """
    def __init__(self,filename,connection):
        self.db_params = fetch_db_params(filename,connection)
        
    def connect(self):
        """
        Connects to postgres database.
        Input: dictionary of database connection parameters. Should be passed as unpacked operator (**)
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

            try:
                results = self.cursor.fetchmany(10)
                print(results)
            except psycopg2.ProgrammingError:
                print("Query returned 0 rows.")
            
            self.connection.commit()
            
        except psycopg2.Error as error:
            print("Error executing query:", error)

    def execute_query_in_file(self, filename, params=None):
        try:
            with open(filename,"r") as sql_file:
                sql_queries = sql_file.read()
            
            self.cursor.execute(sql_queries)

            try:
                results = self.cursor.fetchmany(10)
                print(results)
            except psycopg2.ProgrammingError:
                print("Query returned 0 rows.")

            self.connection.commit()
            
        except psycopg2.Error as error:
            print("Error executing query:", error)
    
    def execute_query_full_process(self,query,params=None):
        self.connect()
        self.execute_query(query,params)
        self.disconnect()

    def execute_query_in_file_full_process(self,filename):
        self.connect()
        self.execute_query_in_file(filename)
        self.disconnect()
        