Data platform for own data etl jobs.

environments:
-dev
-test
-prod


Tools used:
Vagrant (tells which virtual machine to build)
Virtualbox (Virtual machine host, containing the vm)
Airflow (For data flows)
Postgres (database)
Python

Structure is as follows:
1. dataflow folder (etl jobs here)
- Inbound
- Transformation
- Reporting

2. database (database changes here)
-landing
-transformation
-reporting
2. architecture (architecture configs here)

3. tools (python classes)