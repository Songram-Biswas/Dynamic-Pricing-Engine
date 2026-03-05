# from pricing_engine.components.data_ingestion import DataIngestion
# from pricing_engine.entity.config_entity import DataIngestionConfig
# import sys

# if __name__ == "__main__":
#     try:
#         data_ingestion_config = DataIngestionConfig()
#         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#         data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
#         print(data_ingestion_artifact)
#     except Exception as e:
#         print(e)

#just data Ingestion
# from pricing_engine.components.data_ingestion import DataIngestion
# from pricing_engine.components.data_validation import DataValidation
# from pricing_engine.entity.config_entity import DataIngestionConfig, DataValidationConfig

# if __name__ == "__main__":
#     # Ingestion
#     config = DataIngestionConfig()
#     ingestion = DataIngestion(config)
#     artifact = ingestion.initiate_data_ingestion()

#     # Validation
#     val_config = DataValidationConfig()
#     validation = DataValidation(artifact, val_config)
#     validation.initiate_data_validation()

#for Data Validation and Ingestion
# import os
# import sys
# from dotenv import load_dotenv

# # এটি আপনার .env ফাইল থেকে MONGODB_URL লোড করবে
# load_dotenv()
# from pricing_engine.logger import logging
# from pricing_engine.exception import CustomException
# from pricing_engine.components.data_ingestion import DataIngestion
# from pricing_engine.components.data_validation import DataValidation
# from pricing_engine.entity.config_entity import DataIngestionConfig, DataValidationConfig

# if __name__ == "__main__":
#     try:
#         # Step 1: Data Ingestion
#         logging.info("Starting Data Ingestion...")
#         data_ingestion_config = DataIngestionConfig()
#         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
#         data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
#         logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")

#         # Step 2: Data Validation
#         logging.info("Starting Data Validation...")
#         data_validation_config = DataValidationConfig()
#         data_validation = DataValidation(
#             data_ingestion_artifact=data_ingestion_artifact,
#             data_validation_config=data_validation_config
#         )
#         data_validation_artifact = data_validation.initiate_data_validation()
#         logging.info(f"Data Validation Status: {data_validation_artifact}")

#         print("Pipeline executed successfully!")

#     except Exception as e:
#         raise CustomException(e, sys)

import os
import sys
from dotenv import load_dotenv

# .env থেকে MONGODB_URL এবং অন্যান্য ক্রেডেনশিয়াল লোড করা
load_dotenv()

from pricing_engine.logger import logging
from pricing_engine.exception import CustomException

# Components ইমপোর্ট
from pricing_engine.components.data_ingestion import DataIngestion
from pricing_engine.components.data_validation import DataValidation
from pricing_engine.components.data_transformation import DataTransformation
from pricing_engine.components.model_trainer import ModelTrainer

# Entities ইমপোর্ট
from pricing_engine.entity.config_entity import (
    DataIngestionConfig, 
    DataValidationConfig, 
    DataTransformationConfig,
    ModelTrainerConfig
)
# Configuration Manager ইমপোর্ট
from config.configuration import ConfigurationManager
def run_pipeline():
    try:
        config_manager = ConfigurationManager()
        # --- Step 1: Data Ingestion ---
        print("\n" + "="*20 + " DATA INGESTION STARTING " + "="*20)
        logging.info("Starting Data Ingestion Pipeline...")
        
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        
        print(">>> Fetching data from MongoDB Atlas...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        logging.info(f"Data Ingestion completed. Artifact: {data_ingestion_artifact}")
        print(f"✔ Data Ingestion Success! Files saved.")

        # --- Step 2: Data Validation ---
        print("\n" + "="*20 + " DATA VALIDATION STARTING " + "="*20)
        logging.info("Starting Data Validation Pipeline...")
        
        data_validation_config = DataValidationConfig()
        data_validation = DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
        )
        
        print(">>> Validating columns and schema...")
        status = data_validation.initiate_data_validation()
        
        logging.info(f"Data Validation completed. Status: {status}")
        
        if not status:
            print(f"✘ Data Validation Failed! Check logs for details.")
            return # ভ্যালিডেশন ফেইল করলে পাইপলাইন এখানেই থেমে যাবে
        
        print(f"✔ Data Validation Passed!")

        # --- Step 3: Data Transformation ---
        print("\n" + "="*20 + " DATA TRANSFORMATION STARTING " + "="*20)
        logging.info("Starting Data Transformation Pipeline...")

        data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_transformation_config=data_transformation_config
        )
        
        print(">>> Applying Preprocessing (Scaling & Encoding)...")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        
        logging.info(f"Data Transformation completed. Artifact: {data_transformation_artifact}")
        print(f"✔ Data Transformation Success! Preprocessor saved.")
        # --- Step 4: Model Training ---
        print("\n" + "="*20 + " MODEL TRAINING STARTING " + "="*20)
        logging.info("Starting Model Training Pipeline...")

        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact
        )

        print(">>> Training XGBoost and Random Forest Models...")
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info(f"Model Training completed. Best Model R2 Score: {model_trainer_artifact.r2_score}")
        print(f"✔ Model Training Success! Best R2 Score: {model_trainer_artifact.r2_score}")
        
        
        print("\n" + "="*20 + " ALL STEPS COMPLETED SUCCESSFULLY " + "="*20 + "\n")
            
    except Exception as e:
        logging.error(f"Pipeline failed due to: {str(e)}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    run_pipeline()