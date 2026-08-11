# Project 01 - SQL Fundamentals Documentation

## 1. Project Overview

Project 01 focuses on the fundamentals of SQL and basic data retrieval from a relational database.

The exercises are based on the SQL learning material provided during the PKL program.

The main database table used in this project is:

```text
ms_produk
```

The project focuses on practicing the `SELECT` statement and controlling the columns and rows displayed in the query result.

---

## 2. Environment

The SQL exercises were performed using:

- XAMPP
- MySQL
- phpMyAdmin

XAMPP was used as the local development environment, while MySQL was used as the database management system and phpMyAdmin was used as the interface for executing SQL queries.

---

## 3. Database

The database used for the project is:

```text
week4_database
```

The main table used in the exercises is:

```text
ms_produk
```

Basic structure:

```text
week4_database
└── ms_produk
```

---

# 4. Quiz Exercises

## Quiz 1 - Select All Columns

### Objective

Display all columns and records from the `ms_produk` table.

### Query

```sql
SELECT *
FROM ms_produk;
```

### Explanation

The `SELECT` statement is used to retrieve data from a table.

The `*` symbol represents all columns in the table.

The `FROM` clause specifies the table from which the data is retrieved.

### Expected Result

The query displays all available columns and records from:

```text
ms_produk
```

### Evidence

![Quiz 1 Result](../image/quiz-01.png)

---

## Quiz 2 - Select One Column

### Objective

Display only the `nama_produk` column from the `ms_produk` table.

### Query

```sql
SELECT nama_produk
FROM ms_produk;
```

### Explanation

Instead of using `*`, a specific column can be written after the `SELECT` statement.

In this query, only:

```text
nama_produk
```

is displayed.

### Expected Result

The query returns a single column containing the product names.

### Evidence

![Quiz 2 Result](../image/quiz-02.png)

---

## Quiz 3 - Select Multiple Columns

### Objective

Display multiple selected columns from the `ms_produk` table.

### Query

```sql
SELECT nama_produk, harga
FROM ms_produk;
```

### Explanation

Multiple columns can be selected by separating their names with commas.

The query retrieves:

```text
nama_produk
harga
```

from the `ms_produk` table.

### Expected Result

The result contains the selected product name and price columns.

### Evidence

![Quiz 3 Result](../image/quiz-03.png)

---

## Quiz 4 - Limit Rows

### Objective

Limit the number of rows displayed from the `ms_produk` table.

### Query

```sql
SELECT *
FROM ms_produk
LIMIT 5;
```

### Explanation

The `LIMIT` clause restricts the number of rows returned by the query.

In this example, the query returns a maximum of:

```text
5 rows
```

### Expected Result

The result displays the first five rows returned by the query.

### Evidence

![Quiz 4 Result](../image/quiz-04.png)

---

# 5. Summary

The four exercises demonstrate the basic use of the `SELECT` statement:

```text
SELECT *
    ↓
All Columns

SELECT column
    ↓
One Column

SELECT column_1, column_2
    ↓
Multiple Columns

SELECT *
FROM table
LIMIT 5
    ↓
Limited Rows
```

These exercises provide the foundation for retrieving data from a relational database using SQL.

---

# 6. Learning Outcomes

After completing Project 01, I can:

- Identify the purpose of the `SELECT` statement.
- Retrieve all columns from a table.
- Retrieve a specific column.
- Retrieve multiple selected columns.
- Limit the number of returned rows.
- Execute basic SQL queries using MySQL and phpMyAdmin.

---

# 7. Project Files

```text
project-01/
├── README.md
├── queries.sql
├── docs/
│   └── project-01-documentation.md
└── evidence/
    ├── quiz-01.png
    ├── quiz-02.png
    ├── quiz-03.png
    └── quiz-04.png
```

---

# 8. Reference

Primary learning material:

- `Basis Data Part 1.pdf`
