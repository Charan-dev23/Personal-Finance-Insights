import pandas as pd

expense_by_category = pd.read_csv("outputs/reports/expense_by_category.csv")
monthly_summary = pd.read_csv("outputs/reports/monthly_summary.csv")

print("DESCRIPTIVE STATISTICS")
print("----------------------")
print(expense_by_category["amount"].describe())

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

print()
print("HIGHEST SPENDING CATEGORY")
print("--------------------------")
print(highest_category)

print()
print("HIGHEST EXPENSE MONTH")
print("---------------------")
print(highest_expense_month)

print()
print("HIGHEST INCOME MONTH")
print("---------------------")
print(highest_income_month)

print()
print("HIGHEST SAVINGS MONTH")
print("----------------------")
print(highest_savings_month)

print()
print("INCOME-EXPENSE CORRELATION")
print("--------------------------")
print(correlation)
