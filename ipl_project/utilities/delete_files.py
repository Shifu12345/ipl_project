import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger


class DeleteFiles:
    def __init__(self):
        pass

    def remove_zip_files(self,folder_path):
        """
        Removes all .zip files from the specified folder.

        Args:
            folder_path (str): The folder where zip files should be deleted.

        Returns:
            list: A list of deleted zip files.
        """
        if not os.path.isdir(folder_path):
            logger.info(f"Folder '{folder_path}' does not exist or is not a directory.")
            return []

        zip_files = [f for f in os.listdir(folder_path) if f.endswith(".zip")]

        if not zip_files:
            logger.info("No .zip files found to remove.")
            return []

        deleted_files = []
        for zip_file in zip_files:
            zip_path = os.path.join(folder_path, zip_file)
            try:
                os.remove(zip_path)
                logger.info(f"Removed: {zip_file}")
                deleted_files.append(zip_file)
            except Exception as e:
                logger.error(f"Error removing {zip_path}: {e}")

        return deleted_files


