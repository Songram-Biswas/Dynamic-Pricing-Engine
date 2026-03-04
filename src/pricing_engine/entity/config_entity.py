import os
from dataclasses import dataclass
from pricing_engine.constants import *

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(ARTIFACT_DIR, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name: str = DATA_INGESTION_COLLECTION_NAME

from dataclasses import dataclass, field # field ইমপোর্ট করুন

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(ARTIFACT_DIR, "data_validation")
    valid_status_file: str = os.path.join(data_validation_dir, "status.txt")
    report_file_path: str = os.path.join(data_validation_dir, "report.yaml")    
# @dataclass
# class DataValidationConfig:
#     data_validation_dir: str = os.path.join(ARTIFACT_DIR, DATA_VALIDATION_DIR_NAME)
#     validation_report_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_REPORT_FILE_NAME)
#     status_file_path: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE_NAME)
#     all_required_files: list = DATA_VALIDATION_ALL_REQUIRED_FILES

@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(ARTIFACT_DIR, DATA_TRANSFORMATION_DIR_NAME)
    transformed_train_file_path: str = os.path.join(
        data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, 
        TRAIN_FILE_NAME.replace("csv", "npy")
    )
    transformed_test_file_path: str = os.path.join(
        data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, 
        TEST_FILE_NAME.replace("csv", "npy")
    )
    transformed_object_file_path: str = os.path.join(
        data_transformation_dir, DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
        PREPROCSSING_OBJECT_FILE_NAME
    )