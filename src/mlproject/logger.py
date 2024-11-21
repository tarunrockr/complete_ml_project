import os 
from datetime import datetime
import logging

folder_name = f"{datetime.now().strftime('%Y_%m_%d')}"
log_folder_path = os.path.join(os.getcwd(), "logs", folder_name)

if os.path.isdir(log_folder_path) == False:
    os.makedirs(log_folder_path, exist_ok=True)

file_name = f"{datetime.now().strftime('%H_%M_%S')}.log"
log_file_name = os.path.join(log_folder_path, file_name)

logging.basicConfig(
    filename=log_file_name,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)