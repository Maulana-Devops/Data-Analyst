# 🎨 Repository Style Guide

This document defines the coding, documentation, naming, and visualization standards used throughout the **Data Analysis Industry Simulation Portfolio**.

The goal of this style guide is to ensure that every project in this repository is consistent, readable, maintainable, and professional.

---

# 📁 Folder Naming

Use lowercase letters and hyphens (`-`) to separate words.

## ✅ Good

```text
week-02-data-collection
week-03-data-cleaning
business-problem
```

## ❌ Avoid

```text
Week2
Week_02
LatihanPython
```

---

# 📄 File Naming

Use descriptive filenames.

## Notebooks

✅ Good

```text
data-understanding.ipynb
data-cleaning.ipynb
exploratory-data-analysis.ipynb
```

❌ Avoid

```text
latihan.ipynb
baru.ipynb
coba.ipynb
```

---

## Dataset

Raw dataset

```text
customer_data.csv
sales_2025.xlsx
```

Processed dataset

```text
customer_data_clean.csv
sales_2025_processed.csv
```

---

## Reports

```text
analysis-report.md
analysis-report.pdf
```

---

## Images

```text
sales-distribution.png
missing-values.png
correlation-heatmap.png
```

---

# 🐍 Python Style

Follow the PEP 8 Style Guide whenever possible.

## Variable Names

✅ Good

```python
sales_data
customer_age
missing_values
```

❌ Avoid

```python
a
x
data1
```

---

## Function Names

Use snake_case.

```python
load_dataset()

clean_missing_values()

create_visualization()
```

---

## Constants

```python
MAX_ROWS = 100
DATA_PATH = "datasets/raw/"
```

---

# 📓 Notebook Structure

Every notebook should follow the same order.

```text
1. Business Understanding

2. Business Questions

3. Import Libraries

4. Load Dataset

5. Data Understanding

6. Data Cleaning

7. Exploratory Data Analysis

8. Visualization

9. Business Insights

10. Recommendations

11. Conclusion
```

---

# 📚 Markdown Style

Every notebook should include Markdown explanations.

Example:

```markdown
## Data Cleaning

This section handles missing values, duplicate records, and incorrect data types before performing analysis.
```

Avoid notebooks containing only code.

---

# 📊 Visualization Standards

Every visualization should include:

- Title
- Axis Labels
- Appropriate Figure Size
- Readable Font Size
- Suitable Color Palette

Example:

```python
plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Revenue")
```

---

# 📈 Chart Selection Guide

| Purpose | Recommended Chart |
|----------|-------------------|
| Comparison | Bar Chart |
| Trend | Line Chart |
| Distribution | Histogram |
| Composition | Pie Chart (limited use) |
| Correlation | Scatter Plot |
| Relationship | Heatmap |
| Frequency | Count Plot |
| Summary | Box Plot |

---

# 📦 Git Commit Style

Use meaningful commit messages.

## Good

```text
Initialize repository structure

Add Week 2 data understanding notebook

Clean missing values

Update project documentation

Create EDA visualizations
```

## Avoid

```text
update

fix

baru

123
```

---

# 📂 Documentation Standards

Every project should include:

- README
- Notebook
- Dataset Information
- References
- Conclusions

---

# 🧾 Code Comments

Write comments only when necessary.

Example:

```python
# Convert order_date to datetime format
df["order_date"] = pd.to_datetime(df["order_date"])
```

Avoid comments that simply repeat the code.

---

# 📚 Library Import Order

Import libraries in the following order:

```python
# Standard Library

# Third-party Libraries

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Custom Modules
```

---

# 📊 Dataset Rules

Always preserve the original dataset.

```text
datasets/

raw/

processed/
```

Never modify files inside **raw/**.

---

# 📋 Reporting Standards

Every project report should contain:

- Executive Summary
- Business Background
- Objectives
- Methodology
- Findings
- Insights
- Recommendations
- Conclusion

---

# 🔍 Data Analysis Principles

Before analyzing any dataset, always ask:

- What problem am I trying to solve?
- Who benefits from this analysis?
- What does each column represent?
- Is the data complete?
- Is the data reliable?
- What insights can support decision-making?

---

# ✅ Checklist Before Publishing

Before pushing a project to GitHub:

- Notebook is complete
- Markdown explanations are included
- Dataset is documented
- Visualizations are labeled
- README is updated
- References are added
- Commit messages are meaningful

---

# 🎯 Goal

Following this style guide ensures that every project in this repository is:

- Consistent
- Easy to understand
- Well documented
- Reproducible
- Professional
- Portfolio-ready
