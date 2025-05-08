import pandas as pd

def load_transactions(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        df = df[['Date', 'Description', 'Amount', 'Category']].copy()
        return df
    except Exception as e:
        raise ValueError(f"Failed to load transactions: {e}")
