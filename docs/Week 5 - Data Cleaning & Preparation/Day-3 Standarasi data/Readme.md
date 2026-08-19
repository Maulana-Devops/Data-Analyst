# 📂 Day 3: Data Standardization Report

## 📌 Overview
- **Project:** Data Cleaning & Preparation
- **Topic:** Topik 3 - Day 3
- **Objective:** Performing dataset-wide standardization for column naming conventions, string text formats, and date formatting.

---

## 🛠️ Standardization Rules Applied

1. **Column Names:** Renamed columns to Title Case with underscores (`Transaction_ID`, `Price_Per_Unit`, `Payment_Method`).
2. **Text Standardization:** Converted categorical string values to **UPPERCASE** (`COFFEE`, `CREDIT CARD`, `TAKEAWAY`).
3. **Date Standardization:** Parsed date values into standardized ISO 8601 format (`YYYY-MM-DD`).

---

## 📋 Standardization Log Table

| Elemen Dataset | Sebelum Standardisasi | Sesudah Standardisasi | Aturan Standardisasi |
| :--- | :--- | :--- | :--- |
| **Nama Kolom** | `Transaction ID`, `Price Per Unit` | `Transaction_ID`, `Price_Per_Unit` | Title_Case dengan Underscore |
| **Nilai Teks** | `Coffee`, `Credit Card`, `Takeaway` | `COFFEE`, `CREDIT CARD`, `TAKEAWAY` | Upper Case (`UPPERCASE`) |
| **Tanggal** | String bervariasi | `2023-09-08` | ISO Format (`YYYY-MM-DD`) |

---

## 📦 Deliverables
- [x] **`Clean Dataset v2.csv`**
- [x] **`Data Standardization Report.xlsx`**
