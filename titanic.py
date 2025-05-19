import pandas as pd


data = pd.read_csv("tested.csv")
print(data.head())
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())
print(data['Cabin'].value_counts())