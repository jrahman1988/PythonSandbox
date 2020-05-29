'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
We'll use here the pandas.read_html(), which returns a list of data frames. According to the PANDAS doc:
"This function searches for <table> elements and only for <tr> and <th> rows and <td> elements within
each <tr> or <th> element in the table. <td> stands for “table data”.
Document URL: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html
'''
import pandas as pd
import requests

# GET the response from the web page using requests library, response = a list of dfs
req = requests.get("https://www.worldometers.info/coronavirus/")

# This webpage has multiple tables, we will use the index [1] to fetch the table of our interest, the respose is a list of dfs
df = pd.read_html(req.content)[0]

print(type(df))
print(df.head(10))
print(df.tail(10))
print(df.info())

df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/dataFrom_myWebScrapping_fmWorldometer.csv", index=False)

