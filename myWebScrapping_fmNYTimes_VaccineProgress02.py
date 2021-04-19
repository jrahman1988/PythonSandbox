'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
We'll use here the pandas.read_html(), which returns a list of data frames. According to the PANDAS doc:
"This function searches for <table> elements and only for <tr> and <th> rows and <td> elements within
each <tr> or <th> element in the table. <td> stands for “table data”.
Document URL: https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
#
vaccineDF = pd.read_html('https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html')[0]
vaccineDF = vaccineDF.reset_index(drop=True)
print(vaccineDF.head(100))
print(vaccineDF.tail(100))
vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFromNYT_02.csv", index=True)
