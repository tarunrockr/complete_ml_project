import sys, os 
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import pandas as pd 
from dotenv import load_dotenv
import pymysql

load_dotenv()
host     = os.getenv('host')
user     = os.getenv('user')
password = os.getenv('password')
db       = os.getenv('db')

def read_sql_data():
    logging.info("Reading from database start.")
    try:
        conn = pymysql.connect(
            host     = host,
            user     = user,
            password = password, 
            db       = db
        )
        logging.info("Connection established: ", conn)

        df = pd.read_sql_query("SELECT * FROM students", conn)
        print(df.head())
        return df

    except Exception as e:
        raise CustomException(e, sys)