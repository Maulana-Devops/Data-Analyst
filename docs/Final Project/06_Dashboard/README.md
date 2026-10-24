# 06 Dashboard

This folder contains the dashboard deliverables.

## Structure

```
06_Dashboard/
├── Final_Dashboard.xlsx       # Excel dashboard (8 worksheets)
└── README.md                  # This file
```

## Deliverables

### Excel Dashboard (`Final_Dashboard.xlsx`)

The Excel dashboard contains 8 worksheets:
- KPI Summary
- Revenue Analysis
- Product Performance
- Regional Analysis
- Payment Performance
- Cancellation & Return
- Shipping Analysis
- Data Quality Notes

### Interactive Dashboard (Streamlit)

The interactive dashboard is available in the repository's `dashboard/` folder.
To run:

```bash
cd dashboard
pip install -r requirements-dashboard.txt
streamlit run app.py
```

**Note:** The Excel dashboard is the primary deliverable. The Streamlit dashboard is supplementary for demonstration purposes.

## Data Source

All dashboard metrics are computed from `02_Data/Clean_Dataset/Clean_Dataset.csv` (18,868 × 30).

## Key Metrics Verified

- Revenue: Rp962,091,801
- Orders: 18,868
- AOV: Rp50,991 (all orders), Rp59,246 (paid only)
- Cancellation Rate: 13.64% (2,573 orders)
- Return Rate: 0.76% (143 orders)