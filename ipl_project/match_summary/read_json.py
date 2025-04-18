import sys
import os
import json
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger


class ReadJson:
    def __init__(self,file=None):
        self.file=file

    def read_match_file(self,file):
        """Reads all JSON files in the directory and processes match data."""
        process_start=datetime.datetime.now()
        table_name='N/A'
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"season: {data['info']['season']}, match number:{data['info']['event'].get('match_number',0)}")
            if data:
                success_ind = 'Y'  
            else: 
                success_ind = 'N'
                logger.error(f"Failed to read data from {file}")
            process_end=datetime.datetime.now() 
        return data,process_start,success_ind,process_end,table_name
