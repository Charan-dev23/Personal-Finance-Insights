
import pandas as pd

expenses = pd.read_csv("dataset/processed/cleaned_expenses.csv")
income = pd.read_csv("dataset/processed/cleaned_income.csv")

expenses["date_time"] = pd.to_datetime(expenses["date_time"])
income["date_time"] = pd.to_datetime(income["date_time"])

expenses["year"] = expenses["date_time"].dt.year
expenses["month"] = expenses["date_time"].dt.month

income["year"] = income["date_time"].dt.year
income["month"] = income["date_time"].dt.month

expense_by_category = expenses.groupby("category")["amount"].sum().reset_index()
expense_by_category = expense_by_category.sort_values("amount", ascending=False)

expense_by_month = expenses.groupby(["year", "month"])["amount"].sum().reset_index()
expense_by_month = expense_by_month.rename(columns={"amount": "total_expense"})

income_by_month = income.groupby(["year", "month"])["amount"].sum().reset_index()
income_by_month = income_by_month.rename(columns={"amount": "total_income"})

monthly_summary = pd.merge(
    income_by_month,
    expense_by_month,
    on=["year", "month"],
    how="outer"
)

monthly_summary = monthly_summary.fillna(0)

monthly_summary["savings"] = (
    monthly_summary["total_income"] - monthly_summary["total_expense"]
)

monthly_summary = monthly_summary.sort_values(["year", "month"])

expense_by_category.to_csv(
    "outputs/reports/expense_by_category.csv",
    index=False
)

expense_by_month.to_csv(
    "outputs/reports/expense_by_month.csv",
    index=False
)

income_by_month.to_csv(
    "outputs/reports/income_by_month.csv",
    index=False
)

monthly_summary.to_csv(
    "outputs/reports/monthly_summary.csv",
    index=False
)

print("EXPENSE BY CATEGORY")
print("-------------------")
print(expense_by_category.head(10))

print()
print("MONTHLY FINANCIAL SUMMARY")
print("-------------------------")
print(monthly_summary)

output 
EXPENSE BY CATEGORY
-------------------
             category  amount
9          Loan given  2809.0
10              Other  2699.0
4                Food  1528.0
1                Cafe  1413.0
5               Gifts  1277.0
0   Bought for myself  1273.0
8             Leisure   945.0
6              Health   804.0
12               Taxi   770.0
2             Clothes   548.0

MONTHLY FINANCIAL SUMMARY
-------------------------
    year  month  total_income  total_expense  savings
0   2025      1        1864.0          969.0    895.0
1   2025      2        1647.0          615.0   1032.0
2   2025      3        3092.0         3272.0   -180.0
3   2025      4        1423.0         1167.0    256.0
4   2025      5        2010.0          633.0   1377.0
5   2025      6        2227.0          682.0   1545.0
6   2025      7        1967.0          811.0   1156.0
7   2025      8        2359.0          828.0   1531.0
8   2025      9        5730.0         2906.0   2824.0
9   2025     10        2993.0         1928.0   1065.0
10  2025     11        1317.0          882.0    435.0
