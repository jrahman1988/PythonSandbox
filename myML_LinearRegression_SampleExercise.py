'''
This plots Trend charts of selected countries starting from April 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/BDEnergySampleData2.csv")
print(df.info())

'''
LINEAR REGRESSION MODEL:
1. Create a Linear Regression model using linear_model class of sklearn lib
'''
df_X:int = df[['Year']]
df_y = df.Value
print(df_X)
print(df_y)
print(df[['Year']])

reg = linear_model.LinearRegression()
reg.fit(df_X, df_y)

plt.xlabel('Year')
plt.ylabel('Trillion kWH')
plt.scatter(df_X, df_y, color='red', marker='+')
plt.plot(df_X, reg.predict(df[['Value']]), color='blue')
plt.show()

'''
PREDICTION WITH LINEAR REGRESSION MODEL:
'''
predicted_amount = np.around(reg.predict([[2020]]), decimals=2)
print("The projected generated amount of year 2020 is: {} MkWh".format(predicted_amount))