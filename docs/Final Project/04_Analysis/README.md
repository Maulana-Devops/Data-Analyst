# 04 Analysis

This folder contains the exploratory data analysis (EDA) deliverables.

## Structure

```
04_Analysis/
├── EDA_Notebook.ipynb         # Jupyter notebook with analysis code
├── EDA_Report.pdf             # PDF report with visualizations
├── Supporting_Outputs/        # 11 analysis output files
│   ├── Revenue_Order_AOV_Analysis.csv
│   ├── Monthly_Sales_Performance.csv
│   ├── Calendar_Completeness_Check.csv
│   ├── Product_Category_Performance.csv
│   ├── Top10_Product_Category.csv
│   ├── Payment_Method_Performance.xlsx
│   ├── Regional_Province_Performance.xlsx
│   ├── Quantity_Order_Value_Analysis.xlsx
│   ├── Cancellation_Return_Analysis.xlsx
│   ├── Discount_Transaction_Value_Analysis.xlsx
│   └── Shipping_Performance_Analysis.xlsx
└── figures/                   # 10 EDA visualization charts
```

## EDA Visualizations

The `figures/` folder contains 10 charts generated from the dataset:

1. **Payment Distribution** - Histogram of total payment (log scale)
2. **Quantity Boxplot** - Boxplot of order quantities
3. **Monthly Trend** - Revenue and orders over time
4. **Correlation Heatmap** - Relationships between key metrics
5. **Category Pareto** - Top 10 product categories (80.43% of revenue)
6. **Province Bar** - Top 10 provinces (74.34% of revenue)
7. **Payment Mix** - Orders vs revenue by payment method
8. **Cancellation Reasons** - Top cancellation reasons
9. **Return by Category** - Return quantity and rate by product
10. **Shipping Composition** - Estimated vs paid shipping costs

All figures are based on the verified clean dataset (18,868 × 30).