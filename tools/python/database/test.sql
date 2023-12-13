CREATE TEMPORARY TABLE tst_table(
   id VARCHAR,
   rand_string VARCHAR
);

INSERT INTO tst_table (id,rand_string) VALUES 
    ('1','testing'),
    ('2','test2');

--SELECT * FROM tst_table WHERE id='1';
--SELECT * FROM tst_table WHERE id='2';
SELECT * FROM tst_table;


--SELECT *,'1' AS query_order FROM data_engineer.employee;
--SELECT emp_name, '2' AS query_order FROM data_engineer.employee;
--SELECT *,'3' AS query_order FROM data_engineer.employee WHERE emp_id=1; 