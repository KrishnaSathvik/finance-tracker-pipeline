
# 💰 Finance Tracker Pipeline

A powerful and user-friendly personal finance tracking system that processes, analyzes, and visualizes financial transactions using Python, SQLite, and Streamlit.

---

## 🚀 Features

- 🧾 Ingests CSV-based financial transaction data
- 🔄 Cleans and standardizes transaction formats
- 🧠 Auto-categorizes expenses (food, transport, shopping, etc.)
- 💾 Saves transactions to a local SQLite database
- 📊 Generates monthly summaries and category breakdowns
- 🌐 Interactive dashboard built with Streamlit

---

## 🛠️ Tech Stack

- Python 3.10+
- Pandas
- Matplotlib / Seaborn
- SQLite (via sqlite3)
- Streamlit (for dashboard)

---

## 📁 Project Structure

```
finance-tracker-pipeline/
├── data/
│   └── sample_transactions.csv
├── src/
│   ├── main.py
│   ├── ingest.py
│   ├── transform.py
│   ├── analyze.py
│   └── db.py
├── output/
│   ├── monthly_summary.csv
│   └── category_breakdown.csv
├── dashboard.py
├── README.md
└── requirements.txt
```

---

## 🧠 How It Works

1. **Data Ingestion**: Reads transactions from a CSV file.
2. **Transformation**: Cleans descriptions, standardizes dates, detects income vs expenses.
3. **Auto Categorization**: Uses keywords to classify transactions into categories like 'Food', 'Transport', 'Shopping', etc.
4. **SQLite Storage**: Saves all transactions into `finance.db` for persistence.
5. **Streamlit Dashboard**: Offers an interactive UI to filter by month, visualize spending, and track savings.

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/KrishnaSathvik/finance-tracker-pipeline.git
cd finance-tracker-pipeline
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline

```bash
python src/main.py
```

This will:
- Load transactions from CSV
- Clean and categorize them
- Generate `monthly_summary.csv` and `category_breakdown.csv`
- Store them into SQLite

---

## 📊 Run the Dashboard

```bash
streamlit run dashboard.py
```

You’ll see:
- Income, expenses, savings per month
- Category-wise bar chart
- Monthly filter dropdown

---

## 🔒 SQLite Access

Database file: `finance.db`

To query manually:

```sql
SELECT * FROM transactions;
```

---

## 📈 Future Improvements

- [ ] Add full-text search to the dashboard
- [ ] Upload new CSVs via the UI
- [ ] Add export buttons (CSV/PDF)
- [ ] Multi-user login + personalization

---

> Built with 💙 by [Krishna Sathvik](https://github.com/KrishnaSathvik)
