import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# ===== Configurable =====
NUM_ROWS = 1000  # ubah jumlah data di sini
OUTPUT_FILE = 'D:\\belajar airflow\\sales-analytics\\data\\transactions.csv'
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 11, 12)
CUSTOMER_COUNT = 50  # jumlah customer unik
TRANSACTION_TYPES = ['deposit', 'withdrawal', 'transfer', 'payment']
# ========================

fake = Faker()

# Generate customer list
customers = [
    {'customer_id': i, 'customer_name': fake.name()}
    for i in range(1, CUSTOMER_COUNT + 1)
]

data = []

for i in range(1, NUM_ROWS + 1):
    customer = random.choice(customers)
    transaction_date = START_DATE + (END_DATE - START_DATE) * random.random()
    transaction_type = random.choice(TRANSACTION_TYPES)
    amount = round(random.uniform(50, 5000), 2)

    data.append({
        'transaction_id': i,
        'customer_id': customer['customer_id'],
        'customer_name': customer['customer_name'],
        'transaction_date': transaction_date.strftime('%Y-%m-%d'),
        'transaction_type': transaction_type,
        'amount': amount
    })

df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)
print(f"Dummy data generated: {NUM_ROWS} rows -> {OUTPUT_FILE}")
