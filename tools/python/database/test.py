from db import Database


db = Database(filename='database.ini',section='postgresql')
db.connect()
db.disconnect()


"""
db = Database(dbname=dbname,
              user=user, 
              password=password,
              host=host,
              port=port
              )


##dbname, user, password, host, port,environment

# Connect to the database
db.connect()
db.disconnect()


"""