# --- PROJECT: COFFEE SHOP FINANCIAL LEDGER ANALYSIS ---
# Purpose: Clean and categorize bank transaction data to calculate Net Profit and Margin.
# This script demonstrates manual string manipulation and business logic application.

file_name = 'raw_data/checking_account_main.csv'

try:
    with open(file_name, 'r') as file:
        raw_data = file.readlines()

    # Skip header and isolate transaction rows
    header = raw_data[0].strip().split(',')
    data_rows = raw_data[1:]

    # 1. DATA CLEANING & TYPE CONVERSION
    clean_records = []
    for line in data_rows:
        row = [item.strip() for item in line.split(',')]
        
        # Clean currency string in Column F (Index 5) and cast to float
        row[5] = float(row[5].replace('$', '').replace(',', ''))
        clean_records.append(row)

    # 2. FINANCIAL LOGIC (CREDITS VS. DEBITS)
    total_revenue = 0
    total_expenses = 0
    
    for record in clean_records:
        amount = record[5]
        transaction_type = record[4] # Column E identifies the nature of the transaction
        
        if transaction_type == 'Credit':
            total_revenue += amount
        elif transaction_type == 'Debit':
            total_expenses += amount

    # 3. CALCULATING KEY BUSINESS METRICS
    net_profit = total_revenue - total_expenses
    
    # Calculate Profit Margin Percentage: (Net Profit / Revenue) * 100
    if total_revenue > 0:
        profit_margin = (net_profit / total_revenue) * 100
    else:
        profit_margin = 0

    # 4. REPORT GENERATION
    print(f"--- FINANCIAL SUMMARY: {file_name} ---")
    print(f"Transactions Processed: {len(clean_records)}")
    print(f"Gross Revenue (Credits):  ${total_revenue:,.2f}")
    print(f"Total Operating Costs:    ${total_expenses:,.2f}")
    print(f"----------------------------------------")
    print(f"NET PROFIT / (LOSS):      ${net_profit:,.2f}")
    print(f"PROFIT MARGIN:            {profit_margin:.2f}%")

except FileNotFoundError:
    print(f"Critical Error: Source file '{file_name}' missing from directory.")}' missing from directory.")
