-- Project 03 - SQL Filtering & Transaction Analysis


-- Quiz 1 - WHERE
-- Filter transaksi berdasarkan nama_produk
SELECT *
FROM ms_transaksi
WHERE nama_produk = 'Kotak Pensil';


-- Quiz 2 - WHERE + OR
-- Filter transaksi untuk dua produk
SELECT *
FROM ms_transaksi
WHERE nama_produk = 'Kotak Pensil'
   OR nama_produk = 'Flashdisk 32 GB';


-- Quiz 3 - WHERE dengan Filter Harga
-- Menampilkan transaksi dengan harga di atas 50.000
SELECT *
FROM ms_transaksi
WHERE harga > 50000;


-- Quiz 4 - WHERE + AND
-- Menampilkan Flashdisk 32 GB dengan harga di bawah 50.000
SELECT *
FROM ms_transaksi
WHERE harga < 50000
  AND nama_produk = 'Flashdisk 32 GB';


-- Quiz 5 - Mini Project Transaksi
-- Menampilkan transaksi dengan total >= 100.000
-- Total dihitung dari qty × harga
-- Hasil diurutkan dari total terbesar
SELECT
    kode_pelanggan,
    nama_produk,
    qty,
    harga,
    qty * harga AS total
FROM ms_transaksi
WHERE qty * harga >= 100000
ORDER BY total DESC;
