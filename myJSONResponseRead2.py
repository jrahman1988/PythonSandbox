'''
Reading the API response from a web service GET call which returns JSON formatted file
'''
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

trend = pd.read_json("https://api.eia.gov/category/?api_key=23b38fe06b44db760fef92358e76f678&category_id=1")


# Fill all NaN values with 0
trend = trend.fillna(0)

#Write the DF to corona_virus.csv by excluding the DF index and appending with today's date with file name
trend.to_json("~/Desktop/Learning/Sandbox/PythonSandbox/Data/USEnergy.csv")

# print(trend.Date)
print(trend.head(6))
print(trend.shape)
print(trend.info())
print(trend)
