import pandas as pd

data = pd.read_csv("up73-dwdy_version_13.csv")

print(data.head())
print(data.tail())

print(data.info())
print(data.describe())