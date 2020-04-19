'''
This plots Trend charts of selected countries strting from January 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

#List of the countries to be ploted
cc:list = ["US", "CA", "IT", "FR", "GB", "DE", "JP", "KR", "SG", "IN", "BD", "PK", "NP", "LK", "BT", "MV", "NZ", "AU", "SC", "IS", "FI", "NO", "DK", "TW"]
countryName:list = ["USA", "Canada", "Italy", "France", "UK", "Germany", "Japan", "South Korea", "Singapore", "India",
                    "Bangladesh", "Pakistan", "Nepal", "Sri Lanka", "Bhutan", "Maldives", "New Zealand", "Australia", "Seychelles", "Iceland", "Finland", "Norway", "Denmark", "Taiwan"]

# cc:list = ["BD", "DK", "FI", "DE",  "IS", "NZ", "NO", "TW"]
# countryName:list = ["Bangladesh", "Denmark", "Finland", "Germany", "Iceland", "New Zealand", "Norway", "Taiwan"]

#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")
startDate="2020-02-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")

#Web scrape the data for selected countries startDate = 2020-02-01 and endDate=today and save to country specific .csv files
for i in cc:
    url="http://api.coronatracker.com/v3/analytics/trend/country?countryCode={}&startDate={}&endDate={}".format(i, startDate, endDate)
    r = requests.get(url)
    df = pd.DataFrame.from_dict(r.json())
    df["last_updated"] = pd.to_datetime(df.last_updated).dt.date
    df.to_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(i), index=True)

#Now read the country specific file and plot the line graph
k=0
for j in cc:
    fig, ax = plt.subplots()
    cv = pd.read_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(j))
    tc= cv["total_confirmed"].iloc[-1]
    tr= cv["total_recovered"].iloc[-1]
    td= cv["total_deaths"].iloc[-1]
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_confirmed', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_deaths', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_recovered', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax.set_xlabel("Trend from February 01, 2020 until today")
    ax.set_ylabel("Number of cases")
    plt.suptitle(today)
    ax.legend(['Total Cases {}'.format(tc), 'Total Deaths {}'.format(td), 'Total Recovers {}'.format(tr)], fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()
    k += 1

