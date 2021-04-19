'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
We'll use here the pandas.read_html(), which returns a list of data frames. According to the PANDAS doc:
"This function searches for <table> elements and only for <tr> and <th> rows and <td> elements within
each <tr> or <th> element in the table. <td> stands for “table data”.
Document URL: https://ourworldindata.org/covid-vaccinations#how-many-covid-19-vaccination-doses-have-been-administered
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
#
vaacineProgressResponse = requests.get("https://ourworldindata.org/covid-vaccinations#how-many-covid-19-vaccination-doses-have-been-administered")
response = requests.get("https://ourworldindata.org/covid-vaccinations#how-many-covid-19-vaccination-doses-have-been-administered")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# vaacineProgressContentTable = vaacineProgressContent.find_all('table', class_="data-table")
# if vaacineProgressContentTable is not None and len(vaacineProgressContentTable) > 0:
#     vaacineProgressContentTable = vaacineProgressContentTable[0]
# #
# vaccineDF = pd.read_html(str(vaacineProgressContentTable), displayed_only=False)[0]
# vaccineDF = vaccineDF.reset_index(drop=True)
# print(type(vaccineDF))
# print(vaccineDF.info())
# print(vaccineDF.head(100))
# # print(vaccineDF.tail(10))
# vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFromOurWorldInData_02.csv", index=True)
