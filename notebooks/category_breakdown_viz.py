import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load category breakdown
df = pd.read_csv('output/category_breakdown.csv')

# Optional: Sort by amount
df = df.sort_values(by='Amount', ascending=False)

# Plot as bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Amount', y='Category', palette='viridis')
plt.title('💸 Expenses by Category')
plt.xlabel('Amount ($)')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# Optional Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
plt.title('🔍 Expense Distribution by Category')
plt.axis('equal')
plt.tight_layout()
plt.show()
