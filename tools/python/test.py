import psycopg2
import os
from platform_db import Database

ht='localhost'
db='landing_dev'
usr = os.environ['PG_DE_USER']
pwd = os.environ['PG_DE_PW']

db = Database(dbname='landing',
              user=os.environ['PG_DE_USER'], 
              password=os.environ['PG_DE_PW'],
              host='localhost',
              port='5432',
              environment='dev')


##dbname, user, password, host, port,environment

# Connect to the database
db.connect()
db.disconnect()


"""
conn = psycopg2.connect(
    host=ht,
    database = db,
    user = usr,
    password = pwd
)

cur = conn.cursor()
print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)
cur.close()
"""

#
"""
conn = psycopg2.connect(
    host="localhost",
    database="landing_dev",
    user="lmj_1993",
    password="data123!!annm")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
cur.close()
"""


#to do: add separate class conn and make secure connection and make so that password or users are not exposed to github.
##Check https://www.postgresqltutorial.com/postgresql-python/connect/