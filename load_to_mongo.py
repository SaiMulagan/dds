import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["yelp_db"]
collection = db["yelp_business_raw"]

with open("yelp_academic_dataset_business.json", "r") as f:
    for line in f:
        doc = json.loads(line)
        collection.insert_one(doc)

print("Loaded Yelp business data into MongoDB")