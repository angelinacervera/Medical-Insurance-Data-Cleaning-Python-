# --- PROJECT 3: MULTI-SOURCE PAYROLL RECONCILIATION AUDIT ---
# Objective: Cross-validate external HR disbursements against internal bank records.
# Purpose: Ensure financial integrity and identify potential funding gaps or discrepancies.

def run_payroll_audit():
    # Define file paths within the structured 'raw_data' directory
    gusto_file = 'raw_data/gusto_payroll.csv'
    bank_file = 'raw_data/checking_account_secondary.csv'
    
    # --- PHASE A: DATA INGESTION - HR SYSTEM (GUSTO) ---
    # Establishing the 'Source of Truth' based on authorized payroll reports.
    gusto_total = 0
    try:
        with open(gusto_file, 'r') as f:
            # Skip header row to isolate transactional data
            lines = f.readlines()[1:] 
            for line in lines:
                row = line.strip().split(',')
                # Index 5: 'Amount' column representing Net Pay per employee
                gusto_total += float(row[5])
        print(f"AUDIT LOG: Gusto Authorized Total: ${gusto_total:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to ingest Gusto source data. {e}")
        return

    # --- PHASE B: DATA INGESTION - BANK LEDGER ---
    # Extracting cleared 'Payroll' debits from the Secondary Checking account.
    bank_total = 0
    try:
        with open(bank_file, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                row = line.strip().split(',')
                # Filter for 'Payroll' category (Index 3) to exclude internal transfers
                if row[3] == 'Payroll':
                    # Convert negative bank debits to positive values for reconciliation
                    bank_total += abs(float(row[5]))
        print(f"AUDIT LOG: Bank Disbursement Total: ${bank_total:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to ingest Bank Ledger data. {e}")
        return

    # --- PHASE C: VARIANCE ANALYSIS & RECONCILIATION ---
    # Comparing totals to verify 1:1 agreement between systems.
    print("-" * 45)
    variance = abs(gusto_total - bank_total)
    
    # Implementing a 1-cent tolerance for floating-point rounding
    if variance < 0.01:
        print("RECONCILIATION STATUS: ✅ SUCCESS")
        print("CONCLUSION: Bank records are in full agreement with HR disbursements.")
    else:
        print("RECONCILIATION STATUS: ⚠️ DISCREPANCY DETECTED")
        print(f"TOTAL VARIANCE: ${variance:,.2f}")
        print("INVESTIGATION REQUIRED: Review manual checks or processing fees.")

    print("-" * 45)
    print("Audit Complete. Execution Terminated.")

if __name__ == "__main__":
    run_payroll_audit()
