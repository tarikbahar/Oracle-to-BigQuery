# Oracle-to-BigQuery
A simple piece of code that enables data transfer from Oracle Db to Google Big Query. Please develop according to your needs. 


My versions of

Oracle Database 18c Express Edition
Oracle sqldeveloper-20.2.0.175.1842-x64
Python 3.6.8 

You may need to run `pip install -r requirements.txt`

and also you have to rewrite some configurations in the code such as 
 - GOOGLE_APPLICATION_CREDENTIALS path
 - cx_Oracle.connect username,password,connection etc.
 - SQL Query
 - A table_id consisting of BQ project,dataset and table name.
