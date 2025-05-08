import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('output/monthly_summary.csv')
df['Month'] = pd.to_datetime(df['Month']).dt.strftime('%Y-%m')

# Melt the dataframe to long format
df_melted = df.melt(id_vars='Month', value_vars=['Income', 'Expenses', 'Savings'],
                    var_name='Type', value_name='Amount')

# Plot with seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=df_melted, x='Month', y='Amount', hue='Type')

plt.title('Monthly Income, Expenses & Savings Overview')
plt.xticks(rotation=45)
plt.ylabel('Amount ($)')
plt.xlabel('Month')
plt.legend(title='Type')
plt.tight_layout()
plt.show()
