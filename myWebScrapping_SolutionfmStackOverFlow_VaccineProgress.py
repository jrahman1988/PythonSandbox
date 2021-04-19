'''
Someone replied to my question at Stack Over Flow:
https://stackoverflow.com/questions/67145023/how-to-grab-a-complete-table-hidden-beyond-show-all-by-web-scraping-in-python?noredirect=1#comment118687563_67145023
'''
import pandas as pd
import requests
import io
from bs4 import BeautifulSoup
#
dfraw = pd.read_csv(io.StringIO(requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv").text))
dfraw["date"] = pd.to_datetime(dfraw["date"])
dfraw.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFromSOF_v01.csv", index=True)

dfraw.sort_values(["iso_code","date"]).groupby("iso_code", as_index=False).last()
dfraw = dfraw.reset_index(drop=True)
dfraw.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFromSOF.csv", index=True)
print(type(dfraw))
print(dfraw.info())
print(dfraw.head(40))
print(dfraw.tail(40))