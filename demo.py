# import sys
# from pricing_engine.logger import logging
# from pricing_engine.exception import CustomException

# try:
#     logging.info("Testing the logging setup...")
#     result = 10 / 0
# except Exception as e:
#     raise CustomException(e, sys)
import os
import sys
from dotenv import load_dotenv

# .env লোড করা
load_dotenv()

from pricing_engine.logger import logging
from pricing_engine.exception import CustomException
from pricing_engine.entity.config_entity import DataIngestionConfig
from pricing_engine.components.data_ingestion import DataIngestion

def start_ingestion():
    try:
        logging.info("Starting Data Ingestion Pipeline...")
        
        # ১. কনফিগারেশন সেটআপ
        config = DataIngestionConfig()
        
        # ২. ইনজেশন প্রসেস শুরু (এটিই ডাটা ডাউনলোড এবং ফোল্ডার তৈরি করবে)
        ingestion = DataIngestion(data_ingestion_config=config)
        artifact = ingestion.initiate_data_ingestion()
        
        logging.info(f"Ingestion complete. Files saved at: {artifact.trained_file_path}")
        print("Successfully created 'artifact' folder with Train/Test data!")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    start_ingestion()