import pandas as pd

data = pd.read_csv("D:\AI\Day-8\coffee_shop_sales.csv")

print(data.head())
# print(data.tail())

# print(data.info())
# print(data.describe())
data['total']=data['transaction_qty'] * data['unit_price']
print(data.head())