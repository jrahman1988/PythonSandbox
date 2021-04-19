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
vaacineProgressResponse = requests.get("https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html")
vaacineProgressContent = BeautifulSoup(vaacineProgressResponse.content, 'html.parser')
vaacineProgressContentTable = vaacineProgressContent.find_all('table', class_="g-summary-table svelte-2wimac")
if vaacineProgressContentTable is not None and len(vaacineProgressContentTable) > 0:
    vaacineProgressContentTable = vaacineProgressContentTable[0]
#
vaccineDF = pd.read_html(str(vaacineProgressContentTable), displayed_only=False)[0]
vaccineDF = vaccineDF.reset_index(drop=True)
# print(type(vaccineDF))
# print(vaccineDF.info())
print(vaccineDF.head(100))
# print(vaccineDF.tail(10))
vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFromNYT_01.csv", index=True)
