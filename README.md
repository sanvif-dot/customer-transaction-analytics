# 🏦 Customer Transaction Analytics

## 📘 Background
In the banking industry, analyzing customer transactions is crucial to understand customer behavior, detect transaction patterns, and support business decision-making.  
This project automates the **ETL (Extract, Transform, Load)** process using **Apache Airflow**, stores the aggregated data in **PostgreSQL**, and visualizes insights through **Metabase** dashboards.

---

## 🎯 Project Objectives
1. **Automate the ETL pipeline** using Apache Airflow for transaction data ingestion and transformation.  
2. **Aggregate customer transactions** and load results into PostgreSQL for further analytics.  
3. **Create an interactive dashboard** in Metabase for business insights.  

---

## 📊 Final Output
- A **`customer_summary`** table in PostgreSQL containing aggregated transaction data per customer and transaction type.  
- A **Metabase dashboard** displaying:
  - Transaction ratio by type (Deposit, Withdrawal, Payment, Transfer)  
  - Top customers by transaction amount  
  - Average and median transaction values  
  - Distribution of transaction sizes  

- Automated ETL execution through the **DAG `customer_transaction_etl_python_only`** in Airflow.

---

## ⚙️ Architecture Overview


## 🚀 How to Run the Project

### 1️⃣ Prerequisites
Make sure you have:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/downloads)

Clone this repository:
```bash
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

### 2️⃣ Start the Containers

docker-compose up -d

This will spin up:

Airflow Webserver → http://localhost:8080
Metabase → http://localhost:3000
PostgreSQL → port 5432

### 3️⃣ Run the Airflow DAG
1. Run script\generate_dummy_transactions.py to produce data\transactions.csv

2. Open the Airflow UI → http://localhost:8080

3. Enable and trigger the DAG customer_transaction_etl

4. Once complete, the transformed data will be available in the customer_summary table.

### 4️⃣ Visualize in Metabase

1 Open Metabase at http://localhost:3000

2 Add a PostgreSQL connection:

Host: metabase-db
Database: metabase
Username: metabase
Password: metabase
port: 5432

Create a new dashboard using the customer_summary table.

🧠 Tech Stack

| Component          | Description                                     |
| ------------------ | ----------------------------------------------- |
| **Apache Airflow** | Workflow orchestration for ETL                  |
| **PostgreSQL**     | Data warehouse for storing analytics results    |
| **pandas**         | Data transformation and aggregation             |
| **SQLAlchemy**     | Database connection and ORM                     |
| **Metabase**       | Business intelligence & dashboard visualization |
| **Docker Compose** | Container orchestration for all services        |
