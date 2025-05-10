# iDesignGPT Code Repository

This repository provides all supporting materials for the iDesignGPT framework, including agent prompt workflows and computational scripts used for performance evaluation, case study analysis, and user experience assessments. These resources directly support the results and analyses presented in the main manuscript.

---

## 📂 Directory Overview

code/  
├── agent/                                # iDesignGPT prompt structures and agent workflows  
├── quantitative insights into case study/ # Scripts for case study quantitative analysis  
├── performance evaluation/                # Scripts for Delphi-based expert evaluation analysis  
└── user experience/                       # User study data analysis (CSI, NASA-TLX, WSM)  

---

## 📌 Module Descriptions

### 1. `agent/`
Contains prompt structures and workflow definitions for iDesignGPT agents. These scripts define how large language models interact with engineering design processes, including concept generation stages.

Subfolders correspond to six structured concept generation methods:
- Biomimetic design
- Brainstorming
- Functional Structure Decomposition
- Morphological analysis
- SCAMPER
- TRIZ

> **Note**: The core functionality is built upon prompt engineering rather than traditional executable code. These prompts are designed for deployment within the FastGPT platform to facilitate interactive design exploration and optimization.

---

### 2. `quantitative insights into case study/`
Contains scripts for analyzing design space coverage, diversity, and novelty. These scripts support quantitative case study insights and correspond to Figures 4b–4h in the main manuscript. Key analyses include:
- Word cloud visualization (`fig4b_wordcloud.py`)
- Topic modeling using LDA (`fig4cd_topic_modeling.py`)
- Design space exploration using UMAP (`fig4ef_design_space_analysis.py`)
- Coverage, diversity, and novelty analysis (`fig4f_coverage_diversity_novelty_analysis.py`)
- Customer requirement satisfaction distribution analysis (`fig4h_probability_distribution_for_customer_requirement_satisfaction_scores.m`)


---

### 3. `performance evaluation/`
Includes MATLAB scripts for Delphi-based expert evaluation analysis. These scripts implement a structured multi-round evaluation process to assess the consistency and robustness of expert ratings.

**Key Features:**
- Conducts item-level robustness assessment following Round 1 evaluations.
- Computes Kendall’s coefficient of concordance (W) and tests significance via Chi-square analysis.
- Applies refined statistical thresholds for Mean, Standard Deviation (StdDev), Coefficient of Variation (CV), and Full-Score Rate (FSR).
- Classifies evaluation items as 'Keep', 'Consider', 'Recommend Drop', or 'Strongly Drop' based on predefined criteria.
- Exports CSV files for boxplot visualization and Excel reports for final evaluation decisions.
- Visualizes expert agreement using Kendall’s W bar charts.

---

### 4. `user experience/`
Includes reliability and factor analysis scripts for evaluating user experience using three instruments:
- Creativity Support Index (CSI)
- NASA Task Load Index (NASA-TLX)
- Workflow-Specific Metrics (WSM)

Outputs include Cronbach’s Alpha, KMO and Bartlett’s test results, factor loadings (Supplementary Tables S24–S26), and scree plots (Supplementary Figure S18).

---

## 🚀 How to Use

- Agent prompts should be deployed on the FastGPT platform.
- MATLAB scripts require MATLAB R2021a or later.
- Python scripts are compatible with Python 3.8+.
- Results are exported in `.xlsx` and `.csv` formats for reproducibility.

---

