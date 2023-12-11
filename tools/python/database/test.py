from db import Database


db = Database(filename='database.ini',section='postgresql')
db.connect()
#db.fetch_data('SELECT * FROM data_engineer.employee')
#db.execute_query('INSERT INTO data_engineer.employee (emp_name,emp_salary) VALUES (%s,%s);',('Hugh',3000))
db.execute_query_in_file(filename='test.sql')
db.disconnect()

