import pandas as pd

"""

df = pd.read_csv('Cars-Datasets-2025.csv', encoding='windows-1251')

print(df.head(5))

print(df.info())

print(df.describe())
"""
df = pd.read_csv('dz.csv')

print(df.head(12))

group = df.groupby('City')['Salary'].mean()

print(group)

