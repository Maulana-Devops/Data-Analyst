# Phase 3D — Documentation Reconciliation Decision Record

**Project:** Data Analyst Final Project — Indonesia E-Commerce Sales
**Scope:** `docs/Final Project/10_Technical_Documentation/`
**Date:** 2026-10-10
**Basis:** Read-only reconciliation audit (Phase 3D-S1) plus the verified technical
references in this folder. This record captures approved documentation decisions,
supporting evidence, open conflicts, and work that requires separate authorization.

> This record documents decisions and open issues. It does not state that the whole
> project is final. Every revision of a legacy artifact requires its own
> authorization; the source-data license must be verified before publication is
> claimed to be publicly ready; and no claim is made that all results have passed
> manual visual review.

---

## A. Return Rate

**Decision: Order Return Rate is the primary return KPI currently in use.**

| Item | Value |
|---|---|
| Order Return Rate | `143 returned orders ÷ 18.868 orders = 0,7579% ≈ 0,76%` |
| Basis | Returned orders (order count), **not** returned units |
| Implementation | `Is_Returned = True` rows ÷ all rows, full dataset scope |
| Used by | EDA report, root cause analysis, final analysis report, Excel dashboard (KPI sheet 0,007579), analysis workbook `19_Cancellation_Return_Analysis.xlsx` (0,7579%), Streamlit dashboard |

This KPI is **order-based** (numerator = returned orders, denominator = all orders).
It is not a quantity-based measure and the two must not be conflated.

**Quantity-based exploration (recorded, not approved as a KPI):**

| Item | Value |
|---|---|
| Returned units | 353 (`SUM(total_returned_qty)`) |
| Recorded units | 47.688 (`SUM(total_qty)`; 283 missing rows excluded) |
| Quantity-based rate | `353 ÷ 47.688 = 0,7402% ≈ 0,74%` |

Missing-value treatment (verified):
- 283 rows have no `total_qty`; they are left missing and are excluded from the
  recorded-units denominator and summed quantity.
- One returned order also has no `total_qty` (1 of the 143 returned rows).

**The 0,74% quantity-based rate is not adopted as an official KPI.** The denominator
definition and missing-value treatment for a quantity-based rate have not yet been
approved (alternative denominators such as non-cancelled quantity 39.810 would give
different values).

**Open conflict:** the project charter's KPI list defines "Return Rate = proporsi
quantity yang dikembalikan" (quantity-based), which conflicts with the order-based
0,76% used by every delivered output. This remains an open issue and is not resolved
by this record. Reference: `kpi-and-aggregation-contract.md` §7 and §13.

---

## B. Canonical columns for analysis

**Decisions:**
1. Use `Metode_Pembayaran_Clean` for all new payment analysis (13 categories,
   including `Tidak Diketahui` for the 283 missing raw values).
2. Use `Status_Analisis` for all new status analysis (4 categories: `Batal`,
   `Dalam Proses`, `Selesai`, `Selesai - Masa Pengembalian`).

Rationale (verified in the reconciliation audit):
- The raw `Metode Pembayaran` field has 19 distinct values including spelling/case
  variants (`COD` / `COD (Bayar di Tempat)` / `Cash On Delivery`, etc.). Aggregating
  raw labels and normalized labels produces different groups **without either being
  an arithmetic error**: e.g. raw `COD (Bayar di Tempat)` = 10.100 orders /
  Rp353.622.584, while normalized `COD` = 10.306 orders / Rp362.770.729 (the
  difference being the two additional raw variants).
- The raw `Status Pesanan` field has 11 values including seven date-bearing
  "Pesanan diterima, namun Pembeli masih dapat mengajukan pengembalian hingga …"
  variants. The verified mapping to `Status_Analisis` is exact:
  `Batal`→2.573, `Selesai`→16.045, 7 "Pesanan diterima …" variants→161
  (`Selesai - Masa Pengembalian`), `Sedang Dikirim` 59 + `Telah Dikirim` 30→89
  (`Dalam Proses`).

**Scope note:** legacy Excel workbooks and the final analysis PDF that use raw-label
groupings are **not modified in this phase**. Alignment is listed as separately
authorized work (section E).

---

## C. Revenue Growth

The definition below is **verified from `04_Analysis/12_Monthly_Sales_Performance.csv`**
(recomputed to 0 difference against the stored column) and recorded here so that any
future display is consistent.

| Item | Value |
|---|---|
| Type | Month-over-month percentage change |
| Formula | `((revenue_current / revenue_previous_available) - 1) × 100%` |
| Comparison period | The previous **available** month in the series |
| First period | 2023-12 has no comparator → value **null / not available** |
| Missing months | 2024-12 and 2025-07 are absent from the series; they are **skipped**, not assumed to have zero revenue, and the growth that follows them is computed against the prior **available** month (e.g. 2025-01 vs 2024-11) |
| Units | The CSV stores **percentages** (e.g. 3,076); the Excel `Sales Trend` sheet stores the same growth as **decimal fractions** (e.g. 0,030760677) |

**Status:** this definition is recorded as the implemented behavior. It does **not**
authorize adding a Revenue Growth KPI to the Streamlit dashboard. The value shown on
the legacy Excel KPI sheet (-0,26197) is the latest month's (2025-11) change presented
without an explicit basis; the unit/basis difference between CSV and Excel remains an
item needing consistent explanation (see D.5).

---

## D. Documentation and artifact quality — open issues

Recorded as open; none are resolved by writing this file:

1. **Column count 31 vs 30.** `07_Final_Analysis_Report.pdf` states "31 kolom" in two
   places (Data & Methodology, and the Data Quality table). The verified clean dataset
   has **30 columns** (also confirmed by the cleaning log and EDA report). The PDF is
   not modified in this phase.
2. **EDA notebook visualizations.** The charter requires a minimum of 10
   visualizations in the EDA notebook (and lists it in success criteria), but the
   notebook (`04_Analysis/02_EDA_Notebook.ipynb`, 30 cells) currently contains no
   visualization cells. Charts are delivered through the EDA report PDF and the
   dashboards instead. This shortfall is documented neutrally in the Final Project
   README (section 4.8) and remains open.
3. **Raw vs normalized label groupings.** Legacy Excel workbooks and the final report
   use raw-label groupings for payment/status in places, while newer analyses use the
   normalized columns. Both are arithmetically correct but not directly comparable.
   Standardization requires separate authorization.
4. **License confirmation pending.** The repository's `docs/References.md` records
   **CC0: Public Domain** for the dataset. Independent confirmation of the license on
   the upstream source (Kaggle) page is still pending and is not assumed.
5. **Revenue Growth definition/display differences.** The units (percentage vs
   decimal fraction) and the KPI basis (latest-month change) differ between the CSV,
   the Excel workbook, and the Excel KPI sheet; a consistent explanation has not yet
   been adopted.
6. **Primary dashboard.** The primary dashboard for demonstration is the **Streamlit**
   dashboard in `dashboard/`. The Excel workbook
   (`06_Dashboard/06_Final_Dashboard.xlsx`) is retained as the legacy/complementary
   artifact and is **not deleted**.

---

## E. Work that requires separate authorization

Listed for reference; **none of these were executed** in this phase:

- Correcting the two column-count mentions in `07_Final_Analysis_Report.pdf` and the
  PDF re-render process.
- Normalizing the payment tables in the legacy workbook and PDF to
  `Metode_Pembayaran_Clean`, or adding an explicit raw/unnormalized legend.
- Aligning order-status groupings in the operational workbook sheet onto
  `Status_Analisis`.
- Adding a Revenue Growth KPI to the Streamlit dashboard (code change).
- Revising the charter regarding the Return Rate definition or the notebook
  visualization requirement.
- Adding visualizations to the EDA notebook.
- Any other artifact change that falls outside the scope of this phase.

---

## F. Acceptance principles

- This record documents **decisions and open issues**; it does not declare the whole
  project final. No "all done" status is asserted here.
- Every revision of a legacy artifact (PDF, workbook, notebook, charter) requires its
  own separate authorization.
- The source-data license must be **verified against the upstream page** before any
  publication is claimed as publicly ready.
- No claim is made that all results have passed **manual visual review**; automated
  QA is not a substitute for pixel-level visual inspection.

---

## Cross-references

- KPI & aggregation contract: `kpi-and-aggregation-contract.md`
- Data dictionary & methodology: `data-dictionary-and-methodology.md`
- Dashboard architecture, QA & reproducibility:
  `dashboard-architecture-qa-and-reproducibility.md`