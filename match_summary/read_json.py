import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger
# Add the project root to sys.path



class ReadJson:
    def __init__(self, file):
        self.file = file

    def read_match_file(self):
        """Reads all JSON files in the directory and processes match data."""
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info(f"{self.file}, season: {data['info']['season']}, match number:{data['info']['event'].get('match_number',0)}")
                    
        return data
