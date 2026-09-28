# 📚 References

This document records the references, documentation, dataset sources, learning resources, and tools that are relevant to the **Industry Simulation Program – Data Analyst** repository.

The purpose of this document is to support transparency, reproducibility, and proper attribution. References are recorded based on evidence available in the repository; a dependency listed in `requirements.txt` is not automatically treated as a library used in an analysis.

---

# 📖 Reference Policy

References are grouped by their role in the repository:

1. Industry and program materials
2. Official technical documentation
3. Dataset sources
4. Repository-verified tools and technologies
5. Books and learning resources
6. Articles, tutorials, and academic references

Whenever possible, the original or official source is preferred.

---

# 🏢 Industry & Program References

The following materials are part of the learning context of the repository:

- PT Edusoft Center Teknologi
- Industry Simulation Program – Data Analyst
- Weekly modules
- Mentor guidance
- Project briefs
- Presentation materials

These materials provide the program context and learning requirements for the weekly projects and final project.

---

# 🐍 Official Technical Documentation

## Python

https://docs.python.org/3/

Official Python documentation.

---

## Pandas

https://pandas.pydata.org/docs/

Official Pandas documentation.

---

## NumPy

https://numpy.org/doc/stable/

Official NumPy documentation.

---

## Matplotlib

https://matplotlib.org/stable/

Official Matplotlib documentation.

---

## Git

https://git-scm.com/doc

Official Git documentation.

---

## GitHub

https://docs.github.com/

Official GitHub documentation.

---

## Jupyter

https://docs.jupyter.org/

Official Jupyter documentation.

---

## Google Colab

https://colab.research.google.com/

Google Colab is evidenced in multiple notebooks in the repository.

---

# 📊 Dataset Sources

## Final Project — Indonesia E-Commerce Sales

The **Indonesia E-Commerce Sales** dataset is the dataset used for the repository's **Final Project only**. It is not treated as a dataset used throughout the weekly projects.

- Dataset: Indonesia E-Commerce Sales
- Source: Kaggle
- Uploader: ZkyFauzi
- License: CC0: Public Domain
- URL: https://www.kaggle.com/datasets/zkyfauzi/indonesia-ecommerce-sales
- Raw repository file: `docs/Final Project/02_Data/Raw_Dataset/22_Raw_Dataset.csv`
- Clean repository file: `docs/Final Project/02_Data/Clean_Dataset/23_Final_Clean_Dataset.csv`
- Raw shape: 18,868 rows × 19 columns
- Clean shape: 18,868 rows × 30 columns

### Dataset Notes

The Kaggle dataset page states that the dataset is synthetically generated and may not reflect real-world data. Therefore, findings from the Final Project describe the dataset population and analytical scope rather than observed real-world market behaviour.

The repository does not currently record a specific access date or dataset version, so those fields are intentionally not invented here.

---

# 🧰 Repository-Verified Tools & Technologies

The following technologies are evidenced by repository files or deliverables.

## Programming & Analysis

- **Python** — primary programming language used in notebooks.
- **Pandas** — used for tabular data processing and analysis.
- **NumPy** — used in multiple analysis notebooks.
- **Matplotlib** — used for data visualization.
- **Jupyter Notebook** — notebook format used throughout the repository.
- **Google Colab** — evidenced by notebook imports and Colab-specific notebook content.

## Data & Document Processing

- **openpyxl** — used as the Excel writer engine in repository notebooks.
- **Microsoft Excel / XLSX** — multiple analysis, cleaning, recommendation, and dashboard deliverables are stored as `.xlsx`.
- **PDF** — analysis reports and portfolio documents are stored as `.pdf`.
- **PowerPoint / PPTX** — presentation deliverables are stored as `.pptx`.
- **Markdown** — repository documentation is written in Markdown.

## Version Control

- **Git**
- **GitHub**

### Declared Dependencies Requiring Explicit Usage Evidence

The repository's `requirements.txt` also declares:

- seaborn
- plotly
- xlsxwriter
- scipy

These packages remain available as project dependencies, but the current repository audit did not establish sufficient evidence to classify them as actively used analysis libraries. They are therefore not presented above as verified analysis tools.

---

# 📚 Books & Learning Resources

The following resources are retained as general learning references associated with the program. They are not presented as evidence that a specific project depended on a particular book.

- *Python for Data Analysis* — Wes McKinney
- *Storytelling with Data* — Cole Nussbaumer Knaflic
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Practical Statistics for Data Scientists*

## Online Learning Platforms

- Kaggle Learn
- Coursera
- DataCamp
- freeCodeCamp
- edX

---

# 📝 Articles & Tutorials

Third-party articles and tutorials should be added here when a specific project uses them as a substantive reference.

| Date | Topic | Source | Notes |
|------|-------|--------|-------|
| - | - | - | No specific third-party article is currently recorded. |

---

# 📄 Academic References

Research papers and journals should be listed here when they are used to support a specific analytical method, statistical interpretation, or business-analysis framework.

| Author | Title | Journal / Publisher | Year | DOI / URL |
|--------|-------|---------------------|------|-----------|
| - | - | - | - | No specific academic reference is currently recorded. |

---

# 📌 Citation Guidelines

When adding an external resource:

- Cite the original source whenever possible.
- Prefer official documentation for technical claims.
- Record the exact dataset source rather than listing generic dataset portals.
- Record the dataset license when it is known.
- Do not invent access dates, versions, authors, or publication details.
- Distinguish between a package declared in `requirements.txt` and a package with evidence of actual use.
- Keep Final Project dataset references scoped to the Final Project when they are not used by weekly projects.
- Respect dataset licenses and usage restrictions.

---

# 🔄 Update Policy

Update this document when:

- A new dataset is actually used in a project.
- A new library is demonstrably used in repository artifacts.
- A new official documentation source is materially consulted.
- A book, article, tutorial, or academic paper is used as a substantive reference.
- Dataset metadata such as license, version, or access date becomes available.

---

# 📅 Last Updated

2026-09-28

This date records the repository documentation update and does not imply a dataset access date.
