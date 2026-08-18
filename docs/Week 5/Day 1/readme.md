# 📂 Day 1: Initial Data Audit Report

## 📌 Overview
- **Project:** Simulasi Industri Junior Data Analyst - Edusoft Center
- **Topic:** Topik 3 - Data Cleaning & Preparation
- **Date:** Day 1 (Monday)
- **Role:** Junior Data Analyst
- **Objective:** Conducting an initial data audit to identify quality issues in the raw dataset before applying any cleaning procedures.

---

## 🛠️ Tools & Libraries Used
- **Environment:** Google Colab
- **Language:** Python 3.x
- **Libraries:** `pandas`, `numpy`

---

## 🔍 Key Audit Steps Executed
1. **Dataset Loading:** Uploaded and loaded the raw dataset into Pandas DataFrame.
2. **Structural Inspection:** Analyzed dataset dimensions (total rows and columns) and data types using `.info()`.
3. **Missing Value Detection:** Counted total missing values per column using `.isnull().sum()`.
4. **Duplication Check:** Identified identical duplicate rows across the dataset using `.duplicated().sum()`.
5. **Statistical Profiling:** Evaluated data distributions, anomalies, and summary statistics using `.describe(include='all')`.

---

## 📊 Summary of Initial Findings

| Audit Metric | Result / Observation |
| :--- | :--- |
| **Total Rows** | *(Fill with your total rows, e.g., 1,000)* |
| **Total Columns** | *(Fill with your total columns, e.g., 12)* |
| **Total Duplicate Rows** | *(Fill with duplicate count, e.g., 15)* |
| **Columns with Missing Values** | *(e.g., `age` [20], `city` [5])* |
| **Data Type Inconsistencies** | *(e.g., `order_date` loaded as `object` instead of `datetime`)* |

### 🚨 Identified Data Issues:
- **Missing Values:** Found null/empty values in specific numerical and categorical columns.
- **Duplicate Records:** Found redundant rows that need to be dropped.
- **Formatting & Types:** Inconsistent string casing, trailing spaces, and incorrect date formats.

---

## 📄 Day 1 Deliverables Checklist
- [x] **`Notebook Audit.ipynb`** - Google Colab notebook containing all inspection scripts.
- [x] **`Initial Data Audit.xlsx`** - Detailed spreadsheet log summarizing data quality metrics.
- [x] **`DAY1_DOCUMENTATION.md`** - GitHub markdown summary report for Day 1.

---
*Next Step: Proceed to Day 2 - Handling Missing Values & Duplicates.*
