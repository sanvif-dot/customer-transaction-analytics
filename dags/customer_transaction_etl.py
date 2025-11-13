from __future__ import annotations
import os
from datetime import datetime

from airflow.operators.python import PythonOperator
from airflow.models import DAG

import pandas as pd
from sqlalchemy import create_engine
import psycopg2

DATA_PATH = '/opt/airflow/data/transactions.csv'
POSTGRES_URL = "postgresql+psycopg2://metabase:metabase@metabase-db:5432/metabase"

def create_table():
    conn = psycopg2.connect(
        host="postgres",
        user="airflow",
        password="airflow",
        dbname="airflow",
        port=5432
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customer_summary (
            customer_id INT,
            customer_name TEXT,
            transaction_type TEXT,
            amount NUMERIC
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def transform_load():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"File tidak ditemukan: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    summary = df.groupby(
        ['customer_id','customer_name','transaction_type']
    )['amount'].sum().reset_index()

    engine = create_engine(POSTGRES_URL)
    summary.to_sql('customer_summary', engine, if_exists='replace', index=False)

with DAG(
    dag_id='customer_transaction_etl',
    start_date=datetime(2025, 11, 12),
    schedule=None,
    catchup=False,
    tags=['bank','etl','postgres'],
) as dag:

    create_table_task = PythonOperator(
        task_id='create_table',
        python_callable=create_table
    )

    etl_task = PythonOperator(
        task_id='transform_and_load',
        python_callable=transform_load
    )

    create_table_task >> etl_task
