import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Load .env file
load_dotenv()

# Read MongoDB URI
Mongo_db_uri = os.getenv("MONGO_DB_URI")

if not Mongo_db_uri:
    raise ValueError("MONGO_DB_URI not found in .env file")

# Create a new client and connect to the server
client = MongoClient(Mongo_db_uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
