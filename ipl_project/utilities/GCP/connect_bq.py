from google.oauth2 import service_account
from google.cloud import bigquery
import pandas_gbq as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dev import configs


class PythonGCPConnect:
    def __init__(self,service_account_json):
        self.service_account_json=service_account_json
    
    def get_client(self):    
        service_account_path = self.service_account_json
        self.credentials = service_account.Credentials.from_service_account_file(service_account_path)
        
        client = bigquery.Client(
            credentials=self.credentials, 
            project=self.credentials.project_id
            )
        return client
        
    def connect_to_bq(self,df,dataset,table,schema):
        # Initialize BigQuery client
        client= self.get_client()

        # Define BigQuery dataset & table
        dataset_id = dataset
        table_id = table

        # Define full table reference
        table_ref = f"{self.credentials.project_id}.{dataset_id}.{table_id}"
        
        if table_id not in ['audit_table','file_audit_table','process_audit_table'] :
            write_disposition='WRITE_TRUNCATE'
        else :
            write_disposition='WRITE_APPEND'
        # Upload DataFrame to BigQuery
        load_df_job = client.load_table_from_dataframe(df, 
                                               table_ref,
                                               job_config=bigquery.LoadJobConfig(schema=schema,
                                                                                 write_disposition=write_disposition)
                                               )
        load_df_job.result()  # Wait for the job to complete

        print(f" Data uploaded successfully to {table_ref}")
        
    def increment_run_number(self,run_number):

        prefix = ''.join(filter(str.isalpha, run_number))   # Extracts "IPL"
        number = ''.join(filter(str.isdigit, run_number))   # Extracts "00001"
        
        new_number = int(number) + 1                        # Increment the number
        number_width = len(number)                          # Preserve original number length
        
        return f"{prefix}{new_number:0{number_width}d}"    
        
    def process_audit_run_number_query(self):
        
        client=self.get_client()
        result=client.query(f'''
                     select max(run_number) as run_number 
                     from `{configs.gcp_project_name}.{configs.dataset}.{configs.process_audit_table}`
                     ''').result()
        
        for row in result:
            latest_run_number = row.run_number
        
        run_number=self.increment_run_number(latest_run_number)
        
        return  run_number
    
    def get_files_processed(self):

        # Initialize the BigQuery client
        client = self.get_client()

        # Define your query
        query = f"""
            SELECT file_name,processed_flag
            FROM `{configs.gcp_project_name}.{configs.dataset}.{configs.file_audit_table}`
        """

        # Run the query
        query_job = client.query(query)

        # Convert results to list
        result_list = [row.file_name for row in query_job if row.processed_flag == 'Y']

        return result_list

    
    
            
        
        
