# 🩺 Professional Data Engineering Portfolio
A collection of Python projects focused on transforming messy, real-world data into actionable business insights through manual string manipulation and structured analysis.

---

## ⚖️ Project 3: Multi-Source Payroll Reconciliation Audit
This advanced project demonstrates the ability to perform financial auditing by cross-referencing two distinct data sources: an external HR payroll report (**Gusto**) and an internal bank ledger (**Checking Secondary**).

### 📋 Data Dictionary
| Attribute | Source | Description | Data Type |
| :--- | :--- | :--- | :--- |
| **gusto_total** | gusto_payroll.csv | The "Source of Truth" for authorized net pay | Float |
| **bank_total** | checking_secondary.csv | Actual cash outflows categorized as 'Payroll' | Float |
| **variance** | Calculated | The discrepancy between authorized pay and bank clearing | Float |

### 🛠️ Skills Demonstrated
* **Multi-File Integration:** Loading and processing multiple CSV sources within a single execution environment.
* **Audit Controls:** Implementing a "Tolerance Check" (0.01) to account for floating-point rounding in financial data.
* **Data Integrity:** Using absolute value logic (`abs()`) to reconcile debit-based bank records against positive reporting totals.

---

## ☕ Project 2: Coffee Shop Financial Ledger Analysis
This project processes a complex general ledger from a high-volume coffee shop. It demonstrates the ability to handle mixed transaction types (Credits vs. Debits) and calculate high-level business health metrics.

### 📋 Data Dictionary
| Column Name | Description | Data Type |
| :--- | :--- | :--- |
| **transaction_id** | Unique identifier for each bank entry | String |
| **type** | Categorization of funds (Credit = Income, Debit = Expense) | String |
| **amount** | The raw currency value of the transaction | Float |
| **category** | Business label (Sales Revenue, COGS, Operating Expense) | String |

### 🛠️ Skills Demonstrated
* **Financial Logic:** Separating revenue from costs to calculate **Net Profit** and **Profit Margin**.
* **Data Cleaning:** Using manual Python methods to strip currency symbols ($) and commas from strings.
* **Error Handling:** Implementing `try-except` blocks to manage file dependencies.

---

## 🏥 Project 1: Medical Insurance Record Cleaning
This project focuses on the initial stage of the data pipeline: taking a single, unformatted string of patient records and converting it into a structured database format.

### 📋 Data Dictionary
| Attribute | Description | Data Type |
| :--- | :--- | :--- |
| **patient_name** | The full name of the insured individual | String |
| **age** | The current age of the patient | Integer |
| **bmi** | Body Mass Index used for risk assessment | Float |
| **insurance_cost** | The annual premium amount charged | Float |

### 🛠️ Skills Demonstrated
* **String Parsing:** Splitting and stripping "messy" bulk data into individual record components.
* **List Management:** Building nested "List of Lists" to organize multi-dimensional data.
* **Aggregations:** Iterating through cleaned records to find averages for BMI and insurance costs.

---

## 🚀 How to Run These Projects
1. **Clone the repository:**
   `git clone https://github.com/angelinacervera/Medical-Insurance-Data-Cleaning-Python-.git`

2. **Navigate to the project folder:**
   `cd Coffee-Shop-Analysis`

3. **Execute the desired script:**
   * **For Project 2 (Financial Analysis):** `python financial_cleaning.py`
   * **For Project 3 (Payroll Audit):** `python payroll_audit.py`
   * **For Project 1 (Medical Data):** Navigate back to the root and run `python script.py`
