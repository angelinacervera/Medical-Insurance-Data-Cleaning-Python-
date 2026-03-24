# --- PROJECT 4: INTER-ACCOUNT EXPENSE RECONCILIATION ---
# Objective: Audit the flow of capital between the Main Operating account and Credit Liabilities.
# Purpose: Ensure all initiated debt payments were successfully acknowledged by the lender.

def run_expense_audit():
    # File paths pointing to the centralized 'raw_data' repository
    main_account = 'raw_data/checking_account_main.csv'
    credit_card = 'raw_data/credit_card_account.csv'
    
    # --- PHASE A: DISBURSEMENT VALIDATION (MAIN BANK) ---
    # Aggregating all outbound capital specifically coded as 'Credit Card Payment'.
    outbound_payments = 0
    try:
        with open(main_account, 'r') as f:
            # Isolate transactional data by skipping header
            for line in f.readlines()[1:]:
                row = line.strip().split(',')
                # Filter for specific payment category (Index 3)
                if row[3] == 'Credit Card Payment':
                    # Normalize negative bank debits to positive floats for audit comparison
                    outbound_payments += abs(float(row[5]))
        print(f"AUDIT LOG: Main Bank - Total Payments Sent: ${outbound_payments:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to access Main Bank ledger. {e}")
        return

    # --- PHASE B: LENDER ACKNOWLEDGMENT (CREDIT CARD) ---
    # Verifying that the creditor received and applied the reported funds to the balance.
    inbound_credits = 0
    try:
        with open(credit_card, 'r') as f:
            for line in f.readlines()[1:]:
                row = line.strip().split(',')
                # Validate 'Payment' type entries (Index 4) on the CC statement
                if row[4] == 'Payment':
                    inbound_credits += float(row[5])
        print(f"AUDIT LOG: Credit Card - Total Credits Applied: ${inbound_credits:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to access Credit Card statement. {e}")
        return

    # --- PHASE C: VARIANCE ANALYSIS ---
    # Final check for 1:1 agreement between the bank's 'Money Out' and the lender's 'Money In'.
    print("-" * 45)
    variance = abs(outbound_payments - inbound_credits)
    
    # 0.01 tolerance accounts for potential floating-point rounding variances
    if variance < 0.01:
        print("RECONCILIATION STATUS: ✅ SUCCESS")
        print("CONCLUSION: Internal ledgers and lender statements are in full agreement.")
    else:
        print("RECONCILIATION STATUS: ⚠️ DISCREPANCY DETECTED")
        print(f"UNRECONCILED VARIANCE: ${variance:,.2f}")
        print("ACTION: Investigate potential 'In-Flight' payments or processing delays.")

    print("-" * 45)
    print("Expense Audit Process Terminated.")

if __name__ == "__main__":
    run_expense_audit()
