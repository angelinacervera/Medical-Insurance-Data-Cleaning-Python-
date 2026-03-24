import pandas as pd

# 1. Load the dataset (Assuming you upload the CSV to the same folder)
# For now, we'll use a placeholder name
file_name = 'coffee_shop_data.csv' 

try:
    df = pd.read_csv(file_name)
    print("Dataset loaded successfully!\n")

    # 2. Cleaning Logic: Standardize Column Names
    # This makes it easier to reference columns later
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # 3. Cleaning Logic: Currency to Float
    # If the CSV has "$" or "," in the price, we strip them and convert to float
    if 'transaction_amount' in df.columns:
        df['transaction_amount'] = df['transaction_amount'].replace('[\$,]', '', regex=True).astype(float)

    # 4. Analysis: Applying your previous logic at scale
    total_revenue = df['transaction_amount'].sum()
    avg_transaction = df['transaction_amount'].mean()

    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Average Transaction: ${avg_transaction:,.2f}")

except FileNotFoundError:
    print("Please upload the 'coffee_shop_data.csv' file to this folder to run the analysis.")
