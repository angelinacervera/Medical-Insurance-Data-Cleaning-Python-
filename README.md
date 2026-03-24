# Professional Data Engineering Portfolio
A collection of Python projects focused on transforming messy, real-world data into actionable business insights through manual string manipulation and structured analysis.

---

## Project 4: Inter-Account Expense Reconciliation
This project demonstrates high-level data auditing by matching "Outbound" payments from the Main Checking account to "Inbound" credits on a Credit Card statement.

### Data Dictionary
| Attribute | Description | Data Type |
| :--- | :--- | :--- |
| **outbound_payments** | Total payments sent from the primary bank account | Float |
| **inbound_credits** | Total payments acknowledged by the credit card issuer | Float |

### Skills Demonstrated
* **Inter-Ledger Matching:** Verifying the flow of capital between two independent financial data sources.
* **Audit Documentation:** Generating clear success/failure logs to assist in month-end closing processes.

---

## Project 3: Multi-Source Payroll Reconciliation Audit
This project demonstrates the ability to perform financial auditing by cross-referencing an external HR payroll report (Gusto) with an internal bank ledger (Checking Secondary).

### Data Dictionary
| Attribute | Source | Description | Data Type |
| :--- | :--- | :--- | :--- |
| **gusto_total** | gusto_payroll.csv | The "Source of Truth" for authorized net pay | Float |
| **bank_total** | checking_secondary.csv | Actual cash outflows categorized as 'Payroll' | Float |
| **variance** | Calculated | The discrepancy between authorized pay and bank clearing | Float |

### Skills Demonstrated
* **Multi-File Integration:** Loading and processing multiple CSV sources from a structured raw_data/ directory.
* **Audit Controls:** Implementing a "Tolerance Check" (0.01) to account for floating-point rounding.

---

## Project 2: Coffee Shop Financial Ledger Analysis
This project processes a complex general ledger from a high-volume coffee shop to calculate high-level business health metrics.

### Data Dictionary
| Column Name | Description | Data Type |
| :--- | :--- | :--- |
| **type** | Categorization of funds (Credit = Income, Debit = Expense) | String |
| **amount** | The raw currency value of the transaction | Float |
| **category** | Business label (Sales Revenue, COGS, Operating Expense) | String |

### Skills Demonstrated
* **Financial Logic:** Separating revenue from costs to calculate Net Profit and Profit Margin.
* **Data Cleaning:** Using manual Python methods to strip currency symbols ($) and commas from strings.

---

## Project 1: Medical Insurance Record Cleaning
This project focuses on taking a single, unformatted string of patient records and converting it into a structured database format.

### Skills Demonstrated
* **String Parsing:** Splitting and stripping "messy" bulk data into individual record components.
* **Aggregations:** Iterating through cleaned records to find averages for BMI and insurance costs.

---

## How to Run These Projects
1. **Clone the repository:**
   `git clone https://github.com/angelinacervera/Medical-Insurance-Data-Cleaning-Python-.git`

2.
