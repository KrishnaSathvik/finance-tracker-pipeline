def generate_monthly_summary(df):
    df['Month'] = df['Date'].dt.to_period('M').astype(str)  # ✅ Convert to string
    summary = df.groupby('Month')['Amount'].agg([
        ('Income', lambda x: x[x > 0].sum()),
        ('Expenses', lambda x: -x[x < 0].sum()),
        ('Savings', lambda x: x.sum())
    ]).reset_index()
    return summary

def category_breakdown(df):
    return df[df['Amount'] < 0].groupby('Category')['Amount'].sum().abs().sort_values(ascending=False).reset_index()

