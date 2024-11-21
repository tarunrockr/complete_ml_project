from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
import sys

if __name__ == "__main__":

    try: 

        data_ingestion_obj = DataIngestion()
        data_ingestion_obj.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom exception raised")
        raise CustomException(e, sys)
    