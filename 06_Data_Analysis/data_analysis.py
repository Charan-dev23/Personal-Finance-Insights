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
output:

DESCRIPTIVE STATISTICS
----------------------
count      14.000000
mean     1049.500000
std       874.059209
min        45.000000
25%       413.000000
50%       874.500000
75%      1379.000000
max      2809.000000
Name: amount, dtype: float64

HIGHEST SPENDING CATEGORY
--------------------------
category    Loan given
amount          2809.0
Name: 0, dtype: object

HIGHEST EXPENSE MONTH
---------------------
year             2025.0
month               3.0
total_income     3092.0
total_expense    3272.0
savings          -180.0
Name: 2, dtype: float64

HIGHEST INCOME MONTH
---------------------
year             2025.0
month               9.0
total_income     5730.0
total_expense    2906.0
savings          2824.0
Name: 8, dtype: float64

HIGHEST SAVINGS MONTH
----------------------
year             2025.0
month               9.0
total_income     5730.0
total_expense    2906.0
savings          2824.0
Name: 8, dtype: float64

INCOME-EXPENSE CORRELATION
--------------------------
0.7675041682535949
