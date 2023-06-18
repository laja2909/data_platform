import psycopg2
#print(psycopg2.__version__)

#
conn = psycopg2.connect(
    host="localhost",
    database="DATABASE",
    user="USER",
    password="PASSWORD")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)
cur.close()

#to do: add separate class conn and make secure connection and make so that password or users are not exposed to github.
##Check https://www.postgresqltutorial.com/postgresql-python/connect/