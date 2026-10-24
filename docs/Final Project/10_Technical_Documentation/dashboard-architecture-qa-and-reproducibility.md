# Dashboard Architecture, QA & Reproducibility

**Project:** Data Analyst Final Project — Streamlit dashboard
**Status:** Technical reference. Code structure, dependencies, commands, and test
results were re-verified against the working tree on 2026-10-10. Items that were
verified during the earlier QA round (Phase 2C) but not re-executed in this phase are
explicitly labeled **"per prior QA report"**.

---

## 1. Repository state (verified 2026-10-10)

| Item | Value |
|---|---|
| Branch | `main` |
| HEAD | `b15cfeed6d4a502e1bebfaea54d265648540fd94` |
| Working tree | clean except untracked `dashboard/` (`?? dashboard/`) |
| Staged changes | none |
| Remote `origin` | `git@github.com:Maulana-Devops/Data-Analyst.git` (configured) |
| Published on GitHub in this project phase? | **No.** A remote is configured, but this task performed no add/commit/push; whether the new dashboard/README has been pushed is **not verified here** and must not be inferred. |

No Git staging, commit, push, or reset was performed. The dashboard is **not published**
by this phase.

---

## 2. Directory structure and file roles

```
dashboard/
├── app.py                        # Streamlit entry point
├── requirements-dashboard.txt    # Isolated dependency pins (Python 3.12)
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # cached dataset loading + column constants
│   ├── formatting.py             # id-ID number/currency formatting helpers
│   ├── metrics.py                # KPI + filter + all aggregation functions (source of truth)
│   ├── charts.py                 # shared Plotly figure builders + empty-state figure
│   └── pages/
│       ├── __init__.py
│       ├── _skeleton.py          # page scaffold template
│       ├── executive_overview.py # page 1
│       ├── product_regional.py   # page 2
│       ├── payment_discount.py   # page 3
│       ├── order_operations.py   # page 4
│       └── shipping_data_quality.py # page 5
└── tests/
    ├── test_metrics.py           # 14 tests
    ├── test_aggregations.py      # 11 tests
    └── test_phase2b_aggregations.py # 43 tests
```

### Role of each module (verified from code)

| Module | Responsibility |
|---|---|
| `app.py` | Streamlit `st.set_page_config`, sidebar date-range + province filters, calls `metrics.apply_filters(...)`, then dispatches to the selected page's `render(df)`. Applied filters on page changes via session state. |
| `src/data_loader.py` | `get_dataset()` reads the canonical clean CSV (`;`, utf-8-sig) with `st.cache_data`; defines column-name constants (`DATE_COLUMNS`, `NUMERIC_COLUMNS`, `BOOLEAN_COLUMNS`). |
| `src/formatting.py` | id-ID number formatting (`Rp`, `.` thousands/decimal separators) used across pages. |
| `src/metrics.py` | Single source of truth for KPI definitions and aggregations: `apply_filters`, revenue/orders/qty/AOV, cancelled/returned KPIs, discount summary, and per-dimension summaries (category, province, payment, status, returns, shipping, missing-value). All percentages/rates use the filtered scope as denominator. |
| `src/charts.py` | Reusable Plotly figure builders (`bar_chart`, `grouped_bar_chart`, ...) and `empty_figure()` so empty scopes render cleanly. |
| `src/pages/_skeleton.py` | Shared page structure (header, "Definisi KPI" expander, section layout). |
| `tests/` | `unittest` suites covering metric correctness, aggregation behavior, chart construction, and filter/empty-scope behavior. |

---

## 3. The five navigation pages (verified from code)

| Page key | Module | Implemented responsibilities |
|---|---|---|
| Executive Overview | `src/pages/executive_overview.py` | Top KPIs (Revenue, Orders, AOV, Cancellation Rate, Returned Orders, Order Return Rate, Unit Retur, Total Unit Tercatat) with definitions expander; revenue by month trend with full-calendar months (gaps, not zeros); top-10 category contribution; province map values (top-5 contributions); returns trend. |
| Product & Regional | `src/pages/product_regional.py` | Category ranking (revenue, orders, AOV, contribution); category overview table; province performance (revenue/orders/AOV, contribution, top provinces); province distribution chart. |
| Payment & Discount | `src/pages/payment_discount.py` | Payment-method performance on `Metode_Pembayaran_Clean` (revenue, orders, AOV, contribution); discount summary (total discount, orders with/without discount); payment × discount crosses; payment method details table. |
| Order & Operations | `src/pages/order_operations.py` | Order status profile on `Status_Analisis` (orders, share, cancellation rate); cancelled-order analysis (reason frequency, cancelled value/loss); returned-order analysis (return rate by payment/category, return reasons, return history). |
| Shipping & Data Quality | `src/pages/shipping_data_quality.py` | Shipping method performance (on-time/not-on-time split); shipping cost aggregates; delivery time analysis; data-quality view (missing `total_qty`/`Metode Pembayaran`/`order_date` counts, integrity flags). |

Each page exposes a `render(df)` function and renders its own empty-state message when
the filtered frame is empty (verified: no exception, single guidance alert).

---

## 4. Dependencies (as written in `dashboard/requirements-dashboard.txt`)

```
streamlit==1.65.0
pandas==2.3.3
plotly==6.9.0
```

- Pinned exact versions; header comment: "Phase 1 dependencies for the Data Analyst
  dashboard. Python 3.12 compatible. Install into dashboard/.venv only."
- The local virtual environment used for all runs is `dashboard/.venv/` (Python
  3.12.14). It is **not a tracked deliverable**: `.gitignore` contains `.venv/` and
  `git check-ignore` confirms `dashboard/.venv/` is ignored (verified).
- Runtime dependencies are isolated from the rest of the repository; no system-wide
  installs were performed.

---

## 5. Commands (run from `dashboard/`)

```bash
# Install dependencies into the project venv (one-time; read-only to code)
python -m venv .venv
./.venv/bin/pip install -r requirements-dashboard.txt

# Start the dashboard (Streamlit)
./.venv/bin/streamlit run app.py

# Run the full test suite
./.venv/bin/python -m unittest discover -s tests

# Run tests with deprecation warnings promoted to errors
./.venv/bin/python -W error::DeprecationWarning -m unittest discover -s tests
```

---

## 6. Test results (re-run and verified 2026-10-10)

| Run | Result |
|---|---|
| `python -m unittest discover -s tests` | **Ran 68 tests — OK** |
| `-W error::DeprecationWarning` (deprecations as errors) | **Ran 68 tests — OK** |

Breakdown: `tests/test_metrics.py` (14), `tests/test_aggregations.py` (11),
`tests/test_phase2b_aggregations.py` (43). No source or tests were modified to achieve
these results.

---

## 7. Data integrity (re-checked this phase)

| Fact | Verified value |
|---|---|
| Clean dataset path | `docs/Final Project/02_Data/Clean_Dataset/Clean_Dataset.csv` |
| Clean shape | 18,868 × 30 |
| Clean SHA-256 | `927623f4fa170b67a82902b33d9e04dc2852679cc020049e34302c5e6fe2e133` |
| Raw shape / raw SHA-256 | 18,868 × 19 / `a495b9ff70c5324bd8a1c9c65d52c4dff052d8a82e572fd9dcbd4c4f7a383f97` |
| Duplicate `order_id` | 0 (verified) |
| KPI full-scope values | Revenue Rp962,091,801; Orders 18,868; AOV Rp50,990.66; Cancelled 2,573 (13.64%); Returned 143 (0.76%); Returned units 353; Total discount Rp8,004,196 (see kpi-and-aggregation-contract.md) |
| Months without transactions | 2024-12, 2025-07 (gaps, not zero) |

---

## 8. QA coverage

QA in Phase 2C was performed with a real headless Google Chrome driven via the Chrome
DevTools Protocol (Node scripts) while serving the app on a local port. What this
covered and its status:

| Check | Status |
|---|---|
| Full dataset load on all 5 pages | **per prior QA report** — passed (no exceptions, KPIs rendered) |
| Province filter (JAWA BARAT) → caption 6,078 orders / Rp247,638,372, consistent across chart and caption | **per prior QA report** — passed; the aggregation itself re-verified this phase (section 7) |
| Date range with zero orders (single-day 2024-12-01) → caption count 0, single guidance alert, no exception on all 5 pages | **per prior QA report** — passed |
| Empty-state handling per page | **per prior QA report** — passed; also covered by the `empty_scope` unit tests run this phase |
| Headless browser DOM interaction (navigation, captions, tooltips structure) | **per prior QA report** — passed |
| HTTP/health check (`GET /` and `/_stcore/health` → 200) | **per prior QA report** — passed |
| Browser console / page errors | **per prior QA report** — none observed |
| Test suite + deprecation-as-error | **re-run this phase** — 68 OK |
| Dataset schema/types/hash/missing counts | **re-run this phase** — verified |

**"Per prior QA report" items were not re-executed in this phase**; they are recorded
for continuity and should be re-run when the dashboard next changes.

### 8.1 Visual-QA limitations (important)

A headless DOM/browser check is **not** equivalent to a manual, pixel-level visual
review. It verifies that elements exist, captions show expected text, navigation works,
and no exceptions fire, but it does **not** verify layout aesthetics, color contrast,
plotly tooltip placement, hover behavior, or keyboard accessibility. Those require a
human (or a dedicated visual regression/screenshot-diff) review and are listed here as
**out of scope for the automated QA performed**.

---

## 9. Security and environment notes

- No `~/.streamlit/` or `dashboard/.streamlit/` configuration exists; **no secrets,
  API keys, or credentials are stored** and none are referenced by the code. `app.py`
  reads data from the local CSV only.
- Machine-specific details (absolute local paths outside the repo, venv UUIDs) are not
  part of these documents.
- `.gitignore` also covers `__pycache__/`, `.venv/` (all levels), `.env`, notebook
  checkpoints, caches, and generated report/extracted artifacts — so the dashboard
  runtime environment is not accidentally tracked.

---

## 10. Reproducibility summary

| Item | Reproducible? |
|---|---|
| Start dashboard locally | Yes — commands in section 5 |
| Run tests | Yes — 68/68, incl. deprecation-as-error |
| Regenerate clean dataset from raw via one script | **No** — no end-to-end cleaning script exists; steps are documented in the cleaning log but not script-recoverable (see data-dictionary-and-methodology.md §6) |
| Publish from this phase | **No** — no Git operation performed |

---

## 11. Cross-references

- KPI definitions & aggregation rules: `docs/Final Project/10_Technical_Documentation/kpi-and-aggregation-contract.md`
- Dataset schema, dictionary & preprocessing: `docs/Final Project/10_Technical_Documentation/data-dictionary-and-methodology.md`