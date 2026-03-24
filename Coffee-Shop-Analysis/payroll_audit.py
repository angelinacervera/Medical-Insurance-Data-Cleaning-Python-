# --- PROJECT 3: MULTI-SOURCE PAYROLL RECONCILIATION AUDIT ---
# Objective: Validate HR Payroll disbursements (Gusto) against Bank Ledger outflows.
# Purpose: Identify discrepancies, rounding errors, or unauthorized transactions.

def run_payroll_audit():
    # File configuration for internal and external data sources
    gusto_file = 'gusto_payroll.csv'
    bank_file = 'checking_account_secondary.csv'
    
    # --- PHASE A: HR SYSTEM AGGREGATION (GUSTO) ---
    # We treat the Gusto export as the "Source of Truth" for authorized pay.
    gusto_total = 0
    try:
        with open(gusto_file, 'r') as f:
            # Skip header to isolate raw transactional values
            lines = f.readlines()[1:] 
            for line in lines:
                row = line.strip().split(',')
                # Index 5 maps to 'Net Pay' amount in the Gusto schema
                gusto_total += float(row[5])
        print(f"REPORT: Gusto Authorized Total: ${gusto_total:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Unable to parse Gusto source file. {e}")
        return # Exit audit if source of truth is unavailable

    # --- PHASE B: BANK LEDGER VERIFICATION ---
    # We cross-reference the Checking Secondary account for matching 'Payroll' debits.
    bank_total = 0
    try:
        with open(bank_file, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                row = line.strip().split(',')
                # Filter for 'Payroll' category (Index 3) to exclude transfers/fees
                if row[3] == 'Payroll':
                    # Using abs() to convert Bank Debits (negative) to positive values for comparison
                    bank_total += abs(float(row[5]))
        print(f"REPORT: Bank Disbursement Total: ${bank_total:,.2f}")
    except Exception as e:
        print(f"CRITICAL ERROR: Bank ledger access failed. {e}")
        return

    # --- PHASE C: DISCREPANCY ANALYSIS & TERMINATION ---
    print("-" * 40)
    
    # Define a 1-cent tolerance for floating-point rounding issues
    variance = abs(gusto_total - bank_total)
    
    if variance < 0.01:
        print("AUDIT STATUS: ✅ SUCCESS")
        print("RESULT: Internal Bank records are in 100% agreement with HR reporting.")
    else:
        print("AUDIT STATUS: ⚠️ DISCREPANCY DETECTED")
        print(f"VARIANCE: ${variance:,.2f}")
        print("ACTION: Manual review of Payroll Funding vs. Employee Net Pay required.")

    print("-" * 40)
    print("Audit Log Finalized. Process Terminated.")

if __name__ == "__main__":
    run_payroll_audit()
