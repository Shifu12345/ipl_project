import os
import requests
import zipfile
import pandas as pd
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dev import configs
from utilities.logging_cust import logger

class Downloader:
    def __init__(self):
        """Initialize the downloader with configurations."""
        self.url = configs.sheets_url
        self.base_dir = configs.base_directory_data
        self.extract_folder = os.path.join(self.base_dir, "ipl_json_files")
        
        # Ensure necessary directories exist
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(self.extract_folder, exist_ok=True)

    def download_file(self):
        """
        Downloads the ZIP file and saves it with a timestamped name.
        
        Returns:
            str: Path to the downloaded ZIP file.
        """
        timestamp = pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
        file_name = f"{configs.zip_file_name}_{timestamp}.zip"
        zip_file_path = os.path.join(self.base_dir, file_name)

        logger.info(f"Downloading {file_name}...")
        response = requests.get(self.url, stream=True)

        with open(zip_file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        logger.info(f"File downloaded successfully to {zip_file_path}")
        
        return zip_file_path,'Y'

    def extract_zip(self, zip_file_path):
        """
        Extracts the contents of the ZIP file, only if the files do not already exist.
        
        Args:
            zip_file_path (str): Path to the downloaded ZIP file.
        """
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            all_files = zip_ref.namelist()
            
            # Check if all files already exist in the extraction folder
            if all(os.path.exists(os.path.join(self.extract_folder, f)) for f in all_files):
                logger.info(f"All files already exist in {self.extract_folder}. Skipping extraction.")
            else:
                logger.info(f"Extracting files to {self.extract_folder}...")
                zip_ref.extractall(self.extract_folder)
                logger.info("Extraction complete.")

    def downloader_and_extract(self):
        """
        Executes the full process: downloading and extracting.
        """
        zip_file_path,success_ind = self.download_file()
        self.extract_zip(zip_file_path)
        
        return success_ind
