'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
Reference document URL: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html
'''
import pandas as pd
import requests
from matplotlib import pyplot as plt
import datetime
#
#Format the date time to present on the graph
dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
#
#GET the response from the web page using requests library
req = requests.get("https://www.eia.gov/opendata/qb.php?category=2134732&sdid=INTL.36-12-BGD-BKWH.A")
df = pd.read_html(req.content)[0]
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
df = df.rename(columns={'Period':'Year', 'Value': 'Generated amount in MkWh', 'Units': 'Million kWH'})
#
#Now read the file and plot the line graph
fig, ax = plt.subplots()
ax= df.plot(kind='line', figsize=(10,5), x='Year', y='Generated amount in MkWh', grid=True, title="Yearly trend of solar power generation in Bangladesh", ax=ax)
ax.set_xlabel("Period: 1980 to 2018")
ax.set_ylabel("Trillion kWH")
plt.suptitle(today)
plt.show()
#
#Write to a CSV file
df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/BDSolarPowerGeneration.csv", index=False)

print(df.info())
print(df['Generated amount in MkWh'].head())
print(df['Million kWH'].head())