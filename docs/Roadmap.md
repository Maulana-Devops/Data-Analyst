# 🗺️ Data Analysis Industry Simulation Roadmap

This document outlines the complete learning roadmap throughout the **Industry Simulation Program – Data Analyst** at **PT Edusoft Center Teknologi**.

**Status as of 28 September 2026.** This document records the learning journey,
its milestones, and its deliverables. Two numbering systems appear in it and are
kept deliberately separate:

- the **original 8-week curriculum** originally documented in this file, and
- the **repository implementation**, which follows the week numbering used by the
  folder names in `docs/`.

Status in this document is based on evidence committed to the repository: the
existence of each week's folder and the work stored inside it. A stage with no
verifiable folder is not assigned a completion status.

---

# 🎯 Program Goals

By the end of this program, I aim to:

- Perform end-to-end data analysis following industry standards.
- Build analytical thinking and problem-solving skills.
- Produce professional reports and documentation.
- Present insights to technical and non-technical audiences.
- Develop a verifiable Data Analyst portfolio.

---

# 🔄 Standard Project Workflow

Every project in this repository follows the same 12-stage workflow:

```text
Business Understanding
        ↓
Business Questions
        ↓
Data Collection
        ↓
Data Understanding
        ↓
Data Cleaning & Preparation
        ↓
Exploratory Data Analysis (EDA)
        ↓
Visualization
        ↓
Business Insight
        ↓
Recommendations
        ↓
Reporting & Presentation
        ↓
Documentation
        ↓
GitHub Portfolio
```

The full description of each stage — objectives, activities, and deliverables —
is documented in `docs/Workflow.md`.

---

# 📅 Program Roadmap

This section describes each implemented learning stage, organized by the week
numbering used in the repository. The status of every stage is recorded in the
[Progress Tracker](#-progress-tracker).

## Week 2 — Data Collection & Understanding

**Folder in repository:** `docs/Week 2- Data Collection & Understanding/`

### Objectives

- Discover and compare candidate public datasets.
- Build a data dictionary describing each field.
- Perform initial data understanding of a selected dataset.
- Summarize dataset characteristics and coverage.
- Complete a weekly mini project.

### Deliverables

- Python Notebooks
- CSV dataset
- Excel workbooks
- Reports
- Presentation slides
- Project documentation

---

## Week 4 — SQL & Database Fundamentals

**Folder in repository:** `docs/Week 4 - SQL & Database Fundamental/`

### Objectives

- Understand relational database concepts and table structure.
- Practice core SQL syntax: selection, filtering, and column aliasing.
- Apply JOINs to combine data across related tables.
- Use aggregate functions, `GROUP BY`, and `CASE WHEN`.
- Analyze transaction data using subqueries and window functions.

### Deliverables

- SQL scripts
- Per-project SQL documentation
- CSV datasets used in the exercises
- Query result screenshots

> SQL & Database Fundamentals was not part of the original 8-week curriculum
> documented in this file. It is recorded here as an additional learning stage
> implemented in Week 4.

---

## Week 5 — Data Cleaning & Preparation

**Folder in repository:** `docs/Week 5 - Data Cleaning & Preparation/`

### Objectives

- Audit the initial data quality of the dataset.
- Handle missing values and duplicate records.
- Standardize formats, values, and data types.
- Perform feature engineering for downstream analysis.
- Prepare a clean dataset ready for analysis.

### Deliverables

- Python Notebooks
- CSV datasets
- Excel workbooks
- Project documentation
- Presentation slides

---

## Week 6 — EDA Fundamentals

**Folder in repository:** `docs/Week-6/`

### Objectives

- Perform univariate analysis of individual variables.
- Perform bivariate analysis of variable relationships.
- Analyze correlations between variables.
- Summarize EDA findings in a written report.

### Deliverables

- Python Notebook
- Reports
- Excel workbook
- Presentation slides

---

## Week 7 — Advanced EDA

**Folder in repository:** `docs/Week-7 EDA Lanjutan/`

### Objectives

- Perform outlier analysis.
- Perform segment analysis.
- Perform trend analysis.
- Summarize advanced EDA findings and turn them into a business recommendation.
- Build a dashboard of the EDA findings.

### Deliverables

- Python Notebook
- Reports
- Excel workbook
- Presentation slides

---

## Week 8 — Problem Solving & Business Questions

**Folder in repository:** `docs/Week-8 Problem solving & bussiness question/`

### Objectives

- Translate a business problem into analytical questions.
- Define key performance indicators.
- Build a problem tree.
- Perform root cause analysis to identify underlying drivers.

### Deliverables

- Python Notebook
- Excel workbooks
- CSV dataset
- Reports

---

## Week 9 — Solution & Business Recommendation

**Folder in repository:** `docs/Week-9 Problem Solving & Bussiness Recomendation/`

### Objectives

- Design solutions for the identified business problems.
- Analyze the business case for the proposed solutions.
- Prioritize recommended actions.
- Communicate the recommendation to stakeholders.

### Deliverables

- Excel workbooks
- Reports
- Presentation slides

---

## Week 10 — Industry Simulation

**Folder in repository:** `docs/Week-10 Simulasi Industru/`

### Objectives

- Perform an end-to-end analysis under industry simulation conditions.
- Build visualizations and a dashboard.
- Develop a data storytelling narrative.
- Present findings and recommendations.

### Deliverables

- Reports
- Excel dashboard
- Word document
- Presentation slides

---

## Week 11 — Final Project & Portfolio

**Folder in repository:** `docs/Week-11 Final Project/`

### Objectives

- Complete the end-to-end final project.
- Organize the project as a portfolio deliverable.

### Deliverables

- Historical weekly deliverable set — see `docs/Week-11 Final Project/`

---

## Week 12 — Final Project (Continuation)

**Folder in repository:** `docs/Week-12 Final Project/`

### Objectives

- Continue and refine the final project.
- Finalize the project for portfolio publication.

### Deliverables

- Historical weekly deliverable set — see `docs/Week-12 Final Project/`

---

## Canonical Final Project Structure

**Folder in repository:** `docs/Final Project/`

The Final Project & Portfolio is **completed**. The canonical version of the
final project is organized according to the assignment's required deliverable
sections:

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

This is the primary reference for the final project. `docs/Week-11 Final Project/`
and `docs/Week-12 Final Project/` are preserved as the historical weekly stages
of the same project.

---

# 🗺 Original Curriculum vs Repository Implementation

The program was originally documented in this file as an 8-week curriculum. The
repository implements the same learning topics under a different week numbering,
and includes one additional learning stage that was not in the original plan.

| Original curriculum topic | Repository implementation |
| ------------------------- | ------------------------- |
| Data Collection & Understanding | Week 2 |
| Data Cleaning & Preparation | Week 5 |
| Exploratory Data Analysis | Week 6 and Week 7 |
| Business Problem Solving | Week 8 and Week 9 |
| Reporting / Industry Simulation | Week 10 |
| Final Project & Portfolio | Week 11 and Week 12 |

> **SQL & Database Fundamentals was added as an additional learning stage and is
> documented in Week 4.** It is not part of the original 8-week curriculum
> documented in this file.

> **Note.** `Week 4` in the repository is **SQL & Database Fundamentals**, not
> Exploratory Data Analysis. Exploratory Data Analysis is implemented in Week 6
> and Week 7.

> **Note.** Topic names for Week 8, Week 9, and Week 10 are English renderings of
> the Indonesian folder names. The folder names themselves are unchanged.

The original curriculum table is retained in the
[Historical Curriculum](#-historical-curriculum) section below as a record of what
was originally planned.

---

# 🕘 Historical Curriculum (Original Plan)

The 8-week curriculum below was the original plan for this program. It is kept
as a historical record. The repository implements the same topics under a
different week numbering — see
[Original Curriculum vs Repository Implementation](#-original-curriculum-vs-repository-implementation).

| Week | Original Topic | Repository Status |
| ---- | -------------- | ----------------- |
| 1 | Industry Orientation & Setup Tools | 📁 Not in repo |
| 2 | Data Collection & Understanding | ✅ Completed (Week 2) |
| 3 | Data Cleaning & Preparation | ✅ Completed (Week 5) |
| 4 | Exploratory Data Analysis (EDA) | ✅ Completed (Week 6 and Week 7) |
| 5 | Business Problem Solving | ✅ Completed (Week 8 and Week 9) |
| 6 | Reporting & Data Storytelling | ✅ Completed (Week 10) |
| 7 | Final Project & Portfolio | ✅ Completed (Week 11 and Week 12) |
| 8 | Final Presentation & Evaluation | ❔ Not independently verified |
| — | *SQL & Database Fundamentals* | ✅ Completed (Week 4) — additional stage |

> **Original Week 8.** The original Week 8 stage is retained as historical
> curriculum context; its specific implementation is not independently verified
> in this audit.

The Objectives and Deliverables originally written for each of these weeks have
been reorganized into the week sections above, following the repository
numbering.

---

# 📊 Progress Tracker

This table is the single source of truth for stage status in this document. The
README shows a condensed version of this table; where the two differ, this table
takes precedence.

| Week | Stage | Folder in Repository | Status |
| ---- | ----- | -------------------- | ------ |
| 1 | Industry Orientation & Setup | *(no folder in repository)* | 📁 Not in repo |
| 2 | Data Collection & Understanding | `Week 2- Data Collection & Understanding/` | ✅ Completed |
| 3 | — | *(no folder in repository)* | 📁 Not in repo |
| 4 | SQL & Database Fundamentals | `Week 4 - SQL & Database Fundamental/` | ✅ Completed |
| 5 | Data Cleaning & Preparation | `Week 5 - Data Cleaning & Preparation/` | ✅ Completed |
| 6 | EDA Fundamentals | `Week-6/` | ✅ Completed |
| 7 | Advanced EDA | `Week-7 EDA Lanjutan/` | ✅ Completed |
| 8 | Problem Solving & Business Questions | `Week-8 Problem solving & bussiness question/` | ✅ Completed |
| 9 | Solution & Business Recommendation | `Week-9 Problem Solving & Bussiness Recomendation/` | ✅ Completed |
| 10 | Industry Simulation | `Week-10 Simulasi Industru/` | ✅ Completed |
| 11 | Final Project & Portfolio | `Week-11 Final Project/` | ✅ Completed |
| 12 | Final Project (Continuation) | `Week-12 Final Project/` | ✅ Completed |
| — | **Canonical Final Project Structure** | **`Final Project/`** | **✅ Completed** |

### Week 1 and Week 3

Week 1 and Week 3 are marked as *Not in repo* rather than given a completion
status. No folder exists in this repository for either of them, so neither their
deliverables nor their completion can be verified from the repository itself.
They are left unassigned rather than marked complete or in progress, because
assigning a status without evidence would misrepresent the work.

### Basis of Evidence

Status in this table is based on the existence of the corresponding folder in the
repository. It is not derived from commit history, and no individual commit is
attributed to any stage.

### Program Status

- **Completed learning stages:** Week 2, Week 4, Week 5, Week 6, Week 7, Week 8, Week 9, Week 10
- **Completed final project:** Week 11, Week 12, and the canonical structure in `docs/Final Project/`
- **Ongoing:** continued learning, documentation refinement, and portfolio development

---

# 📌 Personal Learning Goals

Throughout this journey, I also aim to develop:

- Analytical thinking
- Problem-solving skills
- Data storytelling
- Professional documentation
- Version control using Git
- Portfolio development
- Communication and presentation skills

---

# 🚀 Current Outcome & Ongoing Work

This repository now contains:

- Python Notebooks
- SQL Scripts
- Cleaned Datasets
- Exploratory Data Analysis Reports
- Business Insight & Root Cause Analysis Reports
- Excel Dashboards
- Presentation Slides
- Project Documentation
- A Completed End-to-End Data Analysis Project

The program continues beyond the final project. The following remain ongoing:

- Further analysis and skill development
- Documentation refinement and consistency maintenance
- Portfolio presentation and review
- Preparation for the next learning stage

---

# 🔗 Related Documentation

| Document | Purpose |
|----------|---------|
| `docs/Roadmap.md` | This document — learning journey, milestones, and stage status |
| `docs/Workflow.md` | The 12-stage data analysis workflow used in every project |
| `docs/Project Structure.md` | Intended directory structure and project conventions |
| `docs/Style-Guide.md` | Coding, naming, notebook, visualization, and Git standards |
| `docs/References.md` | Official documentation, dataset sources, books, and tools |
| `docs/learning-journal.md` | Weekly learning journal and reflections |

The repository overview and condensed progress summary are maintained in
`README.md`. This roadmap is the detailed record and the authoritative source for
stage status.

> **Note.** `docs/Project Structure.md` describes the originally planned directory
> layout, which differs from the layout used in practice. The layout actually
> used is documented in `README.md`.
