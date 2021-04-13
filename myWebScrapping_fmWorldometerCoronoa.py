'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
We'll use here the pandas.read_html(), which returns a list of data frames. According to the PANDAS doc:
"This function searches for <table> elements and only for <tr> and <th> rows and <td> elements within
each <tr> or <th> element in the table. <td> stands for “table data”.
Document URL: https://www.worldometers.info/coronavirus/
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup

# GET the response from the web page using requests library, response = a list of dfs
req = requests.get("https://www.worldometers.info/coronavirus/")
# print(req.content[100])
page = BeautifulSoup(req.content, 'html.parser')

table = page.find_all('table',id="main_table_countries_today")[0]
# print(table)

# df = pd.read_html(str(table))[0]
df = pd.read_html(str(table), displayed_only=False)[0]


# table_corona = pd.read_html('http://www.worldometers.info/coronavirus')
# print(f'Total tables: {len(table_corona)}')

# table_corona = pd.read_html('https://www.worldometers.info/coronavirus', match='main_table_countries_today')
# print(len(df)

# This webpage has multiple tables, we will use the index [0] to fetch the table of our interest, the respose is a list of dfs
# df = pd.read_html(req.content)[0]
print(type(df))
print(df.head(10))
print(df.tail(10))
print(df.info())
#
df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/globalCoronaCasesData.csv", index=False)

# GET the response from the web page using requests library, response = a list of dfs
req = requests.get("https://en.wikipedia.org/wiki/Deployment_of_COVID-19_vaccines#covid-19-pandemic-vaccination")

# This webpage has multiple tables, we will use the index [0] to fetch the table of our interest, the respose is a list of dfs
df = pd.read_html(req.content)[0]

print(type(df))
print(df.head(10))
print(df.tail(10))
print(df.info())

