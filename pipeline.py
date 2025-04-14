import pandas as pd
import sqlite3
from datetime import datetime

# Step 1: Read the CSV
def extract_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data extracted successfully!")
        print("Columns in CSV:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return None

# Step 2: Clean the data
def transform_data(df):
    # Check for required columns
    expected_columns = ['Trans Date', 'Post Date', 'Description', 'Amount']
    if not all(col in df.columns for col in expected_columns):
        missing = [col for col in expected_columns if col not in df.columns]
        raise ValueError(f"Missing columns in CSV: {missing}")
    
    # Rename columns to match expected names
    column_mapping = {
        'Trans Date': 'date',
        'Post Date': 'post_date',  # Keep Post Date and rename it
        'Description': 'description',
        'Amount': 'amount'
    }
    df = df.rename(columns=column_mapping)
    
    # Add a placeholder 'category' column since it's missing in the CSV
    df['category'] = 'Uncategorized'
    
    # Convert date and post_date to datetime
    df['date'] = pd.to_datetime(df['date'])
    df['post_date'] = pd.to_datetime(df['post_date'])
    
    # Ensure amount is float
    df['amount'] = df['amount'].astype(float)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    print("Data cleaned successfully!")
    return df

# Step 3: Load into SQLite
def load_data(df, db_name="finance.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    conn.close()
    print("Data loaded into SQLite successfully!")

# Step 4: Analyze data
def analyze_data(db_name="finance.db"):
    conn = sqlite3.connect(db_name)
    # Analyze by category (as before)
    query_by_category = """
    SELECT category, SUM(amount) as total
    FROM transactions
    GROUP BY category
    """
    result_by_category = pd.read_sql(query_by_category, conn)
    
    # Analyze by post_date (e.g., total spending by posting month)
    query_by_post_date = """
    SELECT strftime('%Y-%m', post_date) as post_month, SUM(amount) as total
    FROM transactions
    GROUP BY post_month
    """
    result_by_post_date = pd.read_sql(query_by_post_date, conn)
    
    conn.close()
    
    print("Analysis results (by category):")
    print(result_by_category)
    print("\nAnalysis results (by post month):")
    print(result_by_post_date)
    
    return result_by_category, result_by_post_date

# Main function to run the pipeline
def main():
    file_path = "transactions.csv"
    db_name = "finance.db"
    
    # Extract
    df = extract_data(file_path)
    if df is None:
        return
    
    # Transform
    df_cleaned = transform_data(df)
    
    # Load
    load_data(df_cleaned, db_name)
    
    # Analyze
    analyze_data(db_name)

if __name__ == "__main__":
    main()