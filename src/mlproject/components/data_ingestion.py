import sys, os 
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd 
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split 

class DataIngestion:

    def __init__(self):
        self.train_data_path = os.path.join('artifacts', 'train.csv')
        self.test_data_path  = os.path.join('artifacts', 'test.csv')
        self.raw_data_path   = os.path.join('artifacts', 'raw.csv')

    def initiate_data_ingestion(self):
        try:
            # Reading data from mysql 
            df = read_sql_data()
            logging.info("Reading data from mysql database")

            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
            # Storing dataframe as raw.csv file 
            df.to_csv(self.raw_data_path, index=False, header=True)

            # Separating train and test dataset
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            # Storing test dataframe 
            train_set.to_csv(self.train_data_path, index=False, header=True)
            test_set.to_csv(self.test_data_path, index=False, header=True)

            logging.info("Data ingestion is complete.")
            return (
                self.train_data_path,
                self.test_data_path,
                self.raw_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)