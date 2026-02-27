import os
from datetime import date

# Database Constants
DATABASE_NAME = "DynamicPricingEngine"
COLLECTION_NAME = "product_features"
MONGODB_URL_KEY = "MONGODB_URL"

# Pipeline and Artifact Constants
PIPELINE_NAME: str = "pricing"
ARTIFACT_DIR: str = "artifact"

# Data Ingestion Constants
DATA_INGESTION_COLLECTION_NAME: str = "product_features"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# File Names
FILE_NAME: str = "pricing_data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"