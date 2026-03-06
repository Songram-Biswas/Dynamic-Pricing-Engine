import os
import yaml
import sys
from pricing_engine.exception import CustomException
from pricing_engine.logger import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import dill

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")    

def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of common class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of common class")
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path: str) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.dump(file_obj)
    except Exception as e:
        raise CustomException(e, sys)    

import os
import sys
import pickle 
from pricing_engine.exception import CustomException
from pathlib import Path

def load_object(file_path: Path) -> object:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"ফাইলটি পাওয়া যায়নি: {file_path}")
            
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
            
    except Exception as e:
        raise CustomException(e, sys) 