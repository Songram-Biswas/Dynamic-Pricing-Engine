import sys
import pandas as pd
import numpy as np
from pricing_engine.configuration.mongo_db_connections import MongoDBConnection
from pricing_engine.exception import CustomException

class PricingData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBConnection()
        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: str = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client.client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e, sys)