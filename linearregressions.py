import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn as sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("car_dekho.csv")
print(data.head())
# print(data[['Fuel_Type']].head())
# print(data[["Car_Name"]].head())

sns.scatterplot(y = "Selling_Price", x = "Age", data = data)
# plt.show()
sns.catplot(x = 'Fuel_Type', y = 'Selling_Price', data = data, kind = 'swarm', s = 2)
# plt.show()

print(data.groupby(["Fuel_Type"]).count())

sns.scatterplot(x = "Kms_Driven", y = "Selling_Price", data = data)
plt.show()
sns.catplot(x = 'Seller_Type', y = 'Transmission', data = data, kind = 'swarm', s = 2)
plt.show()

xAge = data["Age"]
yPrice = data["Selling_Price"]
print(xAge)
print(yPrice)