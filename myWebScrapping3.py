'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
'''
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from pandas import DataFrame

# GET the response from the web page using requests library
# url = 'https://www.trackcorona.live'
# res = requests.get("https://www.trackcorona.live")
# res = requests.get("https://worldpopulationreview.com/countries/saarc-countries/")
# res = requests.get("https://ourworldindata.org/coronavirus")
res = requests.get("https://www.worldometers.info/coronavirus/")

# PARSE and fetch content using BeutifulSoup method of bs4 library
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')
df = pd.read_html(str(table))[0]

print(tabulate(df[0], headers='keys', tablefmt='psql'))
df = df[0]
print(df)
print(df.info())