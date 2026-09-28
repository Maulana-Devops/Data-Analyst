# 📂 Project Structure

This document describes the directory structure used in the **Industry Simulation Program – Data Analyst** repository.

**Status as of 28 September 2026.** This document distinguishes three separate things:

1. the **actual repository structure** — the folders and paths that exist today,
2. the **canonical final project structure** — the organized structure used for
   the completed final project,
3. the **historical and planned structure** — the originally documented layout,
   retained as a record and as a reference template.

A consistent project structure improves organization, reproducibility,
collaboration, and project maintainability.

---

# 📁 Actual Repository Structure

The structure below reflects the repository as it exists today.

```text
Data-Analyst/
│
├── README.md
├── License.mit
├── .gitignore
├── requirements.txt
│
└── docs/
    ├── Roadmap.md
    ├── Style-Guide.md
    ├── Workflow.md
    ├── References.md
    ├── Project Structure.md
    ├── learning-journal.md
    │
    ├── Week 2- Data Collection & Understanding/
    ├── Week 4 - SQL & Database Fundamental/
    ├── Week 5 - Data Cleaning & Preparation/
    ├── Week-6/
    ├── Week-7 EDA Lanjutan/
    ├── Week-8 Problem solving & bussiness question/
    ├── Week-9 Problem Solving & Bussiness Recomendation/
    ├── Week-10 Simulasi Industru/
    │
    ├── Week-11 Final Project/        ← historical weekly stage
    ├── Week-12 Final Project/        ← historical weekly stage
    │
    └── Final Project/                ← canonical final project structure
```

> **Note on naming.** The folder names above are quoted **verbatim** from the
> repository, including their original spelling, spacing, and capitalization, so
> that every path in this document corresponds to a real folder. A folder-naming
> cleanup is tracked separately and has not been applied to the repository.

---

# 📂 Weekly Folders in This Repository

Weekly work is grouped into one folder per week under `docs/`.

| Folder | Stage |
| ------ | ----- |
| `docs/Week 2- Data Collection & Understanding/` | Data Collection & Understanding |
| `docs/Week 4 - SQL & Database Fundamental/` | **SQL & Database Fundamentals** |
| `docs/Week 5 - Data Cleaning & Preparation/` | Data Cleaning & Preparation |
| `docs/Week-6/` | EDA Fundamentals |
| `docs/Week-7 EDA Lanjutan/` | Advanced EDA |
| `docs/Week-8 Problem solving & bussiness question/` | Problem Solving & Business Questions |
| `docs/Week-9 Problem Solving & Bussiness Recomendation/` | Solution & Business Recommendation |
| `docs/Week-10 Simulasi Industru/` | Industry Simulation |

> **Week 4 is SQL & Database Fundamentals, not Exploratory Data Analysis.**
> Exploratory Data Analysis is implemented in `docs/Week-6/` and
> `docs/Week-7 EDA Lanjutan/`.

## Week 4 — SQL & Database Fundamentals

**Folder in repository:** `docs/Week 4 - SQL & Database Fundamental/`

The folder is organized as numbered practice projects:

```text
docs/Week 4 - SQL & Database Fundamental/
├── Project 1/    → doc/, image/
├── Project 2/    → image/
├── Project 3/    → images/
├── Project 4/    → image/
├── Project 5/    → image/
├── Project 6/    → image/
├── Project 7/    → image/
├── Project 8/    → data/, image/
├── Project 9/
└── Project-10/   → image/
```

> **Note.** `Project 1` through `Project 9` use a space, while `Project-10` uses
> a hyphen. The screenshot folder is `image/` in most projects and `images/` in
> `Project 3`. Both variants are recorded here as they exist; neither has been
> renamed.

---

# 📁 Observed Weekly Conventions

The repository currently contains several observed weekly organization patterns, including Day-N, Project N, flat folders, and Day-N folders with working subfolders.

These are observations of what the folders actually contain. They are not a
formal standard, and they are not applied uniformly across weeks.

| Pattern | Where it appears |
| ------- | ---------------- |
| **Day-N folders with working subfolders** | `docs/Week 2- Data Collection & Understanding/` — `Day-01-Dataset-Discovery/`, `Day-02-Data-Dictionary/` (with `data-set-raw/`, `reports/`), `Day-03-Data-Understanding/` (with `notebook/`, `reports/`), `Day-04-Data-Summary/` (with `notebook/`, `reports/`), `Day-05-Mini-Projek-Mingguan/` (with `Project/`, `Script/`) |
| **Project N folders** | `docs/Week 4 - SQL & Database Fundamental/` |
| **Day-N folders with descriptive names** | `docs/Week 5 - Data Cleaning & Preparation/` — `Day-1/`, `Day-2 Menangani Missing Value dan Duplicate/`, `Day-3 Standarasi data/`, `Day-4/`, `Day-4 `, `Day-5/` |
| **Flat folders** | `docs/Week-6/` (with a single `Senin/` subfolder), `docs/Week-7 EDA Lanjutan/`, `docs/Week-8 Problem solving & bussiness question/`, `docs/Week-9 Problem Solving & Bussiness Recomendation/`, `docs/Week-10 Simulasi Industru/` |

> **Note.** `docs/Week 5 - Data Cleaning & Preparation/` contains both `Day-4`
> and `Day-4 ` (with a trailing space). Both entries are recorded as they exist.

### Working Subfolders Observed Across Weekly Folders

| Subfolder | Observed in |
| --------- | ----------- |
| `notebook/` | `Week 2 …/Day-03-Data-Understanding/`, `Week 2 …/Day-04-Data-Summary/` |
| `reports/` | `Week 2 …/Day-02-Data-Dictionary/`, `Day-03-Data-Understanding/`, `Day-04-Data-Summary/` |
| `data-set-raw/` | `Week 2 …/Day-02-Data-Dictionary/` |
| `doc/` | `Week 4 …/Project 1/` |
| `data/` | `Week 4 …/Project 8/` |
| `image/` | `Week 4 …/Project 1/`, `Project 2/`, `Project 4/`–`Project 8/`, `Project-10/` |
| `images/` | `Week 4 …/Project 3/` |
| `Project/`, `Script/` | `Week 2 …/Day-05-Mini-Projek-Mingguan/` |
| `Senin/` | `docs/Week-6/` |

---

# 🏆 Canonical Final Project Structure

The canonical final project structure used in this repository is organized into the following deliverable sections:

```text
docs/Final Project/
├── 01_Project_Charter/
├── 02_Data/
│   ├── Raw_Dataset/
│   └── Clean_Dataset/
├── 03_Data_Cleaning/
├── 04_Analysis/
├── 05_Business_Analysis/
├── 06_Dashboard/
├── 07_Report/
├── 08_Presentation/
└── 09_Portfolio/
```

This is the primary reference structure for the completed final project. The
raw dataset and the cleaned dataset are kept in separate sections, so the
original data is preserved and never modified — consistent with the dataset rules
in `docs/Style-Guide.md`.

---

# 🗄 Historical Weekly Folders

Two weekly folders record the final project as it was delivered at the time:

| Folder | Role |
| ------ | ---- |
| `docs/Week-11 Final Project/` | Historical weekly stage — Final Project & Portfolio |
| `docs/Week-12 Final Project/` | Historical weekly stage — Final Project continuation |

`docs/Final Project/` is the canonical structure. The two weekly folders above
are retained as a record of how the project was delivered during those weeks.

---

# 📁 Planned Repository Structure (Original Plan)

The layout below was the originally planned repository structure. It is retained
as a historical record and as a reference for the intended design. It is **not**
the structure used in practice — see
[Actual Repository Structure](#-actual-repository-structure) for that.

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

# 📁 Planned Weekly Project Template

The template below was the intended structure for each weekly project. It is
retained as a reference for the intended design. Weekly folders in the
repository currently follow the patterns listed in
[Observed Weekly Conventions](#-observed-weekly-conventions) instead.

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

**Status in this repository:** observed in `Week 2 …/Day-03-Data-Understanding/`
and `Week 2 …/Day-04-Data-Summary/`.

Examples of work it covers:

- Data Cleaning
- Exploratory Data Analysis
- Business Analysis

---

## dataset/

Stores datasets used in the project.

**Status in this repository:** not used as a folder name. Dataset storage
currently appears as `data-set-raw/` (Week 2), `data/` (Week 4), and
`02_Data/Raw_Dataset/` + `02_Data/Clean_Dataset/` (canonical final project).

### raw/

Original datasets that should never be modified.

### processed/

Cleaned datasets generated during the project.

---

## reports/

Contains project reports.

**Status in this repository:** observed in `Week 2 …/Day-02-Data-Dictionary/`,
`Day-03-Data-Understanding/`, and `Day-04-Data-Summary/`. Most other weekly
folders keep reports as files directly in the folder rather than in a `reports/`
subfolder.

Examples:

- Markdown Report
- PDF Report
- Executive Summary

---

## presentation/

Contains presentation slides used during project review or final presentation.

**Status in this repository:** not used as a folder name. Presentation files are
stored directly in their weekly folder.

---

## images/

Stores charts, screenshots, and visual assets generated during analysis.

**Status in this repository:** observed as `image/` in most Week 4 projects and
as `images/` in `Project 3`.

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

**Status in this repository:** not used.

---

# 📄 README.md

Every weekly project was intended to include its own README file.

**Status in this repository:** present in `Week 2 …`, `Week 4 …`, and
`Week 5 …`; not present in `Week-6/`, `Week-7 EDA Lanjutan/`,
`Week-8 Problem solving & bussiness question/`,
`Week-9 Problem Solving & Bussiness Recomendation/`, or
`Week-10 Simulasi Industru/`. Where present, the file is named `Readme.md`.

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

The canonical final project keeps the original and the cleaned dataset in
separate sections:

```text
docs/Final Project/02_Data/
├── Raw_Dataset/
└── Clean_Dataset/
```

Rules:

- Never modify files inside the raw dataset section
- Save cleaned datasets in a separate section from the raw dataset

These rules are already applied in the canonical final project structure. The
`dataset/raw/` and `dataset/processed/` layout from the original plan appears in
[Planned Weekly Project Template](#-planned-weekly-project-template) but is not
used in the repository.

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

Images should use descriptive filenames with words separated by hyphens (`-`),
consistent with `docs/Style-Guide.md`.

Good examples:

```text
sales-distribution.png
customer-age-histogram.png
correlation-heatmap.png
```

Avoid filenames like:

```text
image1.png
chart.png
new.png
```

---

# 📌 Naming Convention

## Planned Conventions

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

## Observed Conventions in This Repository

The names below are recorded as they currently exist. They are **not** presented
as a standard, and no folder or file has been renamed to match the planned
conventions.

| Type | Observed example |
| ---- | ---------------- |
| Folder | `Week 5 - Data Cleaning & Preparation/`, `Week-6/`, `Week-10 Simulasi Industru/` |
| Folder | `Week-8 Problem solving & bussiness question/`, `Week-9 Problem Solving & Bussiness Recomendation/` |
| Folder | `Project 1/`, `Project-10/`, `Day-1/`, `Day-3 Standarasi data/` |
| Notebook | `Data-understanding.ipynb`, `Tugas_week_6.ipynb`, `Tugas_Week_7.ipynb` |
| Notebook | `Analysis Notebook.ipynb`, `Part8_SQL.ipynb`, `Pengenalan_Data_Cleaning.ipynb` |
| Dataset | `22_Raw_Dataset.csv`, `23_Final_Clean_Dataset.csv`, `100000 Sales Records.csv` |
| Dataset | `Clean Dataset v1.csv`, `Clean Dataset v2.csv`, `Final Clean Dataset.csv` |
| SQL | `queries.sql`, `query.sql` |
| Report | `03_EDA_Report.pdf`, `04_Root_Cause_Analysis.pdf` |
| Presentation | `05_Final_Presentation.pptx`, `08_Final_Presentation.pptx`, `Presentation.pptx` |

---

# ✅ Project Checklist

Before publishing a project to GitHub, ensure:

- README completed
- Notebook documented
- Dataset documented
- Clean dataset available and kept separate from the raw dataset
- Visualizations included
- Report completed
- Presentation completed (if applicable)
- References updated
- Meaningful Git commits created

---

# 🕘 Historical Folder Layout

The repository used several earlier layouts that no longer exist. They are
recorded here so the reorganization history is not lost.

Earlier layouts that were removed included:

```text
docs/Week 2/
docs/Data Collection & Understanding/
docs/Week 2- Data Collection & Understanding/Day-3-Data-Understanding/
docs/Week 5/Day 1/
```

Weekly work was initially uploaded directly under `docs/` and later reorganized
into per-week folders. The current layout is the one shown in
[Actual Repository Structure](#-actual-repository-structure).

---

# 🔗 Related Documentation

| Document | Purpose |
|----------|---------|
| `docs/Roadmap.md` | Learning roadmap, milestones, and stage status |
| `docs/Workflow.md` | The 12-stage data analysis workflow used in every project |
| `docs/Project Structure.md` | This document — directory structure and conventions |
| `docs/Style-Guide.md` | Coding, naming, notebook, visualization, and Git standards |
| `docs/References.md` | Official documentation, dataset sources, books, and tools |
| `docs/learning-journal.md` | Weekly learning journal and reflections |

The repository overview and the list of weekly folders are also summarized in
`README.md`.

---

# 🎯 Objective

This project structure documentation ensures that the structure of every project
in this repository can be understood as:

- Organized
- Easy to navigate
- Reproducible
- Well documented
- Professional
- Portfolio-ready
