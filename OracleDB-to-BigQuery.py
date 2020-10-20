"""
Created on October 2020
@author: tarikbahar
tarikbahar.com
"""
import cx_Oracle
import csv
from google.cloud import bigquery
import os


# As a precaution to the following error;
# google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials.
# Locate the GOOGLE APPLICATION CREDENTIALS path.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'


# As a precaution to the following error;
# cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library: "The specified module could not be found". See https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html for help
# Locate the oracle instant client path.
# cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_8")


def getTableFromOracle():
    # Make OracleDB connection
    connection = cx_Oracle.connect("userName", "password", "localhost/XEPDB1")
    cursor = connection.cursor()
    # Create temp csv file
    csv_file = open("temp_oracle2BQ.csv", "w")
    writer = csv.writer(csv_file, delimiter=',',
                        lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)

    # Write SQL Query
    r = cursor.execute("SELECT * FROM --------")
    for row in cursor:
        writer.writerow(row)

    cursor.close()
    connection.close()
    csv_file.close()

    # print("Created CSV File...")

    loadBQ()


def loadBQ():

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "your-project.your_dataset.your_table_name"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True)

    # Read temp CSV file.
    with open("temp_oracle2BQ.csv", "rb") as source_file:
        job = client.load_table_from_file(
            source_file, table_id, job_config=job_config)

    job.result()  # Waits for the job to complete.

    # Make an API request.
    table = client.get_table(table_id)
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(
                table.schema), table_id
        )
    )

    os.remove("temp_oracle2BQ.csv")
    # print("Deleted CSV File...")


getTableFromOracle()
