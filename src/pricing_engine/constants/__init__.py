import os
from pathlib import Path
from datetime import date

# General Constants
PIPELINE_NAME: str = "pricing"
ARTIFACT_DIR: str = "artifact"

# Database Constants
DATABASE_NAME = "DynamicPricingEngine"
MONGODB_URL_KEY = "MONGODB_URL"

# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME: str = "product_features"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# Data Validation Constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE_NAME: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES: list = ["train.csv", "test.csv"]
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# Data Transformation Constants
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"
PREPROCSSING_OBJECT_FILE_NAME: str = "preprocessor.pkl"
#Model Trainer Constants
CONFIG_FILE_PATH = Path("config/config.yaml")
SCHEMA_FILE_PATH = Path("config/schema.yaml")
# Common File Names
FILE_NAME: str = "pricing_data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"