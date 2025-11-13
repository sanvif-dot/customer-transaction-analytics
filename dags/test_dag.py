from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def say_hello():
    print("Hello Airflow! Pipeline is working ✅")

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="test_hello_world",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",  # <-- diganti dari schedule_interval
    catchup=False,
) as dag:

    task_hello = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello
    )
