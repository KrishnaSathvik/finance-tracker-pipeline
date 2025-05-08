import pandas as pd
import matplotlib.pyplot as plt

# Load the monthly summary
df = pd.read_csv('output/monthly_summary.csv')
df['Month'] = pd.to_datetime(df['Month'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Income'], marker='o', label='Income')
plt.plot(df['Month'], df['Expenses'], marker='o', label='Expenses')
plt.plot(df['Month'], df['Savings'], marker='o', label='Savings')

plt.title('Monthly Financial Summary')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
