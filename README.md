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
![dashboard](https://github.com/user-attachments/assets/8c75864a-e131-46b5-80ed-71a63f279045)


- Automated ETL execution through the **DAG `customer_transaction_etl_python_only`** in Airflow.

---


📊 Dashboard Insights
1️⃣ Transaction Ratio by Type

Purpose: To understand how different transaction types (Deposit, Withdrawal, Payment, Transfer) contribute to overall transaction activity.
Insight:

Each type represents roughly 25% of all transactions, showing a balanced usage across transaction categories.

This indicates customers engage evenly in saving, spending, and fund transfer activities — useful for identifying behavioral balance among account holders.

2️⃣ Top Customers by Transaction Amount

Purpose: To identify customers with the highest total transaction volume.
Insight:

The top five customers (e.g., Jonathan Gentry, Roberto Goodwin) contribute a significant portion of total transaction volume.

This helps the bank focus retention and cross-sell strategies on high-value customers and monitor large transaction accounts for compliance.

3️⃣ Average and Median Transaction Values

Purpose: To summarize overall customer spending and inflow/outflow behavior.
Insight:

Average transaction value: ≈ 12,876

Median transaction value: ≈ 12,365

The close gap between mean and median indicates a fairly balanced distribution with few extreme outliers, suggesting consistent transaction patterns across customers.

4️⃣ Distribution of Transaction Sizes

Purpose: To segment transactions into size ranges for better understanding of customer activity levels.
Segments:

Low (<10K)

Medium (10K–20K)

High (>20K)

Insight:

The Medium (10K–20K) range dominates, indicating most customers perform moderate-sized transactions.

High-value transactions (>20K) form a smaller but significant portion — often representing high-income or corporate clients.

5️⃣ Transaction Ratio: Inflow vs Outflow

Purpose: To analyze the direction of money movement in the system.

Inflow: Deposits + Transfers

Outflow: Withdrawals + Payments

Insight:

Outflow accounts for 67.1%, while Inflow is 32.9%, suggesting customers are spending or transferring more funds than they deposit.

This imbalance could indicate increased payment activity, lending opportunities, or seasonal spending behavior.

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
