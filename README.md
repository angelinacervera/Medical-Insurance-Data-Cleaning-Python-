# 🩺 Professional Data Engineering Portfolio
A collection of Python projects focused on transforming messy, real-world data into actionable business insights through manual string manipulation and structured analysis.

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
1. Clone the repository: `git clone https://github.com/angelinacervera/Medical-Insurance-Data-Cleaning-Python-.git`
2. Navigate to the specific project folder.
3. Run the Python script: `python financial_cleaning.py` or `python script.py`
