# import os
# import sys
# from pathlib import Path
# from pricing_engine.constants import *
# from pricing_engine.utils.common import read_yaml, create_directories
# from pricing_engine.entity.config_entity import (DataIngestionConfig, 
#                                                 DataValidationConfig, 
#                                                 DataTransformationConfig,
#                                                 ModelTrainerConfig) # এটি যোগ করুন

# class ConfigurationManager:
#     def __init__(self, config_filepath=CONFIG_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
#         self.config = read_yaml(config_filepath)
#         self.schema = read_yaml(schema_filepath)
#         create_directories([self.config.artifacts_root])

#     # ... আপনার অন্যান্য মেথডগুলো (get_data_ingestion_config ইত্যাদি) এখানে থাকবে ...

#     def get_model_trainer_config(self) -> ModelTrainerConfig:
#         try:
#             config = self.config.model_trainer
            
#             create_directories([config.root_dir])

#             model_trainer_config = ModelTrainerConfig(
#                 root_dir=Path(config.root_dir),
#                 trained_model_file_path=Path(config.trained_model_file_path),
#                 base_accuracy=config.base_accuracy
#             )

#             return model_trainer_config
#         except Exception as e:
#             raise e
import os
import sys
from pathlib import Path
from pricing_engine.constants import *
from pricing_engine.utils.common import read_yaml, create_directories
from pricing_engine.entity.config_entity import (DataIngestionConfig, 
                                                DataValidationConfig, 
                                                DataTransformationConfig,
                                                ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            mongodb_url=os.getenv("MONGODB_URL"),
            database_name=config.database_name,
            collection_name=config.collection_name,
            local_data_file=config.local_data_file
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.columns

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            config = self.config.model_trainer
            
            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                root_dir=Path(config.root_dir),
                trained_model_file_path=Path(config.trained_model_file_path),
                base_accuracy=config.base_accuracy
            )

            return model_trainer_config
        except Exception as e:
            raise e