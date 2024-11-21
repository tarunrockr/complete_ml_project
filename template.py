import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

files_list = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_tranier.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in files_list:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    # If directory does not exists, make all directories
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # If file does not exists the create it 
    if not os.path.exists(filepath):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Created an empty file: {filepath}")

else:
    logging.info(f"{filepath} already exists.")
