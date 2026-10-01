# Personal Finance Insights

## A Data Analysis Project on Personal Expense & Saving Behavior

### Project Overview

Personal Finance Insights is a data analysis project that studies income and expense transaction data to identify spending patterns, monthly financial trends, and the relationship between income, expenses, and savings.

The project follows an eight-stage data analysis workflow using Python, Pandas, Matplotlib, and Seaborn.

## Objectives

- Analyze personal expense data to identify important spending patterns.
- Clean and preprocess transaction data for reliable analysis.
- Study the relationship between monthly income and expenses.
- Calculate monthly savings from income and expense values.
- Identify high-spending categories and financially significant months.
- Present findings using clear visualizations.

## Problem Statement

Managing personal finances through manual tracking can make it difficult to identify spending patterns and understand how expenses affect savings. This project applies data analysis techniques to transaction data to identify spending trends, monthly financial activity, and the relationship between income and expenses.

## Scope and Significance

The project covers data loading, filtering, date extraction, validation, cleaning, aggregation, statistical analysis, visualization, and result interpretation.

The analysis helps identify major spending categories, changes in monthly income and expenses, savings patterns, and the relationship between monthly income and monthly expenses.

## Dataset

The project uses two transaction datasets:

- `Expenses_clean.csv`
- `Income_clean.csv`

### Original Dataset Size

**Expenses**

- Records: 938
- Columns: 6

**Income**

- Records: 349
- Columns: 6

### Dataset Columns

- `date_time` — transaction date and time
- `category` — transaction category
- `account` — account identifier associated with the transaction
- `amount` — transaction amount
- `currency` — transaction currency
- `tags` — additional descriptive transaction information

The dataset currency is BYN.

Monthly income is not a raw dataset column. It is derived by aggregating income transaction amounts by year and month.

The dataset files are included in the repository under `dataset/raw/`.

## Data Analysis Workflow

### 01. Data Loading & Reading

Loads the raw expense and income CSV files using Pandas and inspects their structure, columns, record counts, and sample records.

### 02. Data Acquisition & Filtering

Selects the required dataset columns and filters transaction records to retain positive amounts.

### 03. Data Extraction

Converts transaction dates into datetime format and extracts:

- Year
- Month
- Month name

These derived fields support monthly analysis.

### 04. Data Validation & Cleaning

The datasets are checked for:

- Missing values
- Duplicate records
- Invalid dates
- Invalid or non-positive amounts

Cleaning operations include duplicate removal, missing-value handling, date validation, and amount filtering.

### 05. Data Aggregation & Representation

The cleaned datasets are aggregated using Pandas operations such as:

- `groupby()`
- `sum()`
- `sort_values()`
- `merge()`

Monthly income, expenses, and savings are calculated.

Savings are calculated as:

`Savings = Total Income - Total Expense`

### 06. Data Analysis

The project performs:

- Descriptive statistics using `describe()`
- Highest spending category analysis
- Highest expense month analysis
- Highest income month analysis
- Highest savings month analysis
- Correlation analysis between monthly income and monthly expenses

### 07. Data Visualization

The project generates three charts:

1. Expense by Category
2. Monthly Income vs Expense
3. Monthly Savings

The charts are created using Matplotlib and Seaborn.

### 08. Results & Interpretation

The final stage summarizes the important findings and saves the results in:

`outputs/reports/results_interpretation.txt`

## Key Results

- Highest spending category: **Loan given — 2809 BYN**
- Highest expense month: **March 2025 — 3272 BYN**
- Highest income month: **September 2025 — 5730 BYN**
- Highest savings month: **September 2025 — 2824 BYN**
- Income and expense correlation: **0.7675**

The correlation indicates a positive relationship between monthly income and monthly expenses in this dataset. Correlation does not imply causation.

## Team Members & Contributions

| Team Member | Roll Number | Primary Contribution |
|---|---|---|
| M. Uday Sai Reddy | 26B21CS063 | Data Loading, Acquisition & Filtering |
| P. Sai Praneeth | 25B11CS763 | Data Extraction, Validation & Cleaning |
| Y.N.S. Charan | 26B21CS097 | Data Aggregation, Representation & Analysis |
| SK. Masthan | 26B21CS096 | Data Visualization, Results & Interpretation |

All team members are expected to understand the complete project workflow, preprocessing, analysis, visualizations, and conclusions.

## Project Structure

```text
Personal-Finance-Insights/
│
├── 01_Data_Loading_Reading/
├── 02_Data_Acquisition_Filtering/
├── 03_Data_Extraction/
├── 04_Data_Validation_Cleaning/
├── 05_Data_Aggregation_Representation/
├── 06_Data_Analysis/
├── 07_Data_Visualization/
├── 08_Results_Interpretation/
│
├── dataset/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── review-ppts/
│   ├── Review-1 Presentation
│   └── Review-2 Presentation
│
├── .gitignore
├── README.md
└── requirements.txt
```
Limitations
The analysis is based on the available transaction dataset.
The dataset currency is BYN.
Payment mode is not available as a dataset field.
Monthly income is derived from individual income transactions.
The analysis identifies relationships and patterns but does not establish causation.
Conclusion

The project demonstrates an end-to-end data analysis workflow for personal finance data, from raw transaction data loading and cleaning to aggregation, statistical analysis, visualization, and interpretation.

The results provide insights into spending categories, monthly financial activity, savings, and the relationship between income and expenses.


