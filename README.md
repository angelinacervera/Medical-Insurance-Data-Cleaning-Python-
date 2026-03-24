# Medical-Insurance-Data-Cleaning-Python-
Project Objective
The goal of this project was to take a raw, "messy" string of medical records and transform it into a structured, clean format suitable for data analysis. This involved extensive use of Python String Methods and Control Flow.

Skills Demonstrated
Data Cleaning: Used .strip(), .replace(), and .split() to remove whitespace and unwanted characters.

String Manipulation: Utilized string slicing ([1:]) to prepare currency data for mathematical operations.

Data Structuring: Converted a single string into nested lists (List of Lists) to organize individual patient records.

Basic Analysis: Iterated through processed data to calculate key metrics like Average BMI and Average Insurance Cost.

---

---

## ☕ Project 2: Coffee Shop Financial Analysis
This section demonstrates advanced data cleaning using the **Pandas** library. It processes a synthetic financial dataset to calculate business metrics, moving beyond basic string manipulation into structured data analysis.

### 📋 Data Dictionary
| Column Name | Description | Data Type |
| :--- | :--- | :--- |
| **transaction_id** | Unique identifier for each sale | String |
| **transaction_date** | The date the purchase was made | DateTime |
| **transaction_amount** | The total value of the sale (Cleaned to float) | Float |
| **item_category** | The type of product sold (Beverage, Food, etc.) | String |

### 🛠️ Skills Demonstrated
* **Automated Cleaning:** Standardizing column headers (lowercase, underscores).
* **Regex Processing:** Using Regular Expressions to strip currency symbols ($).
* **Aggregations:** Calculating total revenue and average transaction values.
* **Error Handling:** Implementing `try-except` blocks for file management. blocks to manage missing files.
