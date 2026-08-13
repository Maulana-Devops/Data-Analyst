-- ===================================================
-- PROJECT 07: BASIS DATA PART 7 (UNION & UNION ALL)
-- Database: makul_db
-- ===================================================

-- ---------------------------------------------------
-- QUIZ 1
-- Menggabungkan data transaksi dari tabel_a dan tabel_b
-- khusus untuk pelanggan dengan kode 'polibest03'
-- ---------------------------------------------------
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


-- ---------------------------------------------------
-- QUIZ 2
-- Menampilkan data pelanggan yang pernah membeli:
-- 1. Kotak Pensil
-- 2. Flashdisk 32 GB / Flashdisk 32GB
-- 3. Sticky Note 500 Sheets / Sticky Notes 500 sheets
-- ---------------------------------------------------
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


-- ---------------------------------------------------
-- QUIZ 3
-- Menggabungkan katalog ms_produk_1 & ms_produk_2
-- Kriteria: 
-- - ms_produk_1: prod-01 s/d prod-05 dengan harga < 100000
-- - ms_produk_2: prod-06 s/d prod-10 dengan harga < 50000
-- ---------------------------------------------------
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
