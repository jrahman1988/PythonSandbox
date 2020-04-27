'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
Reference document URL: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html
We'll use the Solar Power usage data extracted by web scraping and construct the data frame to plot the trend
Also construct a linear regression model using linear_regression class of sklearn lib to predict trend of a future year
'''
import pandas as pd
import requests
from matplotlib import pyplot as plt
import datetime
from sklearn import linear_model
from sklearn.impute import SimpleImputer
import numpy as np

#
#Format the date time to present on the graph
dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
#
#GET the response from the web page using requests library
req = requests.get("https://www.eia.gov/opendata/qb.php?category=2134732&sdid=INTL.36-12-BGD-BKWH.A")
df = pd.read_html(req.content)[0]
df=df.sort_values(by=list(df.columns),axis=0)
print(df.info())
#
#Convert the generated values from billion to mega
df['Value'] = df['Value'].multiply(1000)
#
#Modify the existing string 'billion kilowatthours' string to 'Million kWH' of 'Units' column
#--here we take one column which is a seris, then apply the Series.str.replace(self, pat, repl, n=-1, case=None, flags=0, regex=True)--
df['Units'] = df['Units'].str.replace('billion kilowatthours', 'Million kWH')
#
#Fill all NaN values with 0
df = df.fillna(0)
#
#Drop the row for Period = 2018
df = df.drop(df.index[0])
#
#Rename the columns
df = df.rename(columns={'Period':'Year', 'Value': 'Amount_MkWh', 'Units': 'Million kWH'})
print(df.info())
#
#Remove all rows with 0
df = df[df.Amount_MkWh != 0]
#
'''
LINEAR REGRESSION MODEL:
1. Create a Linear Regression model using linear_model class of sklearn lib
'''
# df = df.sort_values(["Year", "Amount_MkWh"], ascending=False)
# df=df.sort_values(by=list(df.columns),axis=0)
df_X:int = df[['Year']]
df_y = df.Amount_MkWh
print(df_X)
print(df_y)
print(df[['Amount_MkWh']])

reg = linear_model.LinearRegression()
reg.fit(df_X, df_y)

plt.xlabel('Year')
plt.ylabel('Trillion kWH')
# plt.scatter(df_X, df_y, color='red', marker='+')
plt.plot(df_X, reg.predict(df[['Amount_MkWh']]), color='blue')
plt.show()

'''
PREDICTION WITH LINEAR REGRESSION MODEL:
'''
predicted_amount = np.around(reg.predict([[2020]]), decimals=2)
print("The projected generated amount of year 2020 is: {} MkWh".format(predicted_amount))
