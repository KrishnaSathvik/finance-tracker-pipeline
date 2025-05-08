import pandas as pd
from random import randint
from datetime import datetime, timedelta

# Load existing transactions
df = pd.read_csv('data/sample_transactions.csv')

# Create 10 fake income entries
income_data = []
start_date = datetime(2020, 6, 1)
for i in range(10):
    income_data.append({
        'Date': (start_date + timedelta(days=i * 20)).strftime('%Y-%m-%d %H:%M:%S'),
        'Description': 'company paycheck',
        'Amount': 3000 + randint(0, 1000),
        'Category': 'salary'
    })

# Convert to DataFrame and append
income_df = pd.DataFrame(income_data)
df = pd.concat([df, income_df], ignore_index=True)

# Save updated data
df.to_csv('data/sample_transactions.csv', index=False)
print("✅ Added fake income rows. You can now re-run the pipeline.")
