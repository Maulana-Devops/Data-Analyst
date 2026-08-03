# 📊 Dataset Comparison

## Overview

The first step in every data analysis project is selecting the most appropriate dataset. Rather than choosing the first available dataset, multiple datasets were evaluated based on quality, completeness, scalability, and their potential to answer business questions.

This comparison documents the evaluation process used to select the primary dataset for the Industry Simulation Program.

---

# Evaluation Criteria

The following criteria were used to compare candidate datasets:

| Criteria | Description |
|----------|-------------|
| Relevance | Suitable for business analysis and learning objectives |
| Data Size | Sufficient number of records for meaningful analysis |
| Feature Completeness | Contains enough variables for exploration |
| Data Quality | Well-structured and easy to understand |
| Analysis Potential | Suitable for EDA, visualization, SQL, dashboard, and storytelling |

---

# Candidate Datasets

## Dataset 1

### Sample - Superstore

| Attribute | Information |
|-----------|-------------|
| Source | Kaggle |
| Format | CSV |
| Records | 9,994 |
| Columns | 21 |
| Domain | Retail / Sales |

### Advantages

- Rich customer information
- Multiple categorical variables
- Suitable for visualization
- Popular dataset for learning Data Analysis
- Easy to understand

### Disadvantages

- Relatively small dataset
- Frequently used in tutorials

---

## Dataset 2

### 100000 Sales Records

| Attribute | Information |
|-----------|-------------|
| Source | Kaggle |
| Format | CSV |
| Records | 100,000 |
| Columns | 14 |
| Domain | Sales |

### Advantages

- Large dataset
- Suitable for performance testing
- Contains realistic sales transactions
- Good for statistical analysis
- Suitable for dashboard development

### Disadvantages

- Customer information is limited
- Fewer categorical attributes than Superstore

---

## Dataset 3

### Sample - Superstore (.xls)

| Attribute | Information |
|-----------|-------------|
| Source | Kaggle |
| Format | XLS |
| Records | Same content as CSV version |
| Domain | Retail / Sales |

### Advantages

- Spreadsheet format
- Same data as CSV version

### Disadvantages

- Duplicate dataset
- No additional analytical value

---

# Comparison Summary

| Dataset | Records | Columns | Analysis Potential | Recommendation |
|----------|---------|---------|--------------------|----------------|
| Sample - Superstore | 9,994 | 21 | ⭐⭐⭐⭐⭐ | Recommended |
| 100000 Sales Records | 100,000 | 14 | ⭐⭐⭐⭐⭐ | **Highly Recommended** |
| Sample - Superstore (.xls) | 9,994 | 21 | ⭐⭐⭐ | Not Selected |

---

# Final Decision

The **100000 Sales Records** dataset was selected as the primary dataset for this project because it provides:

- A larger number of observations.
- Better scalability for future analysis.
- Sufficient variables for business analysis.
- Opportunities for statistical analysis, visualization, SQL, and dashboard development.

The **Sample - Superstore** dataset will be retained as an alternative dataset for additional practice and experimentation.

---

# Next Step

The selected dataset will be used in **Day 02 – Data Collection**, where the dataset source, metadata, and licensing information will be documented before moving on to Data Understanding.
