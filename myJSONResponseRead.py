'''
Reading the API response from a web service GET call which returns JSON formatted file
'''
import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

trend = pd.read_json("http://api.coronatracker.com/v3/stats/worldometer/totalTrendingCases")


# Fill all NaN values with 0
trend = trend.fillna(0)

#Modify the 'date_posted' key values to YYY-mm-dd format (using Pandas syntax: Series.dt.date)
# trend["lastUpdated"] = pd.to_datetime(trend.lastUpdated).dt.date

#Rename the columns for better readability
trend = trend.rename(columns={'totalConfirmed':'Total cases',
                              'totalDeaths': 'Total deaths',
                              'totalRecovered': 'Total recovered',
                              'lastUpdated': 'Date'})

# print(trend.Date)
print(trend.head(6))
print(trend.shape)
print(trend.info())
