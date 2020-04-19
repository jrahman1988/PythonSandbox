'''
This plots Trend charts of selected countries strting from January 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

#List of the countries to be ploted
cc:list = ["BD", "IN", "PK", "NP",  "LK", "US", "CA", "GB"]
countryName:list = ["Bangladesh", "India", "Pakistan", "Nepal", "Sri Lanka", "USA", "Canada", "UK"]

#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")
startDate="2020-04-01"
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

    recovery_rate = round((tr/tc * 100),1)
    death_rate = round((td/tc * 100),1)

    ax = cv.plot(kind='bar', x='last_updated', y=['total_confirmed', 'total_deaths', 'total_recovered'] , rot=12, figsize=(16,6), grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax.set_xlabel("Trend from April 01, 2020 until today")
    ax.set_ylabel("Number of cases")
    plt.suptitle(today)
    ax.legend(['Total Cases {}'.format(tc), 'Total Deaths {0} [{1}% of total cases]'.format(td, death_rate), 'Total Recovers [{1}% of total cases]'.format(tr, recovery_rate)], fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()
    k += 1