-- =========================================
-- PROJECT 06
-- SQL JOIN
-- =========================================


-- =========================================
-- QUIZ 1
-- Query 1: INNER JOIN
-- =========================================

SELECT
    tr_penjualan.*,
    ms_produk.*
FROM tr_penjualan
INNER JOIN ms_produk
    ON tr_penjualan.kode_produk = ms_produk.kode_produk;


-- =========================================
-- QUIZ 1
-- Query 2: JOIN menggunakan WHERE
-- =========================================

SELECT
    tr_penjualan.*,
    ms_produk.*
FROM tr_penjualan, ms_produk
WHERE tr_penjualan.kode_produk = ms_produk.kode_produk;


-- =========================================
-- QUIZ 2
-- INNER JOIN + Calculated Column
-- =========================================

SELECT
    tr_penjualan.kode_transaksi,
    tr_penjualan.kode_pelanggan,
    tr_penjualan.kode_produk,
    ms_produk.nama_produk,
    ms_produk.harga,
    tr_penjualan.qty,
    ms_produk.harga * tr_penjualan.qty AS total
FROM tr_penjualan
INNER JOIN ms_produk
    ON tr_penjualan.kode_produk = ms_produk.kode_produk;
