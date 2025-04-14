import sqlite3
import pandas as pd

def run_queries():
    # Connect to the database
    conn = sqlite3.connect("finance.db")
    print("Connected to database successfully!")

    # Query 1: View all transactions
    print("\nQuery 1: All transactions")
    query1 = "SELECT * FROM transactions"
    df1 = pd.read_sql(query1, conn)
    print(df1)

    # Query 2: Total spending by category
    print("\nQuery 2: Total spending by category")
    query2 = """
    SELECT category, SUM(amount) as total
    FROM transactions
    GROUP BY category
    """
    df2 = pd.read_sql(query2, conn)
    print(df2)

    # Query 3: Transactions in a specific date range
    print("\nQuery 3: Transactions between 2025-04-01 and 2025-04-02")
    query3 = """
    SELECT date, description, amount
    FROM transactions
    WHERE date BETWEEN '2025-04-01' AND '2025-04-02'
    """
    df3 = pd.read_sql(query3, conn)
    print(df3)

    # Query 4: Calculate posting delays
    print("\nQuery 4: Transactions with posting delays")
    query4 = """
    SELECT description, amount, (julianday(post_date) - julianday(date)) as posting_delay
    FROM transactions
    """
    df4 = pd.read_sql(query4, conn)
    print(df4)

    # Query 5: Total expenses vs. income
    print("\nQuery 5: Total expenses vs. income")
    query5 = """
    SELECT 
        SUM(CASE WHEN amount < 0 THEN amount ELSE 0 END) as total_expenses,
        SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END) as total_income
    FROM transactions
    """
    df5 = pd.read_sql(query5, conn)
    print(df5)

    # Query 6: Average transaction amount by month
    print("\nQuery 6: Average transaction amount by month")
    query6 = """
    SELECT strftime('%Y-%m', date) as transaction_month, AVG(amount) as avg_amount
    FROM transactions
    GROUP BY transaction_month
    """
    df6 = pd.read_sql(query6, conn)
    print(df6)

    # Query 7: Find transactions with specific keywords
    print("\nQuery 7: Transactions containing 'Starbucks'")
    query7 = """
    SELECT date, description, amount
    FROM transactions
    WHERE description LIKE '%Starbucks%'
    """
    df7 = pd.read_sql(query7, conn)
    print(df7)

    # Query 8: Top 5 largest transactions
    print("\nQuery 8: Top 5 largest transactions")
    query8 = """
    SELECT date, description, amount
    FROM transactions
    ORDER BY ABS(amount) DESC
    LIMIT 5
    """
    df8 = pd.read_sql(query8, conn)
    print(df8)

    # Close the connection
    conn.close()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    run_queries()