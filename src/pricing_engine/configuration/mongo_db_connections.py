import pymongo
import os
import sys
import certifi
from pricing_engine.constants import DATABASE_NAME, MONGODB_URL_KEY
from pricing_engine.logger import logging
from pricing_engine.exception import CustomException

ca = certifi.where()

class MongoDBConnection:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBConnection.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                
                MongoDBConnection.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            
            self.client = MongoDBConnection.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
            
        except Exception as e:
            raise CustomException(e, sys)