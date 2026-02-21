MSDS 697 – Task 2 Mid Project Checkpoint  
Airflow and MongoDB  

Dataset  
Yelp Academic Dataset – Business JSON  

Current Status  
The Yelp business dataset was uploaded to Google Cloud Storage and imported into MongoDB as a raw collection. Initial analytics and aggregation tasks were performed to generate derived datasets. Aggregated results were stored in separate MongoDB collections. Queries were executed on both the original and aggregated data using MongoDB queries and SparkSQL.

MongoDB Collections  
- yelp_business_raw  
- yelp_city_stats  
- yelp_category_stats  

Aggregations Created  
1. Average star rating and total business count per city  
2. Average star rating and business count per category  

Next Steps  
- Integrate full Airflow DAG execution  
- Expand aggregations to include review trends  
- Add indexing and performance tuning in MongoDB  