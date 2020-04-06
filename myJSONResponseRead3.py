'''
Reading the API response from a web service GET call which returns JSON formatted file
'''
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

r = requests.get("http://api.eia.gov/series/?api_key=YOUR_API_KEY_HERE&series_id=INTL.785-3-DZA-TBPD.M")
x = r.json()
df = pd.DataFrame(x)
print (df)

# Fill all NaN values with 0
df = df.fillna(0)

#Write the DF to corona_virus.csv by excluding the DF index and appending with today's date with file name
df.to_json("~/Desktop/Learning/Sandbox/PythonSandbox/Data/USEnergy.csv")

# print(trend.Date)
print(df.head(20))
print(df.shape)
print(df.info())
