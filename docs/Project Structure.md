# 📂 Project Structure

This document defines the standard directory structure used throughout the **Industry Simulation Program – Data Analyst**.

Following a consistent project structure improves organization, reproducibility, collaboration, and project maintainability.

---

# 📁 Repository Structure

```text
data-analysis-industry-simulation/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── docs/
├── datasets/
├── templates/
│
├── week-01-orientation/
├── week-02-data-collection/
├── week-03-data-cleaning/
├── week-04-exploratory-data-analysis/
├── week-05-business-problem/
├── week-06-reporting-storytelling/
├── week-07-final-project/
├── week-08-final-presentation/
│
└── capstone/
```

---

# 📁 Weekly Project Structure

Each weekly project follows the same directory structure.

```text
week-xx-project-name/

│
├── README.md
│
├── notebook/
│   └── analysis.ipynb
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── report.md
│   └── report.pdf
│
├── presentation/
│   └── presentation.pptx
│
├── images/
│
├── outputs/
│
└── requirements.txt
```

---

# 📄 Folder Descriptions

## notebook/

Contains Jupyter Notebook or Google Colab notebooks used during the project.

Examples:

- Data Cleaning
- Exploratory Data Analysis
- Business Analysis

---

## dataset/

Stores datasets used in the project.

### raw/

Original datasets that should never be modified.

### processed/

Cleaned datasets generated during the project.

---

## reports/

Contains project reports.

Examples:

- Markdown Report
- PDF Report
- Executive Summary

---

## presentation/

Contains presentation slides used during project review or final presentation.

---

## images/

Stores charts, screenshots, and visual assets generated during analysis.

Examples:

- Distribution plots
- Correlation heatmaps
- Dashboard screenshots

---

## outputs/

Stores generated outputs such as:

- CSV files
- Excel files
- Model outputs
- Exported tables

---

# 📄 README.md

Every weekly project must include its own README file.

The README should contain:

- Project Overview
- Business Background
- Objectives
- Dataset Information
- Workflow
- Results
- Insights
- Recommendations

---

# 📊 Notebook Structure

Every notebook should follow the same section order.

```text
1. Business Understanding

2. Business Questions

3. Import Libraries

4. Load Dataset

5. Data Understanding

6. Data Cleaning

7. Exploratory Data Analysis

8. Visualization

9. Business Insight

10. Recommendations

11. Conclusion
```

---

# 📁 Dataset Organization

```text
dataset/

├── raw/
│   └── original_dataset.csv
│
└── processed/
    └── cleaned_dataset.csv
```

Rules:

- Never modify files inside **raw/**
- Save cleaned datasets inside **processed/**

---

# 📈 Reports

Each project should produce at least one report.

Recommended contents:

- Executive Summary
- Business Background
- Methodology
- Findings
- Insights
- Recommendations

---

# 🖼 Images

Images should use descriptive filenames.

Good examples:

```text
sales_distribution.png
customer_age_histogram.png
correlation_heatmap.png
```

Avoid filenames like:

```text
image1.png
chart.png
new.png
```

---

# 📌 Naming Convention

Folders

```text
week-03-data-cleaning
```

Notebook

```text
data-cleaning.ipynb
```

Dataset

```text
customer_data.csv
```

Processed Dataset

```text
customer_data_clean.csv
```

Report

```text
analysis-report.pdf
```

Presentation

```text
presentation.pptx
```

---

# ✅ Project Checklist

Before publishing a project to GitHub, ensure:

- README completed
- Notebook documented
- Dataset documented
- Clean dataset available
- Visualizations included
- Report completed
- Presentation completed (if applicable)
- References updated
- Meaningful Git commits created

---

# 🎯 Objective

This project structure ensures that every project in this repository is:

- Organized
- Easy to navigate
- Reproducible
- Well documented
- Professional
- Portfolio-ready
