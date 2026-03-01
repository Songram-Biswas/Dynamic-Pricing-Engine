import os
import sys
from pricing_engine.logger import logging
from pricing_engine.exception import CustomException
from pricing_engine.entity.config_entity import DataIngestionConfig
from pricing_engine.entity.artifact_entity import DataIngestionArtifact
from pricing_engine.data_access.pricing_data import PricingData
from sklearn.model_selection import train_test_split
from pandas import DataFrame

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """
        MongoDB Atlas থেকে ডাটা ফেচ করে ফিচার স্টোর হিসেবে সেভ করা।
        """
        try:
            logging.info("Exporting data from MongoDB to feature store")
            pricing_data = PricingData()
            dataframe = pricing_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )
            
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
            
        except Exception as e:
            raise CustomException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        ডাটাফেচ করার পর সেটিকে ট্রেন এবং টেস্ট সেটে ভাগ করা।
        """
        try:
            logging.info("Performing train-test split")
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            
            logging.info("Exported train and test file paths")
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            return data_ingestion_artifact
            
        except Exception as e:
            raise CustomException(e, sys)