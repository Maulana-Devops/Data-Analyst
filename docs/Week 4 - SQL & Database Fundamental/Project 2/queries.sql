-- Project 02 - SQL Alias, Prefix & DISTINCT


-- Quiz 1
-- DISTINCT
-- Query akan ditambahkan setelah target output Quiz 1 dikonfirmasi.


-- Quiz 2
-- Column Prefix
-- Query akan ditambahkan setelah target output Quiz 2 dikonfirmasi.


-- Quiz 3
-- Alias pada Kolom
SELECT
    no_urut AS nomor,
    nama_produk AS nama
FROM ms_produk;


-- Quiz 4
-- Alias tanpa keyword AS
SELECT
    no_urut nomor,
    nama_produk nama
FROM ms_produk;


-- Quiz 5
-- Prefix + Alias
SELECT
    ms_produk.harga AS harga_jual
FROM ms_produk;


-- Quiz 6
-- Table Alias tanpa keyword AS
SELECT *
FROM ms_produk t2;


-- Quiz 7
-- Prefix + Table Alias
SELECT
    t2.nama_produk,
    t2.harga
FROM ms_produk t2;
