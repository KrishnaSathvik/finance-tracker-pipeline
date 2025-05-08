import sys
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Fix import path for src/
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from db import read_all

# --------------------------------------
st.title("📊 Finance Tracker Dashboard")

# --------------------------------------
# 📥 Load from SQLite DB
df = read_all()

# --------------------------------------
# 🧪 Normalize and show preview
df.columns = df.columns.str.strip().str.lower()
st.subheader("🧪 Debug: Raw Data Preview")
st.write("Available columns:", df.columns.tolist())
st.dataframe(df.head())

if 'date' not in df.columns:
    st.error("❌ No valid 'date' column found.")
    st.stop()

df['date'] = pd.to_datetime(df['date'])

# --------------------------------------
# 📅 Month filter
months = df['date'].dt.to_period('M').astype(str).unique()
selected_month = st.selectbox("📅 Select Month", months)
filtered_df = df[df['date'].dt.to_period('M').astype(str) == selected_month]

# 💰 Income/Expense Summary
income = filtered_df[filtered_df['amount'] > 0]['amount'].sum()
expenses = -filtered_df[filtered_df['amount'] < 0]['amount'].sum()
savings = income - expenses

st.metric("Income", f"${income:,.2f}")
st.metric("Expenses", f"${expenses:,.2f}")
st.metric("Savings", f"${savings:,.2f}")

# --------------------------------------
# 📊 Category Breakdown
category_df = (
    filtered_df[filtered_df['amount'] < 0]
    .groupby('category')['amount']
    .sum()
    .abs()
    .reset_index()
    .sort_values(by='amount', ascending=False)
)

st.subheader("📂 Expense Breakdown by Category")
sns.barplot(data=category_df, x='amount', y='category', palette='coolwarm')
plt.xlabel('Amount ($)')
plt.title('Expenses by Category')
st.pyplot(plt)
