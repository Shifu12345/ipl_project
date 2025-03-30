import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# import logging

from utilities.logging_cust import logger

class LocalWriter:
    def __init__(self):
        pass
    
    def csv_writer_local(self, df, path):
        df.to_csv(path)
        return f"dataframe written to {path} in csv"
    
    def parquet_writer_local(self, df, path):
        """
        Writes a DataFrame to a Parquet file, partitioned by season.

        Parameters:
        df (pd.DataFrame): The DataFrame to be written.
        path (str): The base directory where the Parquet files should be stored.

        Returns:
        str: Confirmation message.
        """
        partition_col = "season"

        # Ensure the path exists
        os.makedirs(path, exist_ok=True)

        # Write the DataFrame partitioned by season
        df.to_parquet(path, partition_cols=[partition_col], engine='pyarrow', index=False)

        return f"DataFrame written to {path}, partitioned by {partition_col}"
        