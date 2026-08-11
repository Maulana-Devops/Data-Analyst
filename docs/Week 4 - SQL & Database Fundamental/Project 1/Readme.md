# Project 01 - SQL Fundamentals

## Overview

This project introduces the fundamentals of SQL and Relational Database Management Systems (RDBMS).

The project focuses on understanding the basic concepts of relational databases and performing basic data retrieval using SQL queries.

---

## Objectives

- Understand the basic concepts of SQL and RDBMS.
- Identify common RDBMS tools.
- Understand the basic structure of a relational database.
- Retrieve data from a table using the `SELECT` statement.
- Select specific columns from a table.
- Limit the number of rows returned by a query.

---

## Topics

### 1. SQL & RDBMS

Introduction to Structured Query Language (SQL) and Relational Database Management Systems (RDBMS).

SQL is used to communicate with relational database systems, while an RDBMS is used to create, manage, and maintain relational databases.

---

### 2. RDBMS Tools

The learning material introduces several RDBMS tools, including:

- MySQL
- PostgreSQL
- Oracle DB
- Microsoft SQL Server
- SQLite

---

### 3. RDBMS Structure

Understanding the basic structure of a relational database, including databases, tables, columns, and rows.

---

### 4. SELECT Query

The `SELECT` statement is used to retrieve data from a table.

Example:

```sql
SELECT *
FROM ms_produk;
```

The `*` symbol is used to select all columns from the table.

---

### 5. Selecting Columns

SQL can be used to retrieve specific columns instead of selecting the entire table.

#### Select One Column

```sql
SELECT nama_produk
FROM ms_produk;
```

#### Select Multiple Columns

```sql
SELECT nama_produk, harga
FROM ms_produk;
```

This allows only the required columns to be displayed in the query result.

---

### 6. Limiting Rows

The number of rows returned by a query can be limited using `LIMIT`.

Example:

```sql
SELECT *
FROM ms_produk
LIMIT 5;
```

This query returns a maximum of five rows from the table.

---

## Project Activities

The activities in this project include:

1. Learning the basic concepts of SQL and RDBMS.
2. Identifying common RDBMS tools.
3. Understanding the structure of relational databases.
4. Practicing the `SELECT` statement.
5. Selecting all columns from a table.
6. Selecting a single column.
7. Selecting multiple columns.
8. Limiting the number of returned rows.

---

## Deliverables

The project produces the following outputs:

- `queries.sql` — SQL queries used during the exercises.
- `evidence/` — Screenshots or other evidence of query execution and results.

---

## Learning Outcome

After completing this project, I understand the basic concepts of SQL and RDBMS and can perform basic data retrieval using the `SELECT` statement.

I can also select specific columns and limit the number of rows returned from a relational database table.

---

## Reference

The primary learning material for this project is:

- `Basis Data Part 1.pdf`
