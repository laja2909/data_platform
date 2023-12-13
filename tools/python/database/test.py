from db import Database


db = Database(filename='config/database.ini',connection='postgresql')
#db.execute_query_full_process('INSERT INTO data_engineer.employee (emp_name,emp_salary) VALUES (%s,%s);',('Pekka',3000))
db.execute_query_full_process('SELECT * FROM data_engineer.employee')

#db.execute_query_in_file_full_process(filename='test.sql')
#db.connect()
#db.fetch_data('SELECT * FROM data_engineer.employee')
#db.execute_query('INSERT INTO data_engineer.employee (emp_name,emp_salary) VALUES (%s,%s);',('Hugh',3000))
#db.execute_query_in_file(filename='test.sql')
#db.disconnect()

