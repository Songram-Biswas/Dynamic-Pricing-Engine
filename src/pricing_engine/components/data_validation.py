import os
import sys
import pandas as pd
from pathlib import Path
from pricing_engine.logger import logging
from pricing_engine.exception import CustomException
from pricing_engine.entity.config_entity import DataValidationConfig
from pricing_engine.entity.artifact_entity import DataIngestionArtifact
from pricing_engine.utils.common import read_yaml # নিশ্চিত করুন utils এ এটি আছে

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, 
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml(Path("config/schema.yaml"))
        except Exception as e:
            raise CustomException(e, sys)
    def validate_all_columns_exist(self, df: pd.DataFrame) -> bool:
        try:
            validation_status = True
            all_columns = df.columns.tolist()
            
            # schema.yaml থেকে কলামের লিস্টটি নেওয়া
            schema_columns = self._schema_config.columns

            for col in schema_columns:
                if col not in all_columns:
                    validation_status = False
                    logging.error(f"Column [{col}] is missing in the ingested data!")
                else:
                    logging.info(f"Column [{col}] found.")
            
            return validation_status
        except Exception as e:
            raise CustomException(e, sys)
    # def validate_all_columns_exist(self, df: pd.DataFrame) -> bool:
    #     try:
    #         validation_status = True
    #         all_columns = df.columns.tolist()
    #         expected_columns = self._schema_config["columns"]

    #         for column in expected_columns:
    #             col_name = list(column.keys())[0]
    #             if col_name not in all_columns:
    #                 validation_status = False
    #                 logging.error(f"Column {col_name} is missing!")
            
    #         return validation_status
    #     except Exception as e:
    #         raise CustomException(e, sys)

    def initiate_data_validation(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.trained_file_path)
            status = self.validate_all_columns_exist(df=train_df)
            
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file, "w") as f:
                f.write(f"Validation status: {status}")
            
            return status
        except Exception as e:
            raise CustomException(e, sys)