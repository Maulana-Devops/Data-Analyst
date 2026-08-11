-- Project 02 - SQL Alias, Prefix & DISTINCT

-- Quiz 1 - DISTINCT
SELECT DISTINCT nama_customer
FROM ms_pelanggan;


-- Quiz 2 - Column Prefix
SELECT ms_pelanggan.nama_customer
FROM ms_pelanggan;


-- Quiz 3 - Column Alias
SELECT
    no_urut AS nomor,
    nama_customer AS nama
FROM ms_pelanggan;


-- Quiz 4 - Alias without AS
SELECT
    no_urut nomor,
    nama_customer nama
FROM ms_pelanggan;


-- Quiz 5 - Prefix + Alias
SELECT
    ms_pelanggan.nama_customer AS nama
FROM ms_pelanggan;


-- Quiz 6 - Table Alias
SELECT *
FROM ms_pelanggan t2;


-- Quiz 7 - Prefix + Table Alias
SELECT
    t2.nama_customer,
    t2.alamat
FROM ms_pelanggan t2;
