# KPI & Aggregation Contract

**Project:** Data Analyst Final Project — Indonesia E-Commerce Sales
**Scope:** Streamlit dashboard in `dashboard/` and its canonical clean dataset
**Status:** Technical reference. Values below were re-verified from the source files and the canonical dataset on 2026-10-10.

> This document is the single source of truth for KPI definitions and aggregation
> rules used by the current dashboard. Where the project charter or legacy
> artifacts (Excel dashboard, PDF reports, analysis workbooks) use a different
> definition, the difference is explicitly recorded in
> [Known inconsistencies and decisions pending](#known-inconsistencies-and-decisions-pending)
> and is not silently resolved.

---

## 1. Canonical dataset and verified dimensions

| Property | Value |
|---|---|
| Canonical clean dataset (relative path) | `docs/Final Project/02_Data/Clean_Dataset/Clean_Dataset.csv` |
| Raw dataset (relative path) | `docs/Final Project/02_Data/Raw_Dataset/Raw_Dataset.csv` |
| Clean dataset shape | **18,868 rows × 30 columns** (verified) |
| Raw dataset shape | **18,868 rows × 19 columns** (verified) |
| Delimiter / encoding | `;` / `UTF-8 with BOM` |
| Row unit | One row = one order (`order_id` unique; 0 duplicates) |
| Order date range | `2023-12-01 00:33` to `2025-11-30 23:17` (from `order_datetime`, verified) |
| Missing values in clean dataset | `total_qty` 283, `Metode Pembayaran` 283, `order_date` 188 (verified) |

All metrics below are computed against the **current filter scope** produced by the
global date/province filters, unless stated otherwise.

---

## 2. Revenue

| Item | Definition |
|---|---|
| Formula | `SUM(Total Pembayaran)` over the rows in the filter scope |
| Source column | `Total Pembayaran` |
| Unit | Rupiah (IDR) |
| Missing values | None in `Total Pembayaran` (0 nulls, verified) |
| Verified value (full scope) | **Rp962,091,801** |

**Interpretation note.** Every order with `Is_Cancelled = True` in this dataset has
`Total Pembayaran` equal to Rp0 (verified: all 2,573 cancelled rows are zero). Revenue
is therefore the **sum of recorded/paid payment values**, not a gross order value.
There are additionally 56 non-cancelled orders with `Total Pembayaran = Rp0`
(verified); revenue does not attribute value to them either.

---

## 3. Order count (Orders)

| Item | Definition |
|---|---|
| Formula | `COUNT(DISTINCT order_id)` |
| Source column | `order_id` |
| Unit | orders |
| Verified value (full scope) | **18,868** |

Each order is counted exactly once. Because `order_id` is unique across the clean
dataset (verified), distinct-count and row-count coincide, but the dashboard
implementation always uses distinct `order_id` so the metric stays correct under any
future grain change.

---

## 4. Total recorded units (Total Unit Tercatat)

| Item | Definition |
|---|---|
| Formula | `SUM(total_qty)` over rows in scope |
| Source column | `total_qty` |
| Unit | items (units) |
| Missing-value behavior | 283 rows have `total_qty` missing; they are **left missing and never imputed**. Summation skips them naturally. |
| Verified value (full scope) | **47,688** |

**Effect of cancelled orders (confirmed from source).** Quantity is recorded at the
order level and is **not zeroed for cancelled orders**: cancelled rows contribute
`total_qty` to the metric. Of the 283 missing `total_qty` rows, **44 belong to
cancelled orders** (verified). Consequently this metric includes units from cancelled
orders and is a "total recorded units" figure, not an effective delivered quantity.

---

## 5. Average Order Value (AOV)

| Item | Definition |
|---|---|
| Formula | `Revenue ÷ Orders` |
| Numerator | Revenue (see section 2) |
| Denominator | **Orders = all distinct orders in scope, including cancelled orders** |
| Unit | Rupiah per order |
| Verified value (full scope) | **Rp50,990.66** (consistent with `962091801 / 18868`) |

**Convention.** The denominator deliberately includes cancelled orders (which have
revenue Rp0). The accepted convention is AOV = revenue ÷ **all** orders in scope;
the dashboard documents this in its "Definisi KPI" expander. This convention differs
from an "AOV over delivered orders only" interpretation, which is not used here.

---

## 6. Cancelled orders and cancellation rate

| Item | Definition |
|---|---|
| Cancelled orders | `COUNT(rows where Is_Cancelled = True)` |
| Cancellation rate | `Cancelled orders ÷ Orders` |
| Unit | orders; rate as decimal fraction 0–1 |
| Verified values (full scope) | Cancelled **2,573**; cancellation rate **0.136368… (13.64%)** |

The rate is stored as a decimal and formatted as a percentage only at presentation.

---

## 7. Returned orders and Order Return Rate

| Item | Definition |
|---|---|
| Returned orders | `COUNT(rows where Is_Returned = True)` |
| **Order Return Rate** | `Returned orders ÷ Orders` |
| Unit | orders; rate as decimal fraction 0–1 |
| Verified values (full scope) | Returned orders **143**; **Order Return Rate 143 ÷ 18,868 = 0.007579… (0.76%)** |

**Explicit label.** This is an **order-based** return rate (numerator = returned
orders, denominator = all orders). It is **not** a quantity-based return rate. The two
must never be conflated (143 orders ≠ 353 units; see section 8). All returned orders
in the dataset have `Status_Analisis = "Selesai"` (verified).

---

## 8. Returned units

| Item | Definition |
|---|---|
| Formula | `SUM(total_returned_qty)` |
| Source column | `total_returned_qty` |
| Unit | items (units) |
| Missing values | None (0 nulls, verified) |
| Verified value (full scope) | **353 units** |

This metric is kept **separate** from the order-based return rate. The dashboard
reports "Returned Orders" (order unit) and "Unit Retur" (item unit) as distinct values.

---

## 9. Total discount (aggregate only)

| Item | Definition |
|---|---|
| Formula | `SUM(Total Diskon)` |
| Source column | `Total Diskon` |
| Unit | Rupiah (IDR) |
| Missing values | None (0 nulls, verified); value 0 means "no discount recorded" for that order |
| Verified values (full scope) | Total discount **Rp8,004,196**; 126 orders with discount > 0; 18,742 orders at 0 |

Only the **aggregate discount value** is presented (per payment method in the Payment
& Discount page). **No Discount Rate is computed or displayed.** A discount rate would
require an approved denominator (e.g., revenue, or pre-discount value) that is not
currently defined, so none is invented.

---

## 10. Canonical dimensions for aggregation

### 10.1 Payment method

| Item | Definition |
|---|---|
| Canonical column | `Metode_Pembayaran_Clean` |
| Number of categories | **13** (verified) |
| Raw column | `Metode Pembayaran` (19 distinct raw values, 283 missing) |

**Why the normalized column is used.** The raw `Metode Pembayaran` contains spelling
and case variants (e.g., `COD`, `COD (Bayar di Tempat)`, `Cash On Delivery`;
`SPay Later`/`SPayLater`; `Online Payment`/`OnlinePayment`/`online payment`;
`Saldo ShopeePay`/`saldo shopeepay`) and 283 missing values that are consolidated into
`Tidak Diketahui`. The dashboard aggregates on `Metode_Pembayaran_Clean` so that each
order maps to exactly one stable category. The 13 clean categories are listed in the
data dictionary document.

### 10.2 Order status

| Item | Definition |
|---|---|
| Canonical column | `Status_Analisis` |
| Number of categories | **4** (verified) |
| Raw column | `Status Pesanan` (11 distinct raw values) |

**Why the normalized column is used.** The raw status contains six near-identical
variants "Pesanan diterima, namun Pembeli masih dapat mengajukan pengembalian hingga
20xx-xx-xx" (one per date) that describe the same state. `Status_Analisis` consolidates
them into four analysis-ready categories (`Batal`, `Dalam Proses`, `Selesai`,
`Selesai - Masa Pengembalian`). The dashboard aggregates on `Status_Analisis`.

---

## 11. Global filters and page-level aggregation rules

- **Global filters** come from the sidebar: a date range (`st.date_input`, inclusive
  start and end day) and a province multiselect (empty = all provinces). They are
  applied once in `dashboard/app.py` via `metrics.apply_filters()` before a page runs.
- **Filter semantics (verified from `src/metrics.py`):**
  - Date: rows kept where `order_datetime >= start` and `order_datetime < end + 1 day`
    (end day inclusive).
  - Province: rows kept where `Provinsi` is in the selected set.
  - Empty selection for province = no province filter.
- **Page-level aggregation.** Every aggregation function in `src/metrics.py`
  (`category_summary`, `province_summary`, `payment_summary`, `status_summary`,
  `returns_summary`, `shipping_method_summary`, etc.) takes the **already filtered**
  frame. Percentages/rates use the filtered scope as their denominator:
  - "Kontribusi Revenue" = group revenue ÷ total revenue of the scope.
  - "Share of Orders" (status) = status orders ÷ total orders of the scope.
  - "Order Return Rate" (per group) = returned orders of the group ÷ total orders of
    the group.
  - Order counts are always distinct `order_id`; no order is double counted across a
    dimension.
- **Filtered example (verified):** province `JAWA BARAT` → 6,078 orders, revenue
  Rp247,638,372.

---

## 12. Empty date ranges and months without transactions

- **Months without transactions are not revenue zero.** The dataset calendar spans 24
  months (2023-12 to 2025-11) but only 22 months have orders; the months **2024-12**
  and **2025-07** have no transactions (verified). The trend functions reindex the
  aggregated months onto the full calendar and represent missing months as **gaps /
  `Has_Transactions = False` with missing revenue**, never as Rp0.
- A date filter that selects no orders produces an empty scope; every page renders an
  empty-state message and no exception.

---

## 13. Charter conflict: "Return Rate" definition

- The **project charter** (`docs/Final Project/01_Project_Charter/Project_Charter.pdf`,
  KPI table) defines **"Return Rate = proporsi quantity yang dikembalikan"** — i.e., a
  **quantity-based** definition.
- The **current KPI** used by the dashboard and the final analysis report is the
  **order-based** return rate: returned orders ÷ all orders = **0.76%** (143 / 18,868).
- This is a **documented conflict**. It is **not** resolved here and the charter is
  **not** claimed to have been amended. A decision is required on which definition is
  official, or whether both may be reported with explicit labels. Until then, the
  dashboard reports only the order-based rate and does not display a quantity-based
  return rate.

---

## 14. Revenue Growth

- `Revenue Growth` appears in legacy artifacts: the charter (KPI list), the Excel
  dashboard `docs/Final Project/06_Dashboard/06_Final_Dashboard.xlsx`, and the monthly
  analysis CSV `docs/Final Project/04_Analysis/12_Monthly_Sales_Performance.csv`
  (`Revenue_Growth` column).
- The **Streamlit dashboard does not present Revenue Growth** today. It is intentionally
  not added by the dashboard code. Adding it would require an approved period-over-period
  definition.

---

## 15. Prohibited / unsupported metrics

The following must **not** be computed or displayed as KPI values until an approved
definition and supporting data exist:

| Metric | Reason it is unsupported today |
|---|---|
| Profit / profit margin | No cost or profit field exists in the raw or clean dataset |
| Customer count / cohort / retention | No customer identifier column exists |
| Discount Rate | Denominator (revenue vs pre-discount value) not approved |
| Quantity-based return rate | Denominator/definition (returned units ÷ ?) not approved; conflicts with the order-based rate (see section 13) |

---

## 16. Verified example KPI values

All values re-verified from the canonical clean dataset on 2026-10-10:

| Metric | Full scope | Source basis |
|---|---|---|
| Revenue | Rp962,091,801 | `SUM(Total Pembayaran)` |
| Orders | 18,868 | `COUNT(DISTINCT order_id)` |
| Total recorded units | 47,688 | `SUM(total_qty)` (283 missing left missing) |
| AOV | Rp50,990.66 | 962,091,801 ÷ 18,868 (all orders incl. cancelled) |
| Cancelled orders | 2,573 | `Is_Cancelled = True` |
| Cancellation rate | 13.64% | 2,573 ÷ 18,868 |
| Returned orders | 143 | `Is_Returned = True` |
| Order Return Rate | 0.76% | 143 ÷ 18,868 (order-based) |
| Returned units | 353 | `SUM(total_returned_qty)` |
| Total discount | Rp8,004,196 | `SUM(Total Diskon)` |
| Province filter (JAWA BARAT) | 6,078 orders / Rp247,638,372 | filtered aggregation |
| Missing `total_qty` | 283 | null count |

---

## 17. Known inconsistencies and decisions pending

Documented here; **no legacy artifact is edited in this phase**:

1. **Column count 31 vs 30.** The legacy PDF `docs/Final Project/07_Report/07_Final_Analysis_Report.pdf`
   states **31** columns in two places; the verified clean dataset has **30** columns.
   The PDF is not edited; a correction decision is pending.
2. **Payment-method numbers.** The Excel dashboard `06_Final_Dashboard.xlsx`
   (Payment Performance sheet) and the Final Analysis Report payment table use the
   **raw** payment labels (e.g., `COD (Bayar di Tempat)` 10,100 orders / Rp353,622,584),
   while the EDA report, root-cause analysis, analysis workbook
   `16_Payment_Method_Performance.xlsx`, and the Streamlit dashboard use
   `Metode_Pembayaran_Clean` (e.g., `COD` 10,306 orders / Rp362,770,729). These two
   groupings produce different numbers and must be reconciled by decision.
3. **Order-status grouping.** The Excel dashboard uses raw `Status Pesanan` (11
   variants); the analysis workbook `19_Cancellation_Return_Analysis.xlsx` and the
   Streamlit dashboard use `Status_Analisis` (4 categories).
4. **Return Rate definition.** Quantity-based (charter) vs order-based (delivered
   KPI) — see section 13.
5. **Revenue Growth** — present in legacy artifacts, absent from the dashboard — see
   section 14.
6. **Two dashboards.** `06_Final_Dashboard.xlsx` (Excel, legacy) and `dashboard/`
   (Streamlit, current) coexist. Which is canonical for the final deliverable is a
   pending decision.