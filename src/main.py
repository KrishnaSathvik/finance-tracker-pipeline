from ingest import load_transactions
from transform import clean_transactions
from analyze import generate_monthly_summary, category_breakdown
from db import init_db, insert_transactions


INPUT_FILE = 'data/sample_transactions.csv'
OUTPUT_FILE = 'output/monthly_summary.csv'
CATEGORY_FILE = 'output/category_breakdown.csv'

def main():
    # Step 1: Load and clean data
    df = load_transactions(INPUT_FILE)
    df = clean_transactions(df)

    # Step 2: Analyze data
    summary = generate_monthly_summary(df)
    category = category_breakdown(df)

    # Step 3: Save reports
    print(summary.to_string(index=False))
    summary.to_csv(OUTPUT_FILE, index=False)
    category.to_csv(CATEGORY_FILE, index=False)

    # Step 4: Store in SQLite
    init_db()
    insert_transactions(df)

if __name__ == "__main__":
    main()
