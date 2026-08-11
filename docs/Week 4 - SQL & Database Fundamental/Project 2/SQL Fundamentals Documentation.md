# Project 02 - SQL Alias, Prefix & DISTINCT

## 1. Project Overview

Project 02 focuses on several fundamental SQL concepts related to data retrieval and query readability.

The main topics covered in this project are:

- `SELECT DISTINCT`
- Column prefix
- Column alias
- Alias without `AS`
- Prefix and alias combination
- Table alias
- Prefix with table alias

The exercises use the `ms_pelanggan` table.

---

## 2. Environment

The exercises were performed using:

- XAMPP
- MySQL
- phpMyAdmin

XAMPP was used as the local development environment, while MySQL was used to execute the SQL queries through phpMyAdmin.

---

## 3. Database and Table

The database used for the exercises is:

```text
week4_database
```

The main table is:

```text
ms_pelanggan
```

The table contains customer-related information, including:

- `no_urut`
- `kode_pelanggan`
- `nama_customer`
- `alamat`

---

# 4. Quiz Exercises

## Quiz 1 - SELECT DISTINCT

### Objective

Retrieve unique customer names from the `ms_pelanggan` table.

### Query

```sql
SELECT DISTINCT nama_customer
FROM ms_pelanggan;
```

### Explanation

`SELECT DISTINCT` is used to remove duplicate values from the query result.

In this exercise, the query retrieves unique values from the `nama_customer` column.

### Result

The query returns each unique customer name only once.

### Evidence

![Quiz 1 Result](image/quiz-01.png)

---

## Quiz 2 - Column Prefix

### Objective

Retrieve a column using the table name as a prefix.

### Query

```sql
SELECT ms_pelanggan.nama_customer
FROM ms_pelanggan;
```

### Explanation

A column prefix is used to explicitly identify which table a column belongs to.

The syntax is:

```text
table_name.column_name
```

In this query:

```text
ms_pelanggan.nama_customer
```

means the `nama_customer` column from the `ms_pelanggan` table.

### Evidence

![Quiz 2 Result](image/quiz-02.png)

---

## Quiz 3 - Column Alias

### Objective

Rename columns in the query result using the `AS` keyword.

### Query

```sql
SELECT
    no_urut AS nomor,
    nama_customer AS nama
FROM ms_pelanggan;
```

### Explanation

A column alias provides a temporary name for a column in the query result.

In this exercise:

```text
no_urut       → nomor
nama_customer → nama
```

The original column names in the database are not changed.

### Evidence

![Quiz 3 Result](image/quiz-03.png)

---

## Quiz 4 - Alias Without AS

### Objective

Use a column alias without explicitly writing the `AS` keyword.

### Query

```sql
SELECT
    no_urut nomor,
    nama_customer nama
FROM ms_pelanggan;
```

### Explanation

The `AS` keyword is optional when defining a column alias.

The following forms produce the same type of result:

```sql
nama_customer AS nama
```

and:

```sql
nama_customer nama
```

### Evidence

![Quiz 4 Result](image/quiz-04.png)

---

## Quiz 5 - Prefix and Alias

### Objective

Use a table prefix together with a column alias.

### Query

```sql
SELECT
    ms_pelanggan.nama_customer AS nama
FROM ms_pelanggan;
```

### Explanation

This query combines two concepts:

1. Table prefix
2. Column alias

The prefix identifies the source table, while the alias changes the displayed column name.

```text
ms_pelanggan.nama_customer
          ↓
       source column

AS nama
   ↓
result column name
```

### Evidence

![Quiz 5 Result](image/quiz-05.png)

---

## Quiz 6 - Table Alias

### Objective

Assign an alias to the `ms_pelanggan` table and use the alias in the query.

### Query

```sql
SELECT *
FROM ms_pelanggan t2;
```

### Explanation

The table `ms_pelanggan` is assigned the alias:

```text
t2
```

The `AS` keyword is not required when creating a table alias.

The alias can then be used to refer to the table within the query.

### Evidence

![Quiz 6 Result](image/quiz-06.png)

---

## Quiz 7 - Prefix with Table Alias

### Objective

Use a table alias as a prefix when selecting columns.

### Query

```sql
SELECT
    t2.nama_customer,
    t2.alamat
FROM ms_pelanggan t2;
```

### Explanation

The table alias `t2` is used as a prefix for the selected columns.

The syntax is:

```text
table_alias.column_name
```

In this query:

```text
t2.nama_customer
t2.alamat
```

refer to columns from the `ms_pelanggan` table represented by the alias `t2`.

### Evidence

![Quiz 7 Result](image/quiz-07.png)

---

# 5. Concepts Practiced

The project demonstrates the following SQL concepts:

| Concept | Purpose |
|---|---|
| `SELECT DISTINCT` | Retrieve unique values |
| Column Prefix | Identify the source table of a column |
| Column Alias | Rename a column in the result |
| Alias without `AS` | Create aliases using shorter syntax |
| Prefix + Alias | Combine table prefix and column alias |
| Table Alias | Give a temporary name to a table |
| Table Alias Prefix | Refer to table columns using an alias |

---

# 6. Learning Outcome

After completing Project 02, I understand how to:

- Retrieve unique data using `DISTINCT`.
- Identify columns using table prefixes.
- Rename columns using aliases.
- Use aliases with and without the `AS` keyword.
- Assign aliases to tables.
- Use table aliases as column prefixes.
- Write SQL queries that are clearer and easier to read.

---

# 7. Project Files

```text
Project 2/
├── image/
│   ├── quiz-01.png
│   ├── quiz-02.png
│   ├── quiz-03.png
│   ├── quiz-04.png
│   ├── quiz-05.png
│   ├── quiz-06.png
│   └── quiz-07.png
│
├── Readme.md
├── SQL Fundamentals Documentation.md
└── queries.sql
```

---

# 8. Conclusion

Project 02 provided practical experience with several SQL techniques used to control and organize query results.

The exercises started with retrieving unique data using `SELECT DISTINCT`, followed by column prefixes and aliases. The project then continued with table aliases and the use of aliases as prefixes when accessing columns.

These concepts provide a foundation for writing more structured and readable SQL queries in subsequent projects.
