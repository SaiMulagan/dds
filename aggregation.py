from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["yelp_db"]

raw = db["yelp_business_raw"]
city_stats = db["yelp_city_stats"]
category_stats = db["yelp_category_stats"]

# Aggregate by city
city_pipeline = [
    {"$group": {
        "_id": "$city",
        "avg_stars": {"$avg": "$stars"},
        "business_count": {"$sum": 1}
    }}
]

city_results = list(raw.aggregate(city_pipeline))
city_stats.insert_many(city_results)

# Aggregate by category
category_pipeline = [
    {"$project": {
        "categories": {"$split": ["$categories", ", "]},
        "stars": 1
    }},
    {"$unwind": "$categories"},
    {"$group": {
        "_id": "$categories",
        "avg_stars": {"$avg": "$stars"},
        "business_count": {"$sum": 1}
    }}
]

category_results = list(raw.aggregate(category_pipeline))
category_stats.insert_many(category_results)

print("Aggregations stored in MongoDB")