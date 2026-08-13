```markdown
# Project 07 - SQL UNION & UNION ALL

## 1. Project Overview

Project 07 focuses on combining result sets from multiple tables vertically using SQL UNION set operations.

The main concepts practiced in this project are:

- Vertically combining query results (`UNION`)
- Filtering combined datasets with `WHERE`
- Combining tables with subqueries and `INNER JOIN`
- Applying conditional filters across multiple master tables
- Calculated columns and aliases in set operations

The exercises use the `tabel_a`, `tabel_b`, `ms_pelanggan`, `ms_produk_1`, and `ms_produk_2` tables.

---

## 2. Environment

The exercises were performed using:

- XAMPP
- MySQL
- phpMyAdmin

XAMPP was used as the local development environment, while MySQL was used to execute the SQL queries through phpMyAdmin.

---

## 3. Database and Tables

The main tables used in this project are:

```text
tabel_a
tabel_b
ms_pelanggan
ms_produk_1
ms_produk_2

```

The relationships and combining logic across tables are structured as follows:

* **Transaction Combining (`tabel_a` and `tabel_b`):**
Both tables share identical schema structures (`id_transaksi`, `kode_transaksi`, `kode_pelanggan`, `no_urut`, `kode_produk`, `nama_produk`, `qty`, `harga`), allowing seamless vertical combining via `UNION`.
* **Customer Relationship:**
```text
(tabel_a UNION tabel_b).kode_pelanggan
          =
ms_pelanggan.kode_pelanggan

```


* **Product Catalog Combining (`ms_produk_1` and `ms_produk_2`):**
Both master product tables contain `kode_produk`, `nama_produk`, and `harga`, allowing unified product filtering via `UNION`.

---

# 4. Quiz Exercises

## Quiz 1 - Combining Transactions with UNION & WHERE

### Objective

Combine transaction data from `tabel_a` and `tabel_b` specifically for the customer with `kode_pelanggan = 'polibest03'`, including a calculated column for total transaction value.

### Query

```sql
SELECT 
    kode_transaksi,
    kode_pelanggan,
    no_urut,
    kode_produk,
    nama_produk,
    qty,
    harga,
    (harga * qty) AS total
FROM tabel_a
WHERE kode_pelanggan = 'polibest03'

UNION

SELECT 
    kode_transaksi,
    kode_pelanggan,
    no_urut,
    kode_produk,
    nama_produk,
    qty,
    harga,
    (harga * qty) AS total
FROM tabel_b
WHERE kode_pelanggan = 'polibest03';

```

### Explanation

The `UNION` operator vertically combines records from both transaction tables into a single result set while automatically removing duplicates.

Key points of execution:

* Each individual `SELECT` filters records where `kode_pelanggan = 'polibest03'`.
* The expression `(harga * qty)` calculates the total expenditure for each transaction item and is aliased as `total`.
* The combined result reflects all purchases made by customer `polibest03` across both transaction sources.

### Evidence

---

## Quiz 2 - Combining Subqueries (UNION) with INNER JOIN

### Objective

Retrieve distinct customer information (`kode_pelanggan`, `nama_customer`, `alamat`) for customers who bought specific products ("Kotak Pensil", "Flashdisk 32 GB", or "Sticky Note 500 Sheets") across either transaction table.

### Query

```sql
SELECT DISTINCT
    p.kode_pelanggan,
    p.nama_customer,
    p.alamat
FROM ms_pelanggan p
INNER JOIN (
    SELECT kode_pelanggan, nama_produk FROM tabel_a
    UNION
    SELECT kode_pelanggan, nama_produk FROM tabel_b
) AS tr
ON p.kode_pelanggan = tr.kode_pelanggan
WHERE tr.nama_produk IN (
    'Kotak Pensil', 
    'Flashdisk 32 GB', 
    'Flashdisk 32GB', 
    'Sticky Note 500 Sheets', 
    'Sticky Notes 500 sheets'
);

```

### Explanation

This query integrates a derived table subquery created by `UNION` with an `INNER JOIN`:

1. The subquery combines unique `kode_pelanggan` and `nama_produk` pairs from `tabel_a` and `tabel_b`.
2. The `INNER JOIN` matches the combined transaction records (`tr`) with master customer records (`ms_pelanggan`) on `kode_pelanggan`.
3. The `WHERE ... IN (...)` clause filters transactions for the targeted items.
4. `DISTINCT` ensures each customer is listed only once regardless of how many times they purchased the items.

### Evidence

---

## Quiz 3 - Conditional UNION Across Product Catalogs

### Objective

Create a unified product catalog by combining records from `ms_produk_1` and `ms_produk_2` based on specific price range criteria for each product range.

### Criteria

* From `ms_produk_1`: Products with `kode_produk` between `prod-01` and `prod-05` and `harga < 100000`.
* From `ms_produk_2`: Products with `kode_produk` between `prod-06` and `prod-10` and `harga < 50000`.

### Query

```sql
SELECT 
    kode_produk,
    nama_produk,
    harga
FROM ms_produk_1
WHERE harga < 100000 AND kode_produk BETWEEN 'prod-01' AND 'prod-05'

UNION

SELECT 
    kode_produk,
    nama_produk,
    harga
FROM ms_produk_2
WHERE harga < 50000 AND kode_produk BETWEEN 'prod-06' AND 'prod-10';

```

### Explanation

The query creates a combined catalog by enforcing strict schema alignment:

* Both `SELECT` queries return the exact same column structure (`kode_produk`, `nama_produk`, `harga`).
* The first `SELECT` filters items under 100,000 in `ms_produk_1`.
* The second `SELECT` filters items under 50,000 in `ms_produk_2`.
* `UNION` combines both result sets into a single continuous catalog.

### Evidence

---

# 5. SQL Concepts Practiced

| Concept | Purpose |
| --- | --- |
| `UNION` | Vertically combine distinct result sets from multiple queries |
| `WHERE` | Filter datasets before and after set operations |
| `BETWEEN` | Filter values within a specified range |
| `IN (...)` | Match values against a list of candidates |
| Subquery / Derived Table | Treat a query result (e.g., `UNION`) as a temporary table for JOIN operations |
| `INNER JOIN` | Connect combined subquery records with master table details |
| `DISTINCT` | Eliminate duplicate rows from the final result set |
| Calculated Column | Perform arithmetic operations (e.g., `harga * qty`) across combined tables |

---

# 6. Learning Outcome

After completing Project 07, I understand how to:

* Combine data vertically from tables with matching schema structures using `UNION`.
* Apply conditional logic (`WHERE`) to individual queries prior to merging results.
* Embed `UNION` queries inside subqueries to perform `INNER JOIN` operations with master tables.
* Standardize data formats when filtering text values (e.g., handling variations like `Flashdisk 32 GB` vs `Flashdisk 32GB`).
* Combine separate catalog tables (`ms_produk_1` & `ms_produk_2`) with conditional rules per table.
* Retrieve clean, non-duplicated lists using `DISTINCT`.

---

# 7. Project Files

```text
Project 7/
├── image/
│   ├── quiz-1.png
│   ├── quiz-2.png
│   └── quiz-3.png
│
├── tabel_a.sql
├── tabel_b.sql
├── ms_pelanggan.sql
├── ms_produk_1.sql
├── ms_produk_2.sql
├── queries.sql
└── README.md

```

---

# 8. Conclusion

Project 07 provided comprehensive hands-on practice with SQL `UNION` operations for dataset aggregation.

The exercises demonstrated how to combine transaction splits (`tabel_a` and `tabel_b`), integrate merged sets with master data (`ms_pelanggan`), and consolidate multiple product master tables (`ms_produk_1` and `ms_produk_2`).

Mastering set operations alongside JOINs and subqueries completes a critical skill set for handling distributed or partitioned datasets in relational databases.

```

```
