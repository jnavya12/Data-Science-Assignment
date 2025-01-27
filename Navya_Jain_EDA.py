# -*- coding: utf-8 -*-
"""Task 1 Navya Jain

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hQYd8CFFVZCkOjTeu5SPUStiq_kB_ZO6
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv('Customers.csv')
products = pd.read_csv('Products.csv')
transactions = pd.read_csv('Transactions.csv')

print(customers.head())
print(products.head())
print(transactions.head())

print(customers.isnull().sum())
print(products.isnull().sum())
print(transactions.isnull().sum())

customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])

merged_data = transactions.merge(customers, on='CustomerID', how='left').merge(products, on='ProductID', how='left')

region_sales = merged_data.groupby('Region')['TotalValue'].sum().sort_values(ascending=False)
top_products = merged_data.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title('Revenue by Region')
plt.show()