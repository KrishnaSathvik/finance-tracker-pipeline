import pandas as pd

def auto_categorize(description):
    description = description.lower()
    
    if any(word in description for word in ['starbucks', 'coffee', 'mcdonald', 'restaurant', 'food']):
        return 'Food'
    elif any(word in description for word in ['uber', 'lyft', 'taxi', 'gas', 'shell']):
        return 'Transport'
    elif any(word in description for word in ['netflix', 'spotify', 'subscription']):
        return 'Entertainment'
    elif any(word in description for word in ['walmart', 'target', 'amazon']):
        return 'Shopping'
    elif any(word in description for word in ['rent', 'mortgage', 'lease']):
        return 'Housing'
    elif any(word in description for word in ['salary', 'paycheck', 'deposit']):
        return 'Salary'
    elif any(word in description for word in ['gym', 'health', 'clinic', 'doctor']):
        return 'Health'
    else:
        return 'Other'

def clean_transactions(df):
    df['Description'] = df['Description'].str.strip().str.lower()
    df['Category'] = df['Category'].fillna('Uncategorized')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)

    # 🧠 Auto-categorize if missing or 'Uncategorized'
    df['Category'] = df.apply(
        lambda row: row['Category'] if pd.notnull(row['Category']) and row['Category'] != 'Uncategorized' 
        else auto_categorize(row['Description']), axis=1
    )

    # 💸 Make expenses negative
    income_categories = ['income', 'salary', 'deposit']
    df['Amount'] = df.apply(
        lambda row: row['Amount'] if row['Category'].lower() in income_categories else -row['Amount'],
        axis=1
    )
    
    return df
