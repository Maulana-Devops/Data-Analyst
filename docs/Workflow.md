# 🔄 Data Analysis Workflow

This document describes the workflow currently documented in this repository for use across its projects.

The workflow is organized around activities that are common in data analysis practice; this repository does not claim it reproduces any specific company or industry-standard workflow. It serves as a guideline to keep projects organized, reproducible, and well documented.

---

# 📌 Workflow Overview

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

The twelve stages above are the stages documented in this repository. The same
twelve names and the same order appear in `README.md` and `docs/Roadmap.md`.
Stages 7 to 9 are dependent: visualization is produced from the EDA output,
business insight is derived from that visualization, and recommendations are
derived from the insight.

---

# 🗺️ Stage Reference

| # | Stage | Purpose |
|---|-------|---------|
| 1 | Business Understanding | Understand the business context before any analysis is performed |
| 2 | Business Questions | Translate the business problem into analytical questions and KPIs |
| 3 | Data Collection | Gather datasets relevant to the business problem |
| 4 | Data Understanding | Inspect structure, types, relationships, and initial data quality |
| 5 | Data Cleaning & Preparation | Produce clean and reliable data for analysis |
| 6 | Exploratory Data Analysis (EDA) | Explore data to identify patterns and relationships |
| 7 | Visualization | Communicate findings through effective visualizations |
| 8 | Business Insight | Interpret analytical findings from a business perspective |
| 9 | Recommendations | Turn insights into prioritized, actionable recommendations |
| 10 | Reporting & Presentation | Communicate results to stakeholders |
| 11 | Documentation | Make the project reproducible and documented |
| 12 | GitHub Portfolio | Publish the project as a portfolio artifact |

Quality checks that apply across these stages are described in
[Validation & Quality Check](#-validation--quality-check). Validation is not a
thirteenth stage.

---

# 1️⃣ Business Understanding

## Objective

Understand the business context before performing any analysis.

## Activities

- Read the project brief.
- Identify the business background.
- Understand stakeholder needs.
- Define project objectives.
- Determine expected outcomes.

## Deliverables

- Business Background
- Problem Statement
- Project Objectives
- Stakeholder Identification

---

# 2️⃣ Business Questions

## Objective

Translate business problems into analytical questions.

## Activities

- Identify measurable questions.
- Define Key Performance Indicators (KPIs).
- Prioritize business objectives.

## Deliverables

- List of Business Questions
- KPIs
- Analysis Scope

---

# 3️⃣ Data Collection

## Objective

Collect datasets relevant to the business problem.

## Activities

- Identify data sources.
- Download or import datasets.
- Verify dataset integrity.
- Record metadata.

## Deliverables

- Raw Dataset
- Dataset Documentation

---

# 4️⃣ Data Understanding

## Objective

Understand the structure and characteristics of the dataset.

## Activities

- Inspect rows and columns.
- Identify data types.
- Understand relationships between variables.
- Review data quality.

## Deliverables

- Dataset Summary
- Data Dictionary
- Initial Findings

---

# 5️⃣ Data Cleaning & Preparation

## Objective

Prepare clean and reliable data for analysis.

## Activities

- Handle missing values.
- Remove duplicates.
- Correct data types.
- Standardize formats.
- Detect outliers.
- Create new variables if necessary.

## Deliverables

- Clean Dataset
- Cleaning Report

---

# 6️⃣ Exploratory Data Analysis (EDA)

## Objective

Explore data to identify patterns and relationships.

## Activities

- Descriptive statistics.
- Distribution analysis.
- Correlation analysis.
- Trend analysis.
- Segment analysis.

## Deliverables

- EDA Notebook
- Initial Insights

---

# 7️⃣ Visualization

## Objective

Communicate findings through effective visualizations.

## Activities

- Select appropriate chart types.
- Label charts properly.
- Highlight key findings.
- Ensure readability.

## Deliverables

- Charts
- Dashboards
- Visual Summary

---

# 8️⃣ Business Insight

## Objective

Interpret analytical findings from a business perspective.

## Activities

- Explain patterns.
- Identify opportunities.
- Identify risks.
- Answer business questions.

## Deliverables

- Business Insights
- Supporting Evidence

---

# 9️⃣ Recommendations

## Objective

Provide actionable recommendations based on the analysis.

## Activities

- Suggest improvements.
- Connect each recommendation to a specific business insight.
- Prioritize recommendations based on impact and effort.
- Identify expected business impact where the evidence allows.
- Define measurable success metrics.
- Document the action plan and its owner or next step.

## Deliverables

- Business Recommendations
- Recommendation Prioritization
- Success Metrics / Action Plan

---

# 🔟 Reporting & Presentation

## Objective

Communicate results effectively to stakeholders.

## Activities

- Prepare reports.
- Create presentation slides.
- Summarize key findings.
- Present recommendations.

## Deliverables

- Report
- Presentation
- Executive Summary

---

# 1️⃣1️⃣ Documentation

## Objective

Ensure the project is reproducible and well documented.

## Activities

- Update README.
- Document datasets.
- Record project structure.
- Update references.
- Write notebook explanations.

## Deliverables

- Complete Documentation

---

# 1️⃣2️⃣ GitHub Portfolio

## Objective

Publish the completed project as part of a professional portfolio.

## Activities

- Organize repository.
- Review documentation.
- Upload project files.
- Write meaningful commit messages.
- Publish final version.

## Deliverables

- GitHub Repository
- Portfolio Project

---

# 🔍 Validation & Quality Check

Validation is **not** a thirteenth stage. It is a cross-cutting quality gate that
is applied at specific points in the twelve stages above, so that each stage only
builds on output that has already been checked.

## Purpose

- Ensure the output of each stage is fit to be used by the next stage.
- Prevent data or analysis errors from being carried into downstream stages.
- Ensure the final result is consistent before documentation and portfolio work.

## Where Validation Is Applied

| Point | After / Before | What Is Checked |
|-------|----------------|-----------------|
| 1 | After #4 Data Understanding | Structure, types, missing values, initial quality baseline |
| 2 | After #5 Data Cleaning & Preparation | Cleaning results, schema stability, remaining gaps |
| 3 | After #6 Exploratory Data Analysis (EDA) | Sanity of statistics and findings before they are visualized |
| 4 | After #9 Recommendations | Every recommendation traces to a specific insight |
| 5 | Before #11 Documentation and #12 GitHub Portfolio | Final review of numbers, report text, and visual consistency |

## Activities

1. Row count and schema comparison between the raw dataset and the clean dataset.
2. Missing-value and duplicate recheck after cleaning.
3. Sanity check of distributions and outliers.
4. Cross-check the numbers written in the report against the notebook or source analysis.
5. Proofread the report and check visual consistency across charts.
6. Verify that the raw dataset has not been modified.

### Data Validation

Focuses on the structure of the data itself:

- Structure and schema
- Missing values
- Duplicates
- Distributions
- Numeric sanity checks

### QA

Focuses on consistency and completeness of the work product:

- Consistency checks between stages
- Cross-check of results
- Proofread
- Visual consistency
- Completeness

### Final Review

The last check before #11 Documentation and #12 GitHub Portfolio. It confirms
that the numbers, statements, and visuals that will be published have already
been verified.

## Deliverables

- Validation Notes
- Data Quality Summary
- Issue Log
- Pre-release Checklist

---

# ✅ Workflow Checklist

This checklist mirrors the twelve stages above. It is a tracking checklist, not an
additional stage.

| Stage | Status |
|-------|--------|
| Business Understanding | ☐ |
| Business Questions | ☐ |
| Data Collection | ☐ |
| Data Understanding | ☐ |
| Data Cleaning & Preparation | ☐ |
| Exploratory Data Analysis (EDA) | ☐ |
| Visualization | ☐ |
| Business Insight | ☐ |
| Recommendations | ☐ |
| Reporting & Presentation | ☐ |
| Documentation | ☐ |
| GitHub Portfolio | ☐ |

---

# 📅 Workflow Across Weekly Projects

```text
Weekly Projects
      ↓
Final Project
      ↓
GitHub Portfolio
```

## Weekly Projects

Weekly projects are used as stages of learning and practice. Each week focuses on
a limited set of skills, so a weekly project may cover only the stages relevant
to its learning objective.

> Weekly projects may cover selected stages depending on their learning
> objective. A weekly project is not expected to cover all twelve stages, and
> this document does not claim that every week in the repository has applied the
> full workflow.

## Final Project

The Final Project integrates the analysis skills developed in the weekly projects
into a single project. It is the point where the stages are used together rather
than in isolation. Its structure is documented in
[Project Structure.md](Project%20Structure.md).

## GitHub Portfolio

The GitHub Portfolio is the published form of the project: the repository, its
documentation, its report, and its presentation, organized so the work can be
reviewed and reproduced by others.

---

# 🔗 Related Documentation

| Document | Purpose |
|----------|---------|
| [Repository overview](../README.md) | Project overview, weekly folders, and the same twelve-stage workflow |
| [Roadmap.md](Roadmap.md) | Learning roadmap, milestones, and stage status |
| [Project Structure.md](Project%20Structure.md) | Directory structure, canonical final project, and folder conventions |
| [Style-Guide.md](Style-Guide.md) | Coding, naming, notebook, visualization, and Git standards |
| [References.md](References.md) | Official documentation, dataset sources, books, and tools |
| [learning-journal.md](learning-journal.md) | Weekly learning journal and reflections |

---

# 📌 Scope of This Document

- This document describes the workflow used and documented in this repository.
- It is **not** an official company SOP.
- It is **not** a claim that this is the only workflow used in the industry.
- It does **not** claim to be identical to the workflow of any particular company.
- It is used here as a documentation and learning framework for this repository.

The weekly folders and their observed contents are recorded in
[Project Structure.md](Project%20Structure.md).

---

# 💡 Notes

Projects in this repository are structured around these stages. Where a project does not cover a stage in full, the gap is recorded rather than filled with assumed results:

- Consistency
- Reproducibility
- Professional documentation
- Better communication
- Documented, repeatable process

This workflow serves as the documentation and learning framework for the Data Analysis projects in this repository.
