
import pandas as pd

expenses = pd.read_csv("dataset/raw/Expenses_clean.csv")
income = pd.read_csv("dataset/raw/Income_clean.csv")

print("EXPENSE DATA")
print("------------")
print("Rows and columns:", expenses.shape)
print("Columns:", list(expenses.columns))
print()
print(expenses.head())

print()
print("INCOME DATA")
print("-----------")
print("Rows and columns:", income.shape)
print("Columns:", list(income.columns))
print()
print(income.head())
output EXPENSE DATA
------------
Rows and columns: (938, 6)
Columns: ['date_time', 'category', 'account', 'amount', 'currency', 'tags']

             date_time          category account  amount currency   tags
0  2025-11-30 00:00:00            Health  acct_1   114.0      BYN  tag_1
1  2025-11-29 00:00:00              Food  acct_1     5.0      BYN  tag_1
2  2025-11-27 00:00:00  Public transport  acct_2     1.0      BYN  tag_1
3  2025-11-27 00:00:00              Cafe  acct_1    10.0      BYN  tag_1
4  2025-11-27 00:00:00  Public transport  acct_2     1.0      BYN  tag_1

INCOME DATA
-----------
Rows and columns: (349, 6)
Columns: ['date_time', 'category', 'account', 'amount', 'currency', 'tags']

             date_time     category account  amount currency      tags
0  2025-11-29 00:00:00          Job  acct_1    49.0      BYN     tag_1
1  2025-11-29 00:00:00          Job  acct_1    18.0      BYN     tag_2
2  2025-11-29 00:00:00          Job  acct_1    32.0      BYN     tag_3
3  2025-11-29 00:00:00          Job  acct_1   109.0      BYN     tag_4
4  2025-11-28 00:00:00  Second work  acct_1   132.0      BYN  2th_work
