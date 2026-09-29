import pandas as pd

monthly_summary = pd.read_csv("outputs/reports/monthly_summary.csv")
expense_by_category = pd.read_csv("outputs/reports/expense_by_category.csv")

highest_category = expense_by_category.loc[
    expense_by_category["amount"].idxmax()
]

highest_expense_month = monthly_summary.loc[
    monthly_summary["total_expense"].idxmax()
]

highest_income_month = monthly_summary.loc[
    monthly_summary["total_income"].idxmax()
]

highest_savings_month = monthly_summary.loc[
    monthly_summary["savings"].idxmax()
]

correlation = monthly_summary["total_income"].corr(
    monthly_summary["total_expense"]
)

report = f"""PERSONAL FINANCE INSIGHTS
RESULTS AND INTERPRETATION

1. Highest Spending Category
Category: {highest_category["category"]}
Amount: {highest_category["amount"]:.2f}

2. Highest Expense Month
Year: {int(highest_expense_month["year"])}
Month: {int(highest_expense_month["month"])}
Total Expense: {highest_expense_month["total_expense"]:.2f}

3. Highest Income Month
Year: {int(highest_income_month["year"])}
Month: {int(highest_income_month["month"])}
Total Income: {highest_income_month["total_income"]:.2f}

4. Highest Savings Month
Year: {int(highest_savings_month["year"])}
Month: {int(highest_savings_month["month"])}
Savings: {highest_savings_month["savings"]:.2f}

5. Income and Expense Relationship
Correlation: {correlation:.4f}

Interpretation:
The analysis identifies the expense categories and months with the highest financial activity. The highest spending category represents the category with the largest total recorded expense. Monthly income and expense values show how financial activity changes over time. The correlation value indicates a positive relationship between monthly income and monthly expenses in this dataset.

Note:
Monthly income is derived by aggregating individual income transactions. The dataset does not contain a separate payment-mode field.
"""

with open("outputs/reports/results_interpretation.txt", "w") as file:
    file.write(report)

print("Stage 8 completed successfully.")
print()
print(report)
print()
print("Results report saved in outputs/reports/")
