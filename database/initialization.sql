--run in psql (superuser) to create default databases
REVOKE ALL ON SCHEMA public FROM public;

--data_engineer role which should have CRUD privileges to all databases and tables.
CREATE ROLE data_engineer;
--CREATE USER lmj_1993 PASSWORD 'PASSWORD';
--GRANT data_engineer to lmj_1993;

--initial databases
CREATE DATABASE landing_dev;
REVOKE ALL ON DATABASE landing_dev FROM public;
GRANT ALL ON DATABASE landing_dev to data_engineer;

CREATE DATABASE landing_test;
REVOKE ALL ON DATABASE landing_test FROM public;
GRANT ALL ON DATABASE landing_test to data_engineer;

CREATE DATABASE landing_prod;
REVOKE ALL ON DATABASE landing_prod FROM public;
GRANT ALL ON DATABASE landing_prod to data_engineer;

CREATE DATABASE transformation_dev;
REVOKE ALL ON DATABASE transformation_dev FROM public;
GRANT ALL ON DATABASE transformation_dev to data_engineer;

CREATE DATABASE transformation_test;
REVOKE ALL ON DATABASE transformation_test FROM public;
GRANT ALL ON DATABASE transformation_test to data_engineer;

CREATE DATABASE transformation_prod;
REVOKE ALL ON DATABASE transformation_prod FROM public;
GRANT ALL ON DATABASE transformation_prod to data_engineer;

CREATE DATABASE reporting_dev;
REVOKE ALL ON DATABASE reporting_dev FROM public;
GRANT ALL ON DATABASE reporting_dev to data_engineer;

CREATE DATABASE reporting_test;
REVOKE ALL ON DATABASE reporting_test FROM public;
GRANT ALL ON DATABASE reporting_test to data_engineer;

CREATE DATABASE reporting_prod;
REVOKE ALL ON DATABASE reporting_prod FROM public;
GRANT ALL ON DATABASE reporting_prod to data_engineer;

--when schemas are created, remember to grant privileges to data_engineer
