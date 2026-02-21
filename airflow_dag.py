from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def placeholder():
    print("Airflow DAG placeholder for Yelp pipeline")

with DAG(
    dag_id="yelp_mongodb_pipeline",
    start_date=datetime(2026, 2, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="load_data",
        python_callable=placeholder
    )

    task2 = PythonOperator(
        task_id="run_aggregations",
        python_callable=placeholder
    )

    task1 >> task2