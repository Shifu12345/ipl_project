from google.cloud import bigquery
from google.oauth2 import service_account
import datetime
import sys
import os
import pandas as pd


# Load credentials and initialize BigQuery client
def initiate_audit_table(serv):
    service_account_path =  serv # Update this
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    # Define the table reference
    table_id = "synthetic-style-439016-b9.ipl.process_audit_table"

    # Create a row to insert
    rows_to_insert = [
        {
            "run_number": "IPL00001",
            "process_start": datetime.datetime.now().isoformat(),  # Current timestamp
            "file_name": "N/A",
            "process_name": "N/A",
            "table_name": "N/A",
            "records_added": 0,
            "success_ind": "Y",
            "process_end": datetime.datetime.now().isoformat(),  # Current timestamp
        }
    ]
    
    df=pd.DataFrame(rows_to_insert)
    
    df["run_number"] = df["run_number"].astype(str)
    df["process_start"] = pd.to_datetime(df["process_start"])  # Ensure TIMESTAMP format
    df["file_name"] = df["file_name"].astype(str)
    df["process_name"] = df["process_name"].astype(str)
    df["table_name"] = df["table_name"].astype(str)
    df["records_added"] = df["records_added"].astype(int)  # Ensure INTEGER format
    df["success_ind"] = df["success_ind"].astype(str)
    df["process_end"] = pd.to_datetime(df["process_end"])  
        # Insert the row(s) into BigQuery
    errors =  client.load_table_from_dataframe(df, table_id, job_config=bigquery.LoadJobConfig(), location="US")


    # Check for errors
    if errors:
        print("Errors occurred while inserting data:", errors)
    else:
        print("Data inserted successfully into", table_id)

initiate_audit_table("E:\\Sivadatt K\\ipl_json\\bq_files_and_py\\synthetic-style-439016-b9-3f5b87717517.json")
