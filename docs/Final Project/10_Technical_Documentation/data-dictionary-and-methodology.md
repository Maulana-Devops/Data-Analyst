# Data Dictionary & Methodology

**Project:** Data Analyst Final Project — Indonesia E-Commerce Sales
**Status:** Technical reference. All shape, type, hash, and missing-value statements
were verified read-only against the actual files on 2026-10-10.

> Layout: section 2 = raw dataset (19 columns); section 3 = clean dataset (30
> columns); section 4 = key missing values; section 5 = categorical domains.
> "Factual" rows come direct from the files; "inferred" rows are business
> interpretations and are marked **needs confirmation**.

---

## 1. Source files and integrity

| File (repository-relative path) | Shape | SHA-256 |
|---|---|---|
| `docs/Final Project/02_Data/Raw_Dataset/Raw_Dataset.csv` | 18,868 × 19 | `a495b9ff70c5324bd8a1c9c65d52c4dff052d8a82e572fd9dcbd4c4f7a383f97` |
| `docs/Final Project/02_Data/Clean_Dataset/Clean_Dataset.csv` | 18,868 × 30 | `927623f4fa170b67a82902b33d9e04dc2852679cc020049e34302c5e6fe2e133` |

- Both files: delimiter `;`, encoding UTF-8 with BOM, 1 header row, row unit = order
  (`order_id` unique). Verified read-only; no dataset was modified.
- The dashboard loads the **clean** file via
  `dashboard/src/data_loader.py` (`get_dataset()`), which caches it with
  `st.cache_data`.

### 1.1 Provenance

- The data is documented in the repository (`docs/Final Project/README.md` and the
  weekly sales records reference files) as a synthetic sales dataset for a shopee-style
  e-commerce scenario. **Needs confirmation:** the exact source title must be
  re-verified against the original Kaggle/online source page.
- **License.** `docs/References.md` (dataset sources section) records this dataset as
  **CC0: Public Domain**. Independent confirmation that the current live Kaggle page
  still carries the same license is **pending** and is recorded as such here.

---

## 2. Raw dataset — 19 columns

Types are as read natively from the raw CSV (`) with Python/Pandas; the dashboard and
all analyses then read these same columns from the clean file, where they retain the
same raw content (see section 3).

| # | Column (exact) | Raw type | Meaning (factual / inferred) | Missing |
|---|---|---|---|---|
| 1 | `order_id` | text | Order identifier. Factual: unique per row. | none |
| 2 | `total_qty` | number (float in clean) | Total item quantity for the order. Inferred: sum of units ordered. | 283 |
| 3 | `total_weight_gr` | integer | Total order weight in grams. Inferred from column name. | none |
| 4 | `total_returned_qty` | integer | Total units returned for the order. Inferred from column name. | none |
| 5 | `Total Diskon` | integer | Discount amount in Rupiah. Inferred: total discount applied. Value 0 = none recorded. | none |
| 6 | `product_categories` | text | Product category(ies) of the order. Factual: may contain multiple categories separated by `", "` (1,366 multi-category rows verified). | none |
| 7 | `num_product_categories` | integer | Number of categories in `product_categories`. Factual: equals count of comma-separated parts (verified for all rows). | none |
| 8 | `Status Pesanan` | text | Raw order status with 11 distinct values (incl. 6 date-bearing "return window" variants). | none |
| 9 | `Alasan Pembatalan` | text | Cancellation reason. Inferred from column name. | none / empty string semantics |
| 10 | `Opsi Pengiriman` | text | Shipping option chosen. Inferred from column name. | none |
| 11 | `Metode Pembayaran` | text | Payment method, raw. Factual: 19 distinct values incl. spelling/case variants; **283 missing**. | 283 |
| 12 | `Kota/Kabupaten` | text | City/regency of the order. Inferred from column name. | none |
| 13 | `Provinsi` | text | Province of the order. Factual: 34 distinct provinces. | none |
| 14 | `Ongkos Kirim Dibayar oleh Pembeli` | integer | Shipping fee paid by the buyer, Rupiah. Inferred from column name. | none |
| 15 | `Estimasi Potongan Biaya Pengiriman` | integer | Estimated shipping discount, Rupiah. Inferred from column name. | none |
| 16 | `Total Pembayaran` | integer | Final payment amount, Rupiah. Factual: Rp0 for every cancelled order; revenue metric basis. | none |
| 17 | `Perkiraan Ongkos Kirim` | integer | Estimated shipping cost, Rupiah. Inferred from column name. | none |
| 18 | `Waktu Pesanan Dibuat` | text | Order created timestamp. Inferred from column name. | none |
| 19 | `order_date` | text | Order date (raw). Factual: 188 rows missing. | 188 |

Notes: numeric shipping/discount columns show 0 nulls (verified from the clean file);
`Alasan Pembatalan`/`Opsi Pengiriman` semantics are treated as **needs confirmation**
beyond their names.

---

## 3. Clean dataset — 30 columns

The clean file keeps all 19 raw columns (with clean load types) and adds **11 derived
columns** (marked ✚). Types below are the actual Pandas dtypes produced by the
dashboard loader from the clean CSV.

| # | Column (exact) | Clean type | Origin | Missing | Notes |
|---|---|---|---|---|---|
| 1 | `order_id` | object (text) | raw | none | unique |
| 2 | `total_qty` | float64 | raw | **283** | float because of missing values; never imputed |
| 3 | `total_weight_gr` | int64 | raw | none | |
| 4 | `total_returned_qty` | int64 | raw | none | |
| 5 | `Total Diskon` | int64 | raw | none | 0 = none recorded |
| 6 | `product_categories` | object | raw | none | may hold `", "`-joined categories |
| 7 | `num_product_categories` | int64 | raw | none | = parts count of column 6 (verified) |
| 8 | `Status Pesanan` | object | raw | none | 11 raw variants retained |
| 9 | `Alasan Pembatalan` | object | raw | — | |
| 10 | `Opsi Pengiriman` | object | raw | — | |
| 11 | `Metode Pembayaran` | object | raw | **283** | raw variants retained |
| 12 | `Kota/Kabupaten` | object | raw | none | |
| 13 | `Provinsi` | object | raw | none | 34 distinct |
| 14 | `Ongkos Kirim Dibayar oleh Pembeli` | int64 | raw | none | sum 81,365,659 (verified) |
| 15 | `Estimasi Potongan Biaya Pengiriman` | int64 | raw | none | sum 200,109,075 (verified) |
| 16 | `Total Pembayaran` | int64 | raw | none | revenue basis; Rp0 on cancelled |
| 17 | `Perkiraan Ongkos Kirim` | int64 | raw | none | sum 348,049,366 (verified) |
| 18 | `Waktu Pesanan Dibuat` | object | raw | none | raw timestamp text |
| 19 | `order_date` | object | raw | **188** | raw date text; kept alongside derived date |
| 20 | `order_datetime` | datetime64[ns] | ✚ derived | none | parsed from `Waktu Pesanan Dibuat`; used by date filter |
| 21 | `order_date_clean` | datetime64[ns] | ✚ derived | none | parsed from `order_date`; parsed from `order_datetime` where needed |
| 22 | `Metode_Pembayaran_Clean` | object | ✚ normalized | none | 13 categories; canonical for aggregation |
| 23 | `Status_Analisis` | object | ✚ normalized | none | 4 categories; canonical for aggregation |
| 24 | `Tahun` | int64 | ✚ derived | none | year of `order_datetime` |
| 25 | `Bulan` | int64 | ✚ derived | none | month of `order_datetime` |
| 26 | `Tahun_Bulan` | object | ✚ derived | none | `YYYY-MM` label for monthly trends |
| 27 | `Hari` | int64 | ✚ derived | none | day of `order_datetime` |
| 28 | `Hari_Minggu` | object | ✚ derived | none | weekday name (e.g., `Senin`) |
| 29 | `Is_Cancelled` | boolean | ✚ derived | none | `True` on cancelled orders; defines cancellation KPIs |
| 30 | `Is_Returned` | boolean | ✚ derived | none | `True` on returned orders; defines return KPIs |

**Load-order note on types.** `Alasan Pembatalan` is read as string; empty strings are
treated as "no reason" at presentation. Every boolean/numeric/derived column has no
nulls (verified). The object columns are stored as text; identify them as categorical
domains in section 5.

---

## 4. Known missing values (counts verified from the canonical clean file)

| Column | Missing | Interpretation |
|---|---|---|
| `total_qty` | **283** | Not imputed. 44 of these rows are cancelled orders (the rest are non-cancelled). Quantity sums exclude missing rows. |
| `Metode Pembayaran` (raw) | **283** | Normalized to `Metode_Pembayaran_Clean = "Tidak Diketahui"` for aggregation. |
| `order_date` | **188** | Derived `order_date_clean` and `order_datetime` recover the date from `Waktu Pesanan Dibuat`, so analysis is not blocked. |
| all other columns | 0 | verified |

---

## 5. Categorical domains (verified from the canonical clean file)

### 5.1 `Metode_Pembayaran_Clean` — 13 categories

| Category | 
|---|
| Alfamart/Alfamidi/Dan+Dan |
| BCA OneKlik |
| COD |
| Cicilan Kartu Kredit |
| Indomaret/i.Saku |
| Kartu Kredit/Debit |
| Mitra Shopee |
| Online Payment |
| Pembayaran dibebaskan |
| SPayLater |
| SeaBank Bayar Instan |
| ShopeePay |
| Tidak Diketahui |

Normalization evidence: raw `Metode Pembayaran` has 19 distinct values covering case
and spelling variants (`COD` / `COD (Bayar di Tempat)` / `Cash On Delivery`;
`SPayLater` / `SPay Later`; `Online Payment` / `OnlinePayment` / `online payment`; `Saldo
ShopeePay` / `saldo shopeepay`) plus 283 missing → `Tidak Diketahui`.

### 5.2 `Status_Analisis` — 4 categories (with counts)

| Category | Orders |
|---|---|
| Selesai | 16,045 |
| Batal | 2,573 |
| Selesai - Masa Pengembalian | 161 |
| Dalam Proses | 89 |

Normalization evidence: raw `Status Pesanan` has 11 distinct values, including six
near-identical variants "Pesanan diterima, namun Pembeli masih dapat mengajukan
pengembalian hingga 20xx-xx-xx" (each with a different date), all consolidated into
`Selesai - Masa Pengembalian`.

### 5.3 `Provinsi` — 34 provinces (verified distinct count)

The 34 province names are the Indonesian provinces present in the dataset (e.g.,
`JAWA BARAT`, `DKI JAKARTA`, `JAWA TIMUR` — full list verified in the file).

### 5.4 `product_categories` — 640 distinct category strings (verified), incl. 1,366
multi-category rows.

---

## 6. Methodology / preprocessing (as supported by repository evidence)

Supported by the cleaning log and weekly prep documents (`Clean_Dataset` folder,
`README.md`, and cleaning-related notebooks/artifacts in `docs/Final Project`):

1. **Load & parse:** read raw CSV (`;`, UTF-8), drop exact-duplicate rows, parse
   date/time.
2. **Date derivation:** `order_datetime` from `Waktu Pesanan Dibuat`; `order_date_clean`
   from `order_date`, with recovery from `order_datetime` for the 188 missing rows;
   calendar parts (`Tahun`, `Bulan`, `Tahun_Bulan`, `Hari`, `Hari_Minggu`).
3. **Normalization:** payment method and order status consolidated to
   `Metode_Pembayaran_Clean` and `Status_Analisis` (section 5).
4. **Boolean flags:** `Is_Cancelled`, `Is_Returned` derived for KPI use.
5. **Missing values:** not imputed in the clean dataset; handled at analysis time.

**Reproducibility status.** The steps above are evidenced by the cleaning log and the
EDA notebook (`04_Analysis/EDA_Notebook.ipynb`) **for what was done**, but there is
**no single end-to-end cleaning script** in the repository that regenerates
`Clean_Dataset.csv` from the raw file in one run. Therefore the clean pipeline
is **documented but not fully script-reproducible** today. The dashboard itself is
read-only over the existing clean file.

---

## 7. Column-count discrepancy (31 vs 30)

- Verified fact: the clean dataset has **30 columns**.
- The legacy PDF `docs/Final Project/07_Report/07_Final_Analysis_Report.pdf` states
  **"31"** columns in two places.
- The PDF is **not edited** in this phase; the discrepancy is recorded as a pending
  decision in the KPI contract document and the PDF revision plan.

---

## 8. Limitations

- **No profit.** Neither raw nor clean dataset contains cost or profit fields; profit
  KPIs are unsupported.
- **No customer identifier.** No customer ID exists; customer-count, cohort, LT
  (lifetime value), and retention metrics are unsupported (marked **needs confirmation**
  if any future dataset adds such a column).
- **Missing values.** 283 `total_qty`, 283 raw payment, 188 raw order-date missing;
  handled without imputation.
- **Synthetic data.** Provenance is documented in the repository as a synthetic
  e-commerce dataset; synthetic signals may not reflect real-world patterns, and no
  external validation data exists. License recorded in the repository as CC0 (see
  §1.1); the current upstream license is pending confirmation.
- **Recurring dates.** Two months (2024-12, 2025-07) have no transactions; trend
  visualizations keep these as gaps.
- **Inconsistent legacy analyses.** Payment/status groupings, the return-rate
  definition, column count (31 vs 30), and Revenue Growth differ across legacy
  artifacts; see "Known inconsistencies and decisions pending" in the KPI contract.
- **No PII.** This dataset contains no personally identifying information; none is
  introduced in this documentation.