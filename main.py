from pricing_engine.components.data_ingestion import DataIngestion
from pricing_engine.entity.config_entity import DataIngestionConfig
import sys

if __name__ == "__main__":
    try:
        data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
    except Exception as e:
        print(e)