import sqlite3
import pandas as pd

DB_FILE = 'finance.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            amount REAL,
            category TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_transactions(df):
    conn = sqlite3.connect(DB_FILE)
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def read_all():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df
