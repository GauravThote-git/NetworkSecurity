from networksecurity.logging.logger import logger
from networksecurity.exception.exception import NetworkSecurityException
import pymongo
import numpy as np
import pandas as pd
import certifi
import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
print(MONGO_DB_URI)

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            # Connect once
            mongo_client = pymongo.MongoClient(MONGO_DB_URI)

            # Step 1: Get database
            db = mongo_client[database]

            # Step 2: Get collection (⚠️ FROM DATABASE, NOT CLIENT)
            col = db[collection]

            # Step 3: Insert records
            result = col.insert_many(records)

            return len(result.inserted_ids)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "GauravAI"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(
        records=records, database=DATABASE, collection=Collection)
    print(no_of_records)
