'''
Using dataframe.corr() this program calculates the correlation R values of values in columns of a dataframe
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

# cc:list = ["BD"]
# countryName:list = ["Bangladesh"]

cc:list = ["BD", "IN", "CA", "US", "NZ", "AU", "GB"]
countryName:list = ["Bangladesh", "India", "Canada", "USA", "New Zealand", "Australia", "UK"]

#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")

startDate="2020-04-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")

#Web scrape the data for selected countries startDate = 2020-02-01 and endDate=today and save to country specific .csv files
k=0
for i in cc:
    req = "http://api.coronatracker.com/v5/analytics/trend/country?countryCode={}&startDate={}&endDate={}".format(i, startDate, endDate)
    cv= pd.read_json(req)
    cv["last_updated"] = pd.to_datetime(cv.last_updated).dt.date

    cv.index = cv.index + 1
    corr_tctd:float = round(cv['total_confirmed'].corr(cv['total_deaths'], method='pearson'),2)
    corr_tctr:float = round(cv['total_confirmed'].corr(cv['total_recovered'], method='pearson'),2)

    fig, ax = plt.subplots()
    tc = cv["total_confirmed"].iloc[-1]
    tr = cv["total_recovered"].iloc[-1]
    td = cv["total_deaths"].iloc[-1]

    #Read one month before data
    tc_onemonthbefore= cv["total_confirmed"].iloc[-30]
    tr_onemonthbefore= cv["total_recovered"].iloc[-30]
    td_onemonthbefore= cv["total_deaths"].iloc[-30]

    tc_deltasincelastmonth = (tc - tc_onemonthbefore)
    tr_deltasincelastmonth = (tr - tr_onemonthbefore)
    td_deltasincelastmonth = (td - td_onemonthbefore)

    cv.reset_index().plot(kind='scatter', figsize=(10, 5), x='index', y='total_confirmed', color='red', grid=True,
                         title="Trend of {}".format(countryName[k]), marker = 's', ax=ax)
    cv.reset_index().plot(kind='scatter', figsize=(10, 5), x='index', y='total_deaths', color='black', grid=True,
                          title="Trend of {}".format(countryName[k]), marker = 'o', ax=ax)
    cv.reset_index().plot(kind='scatter', figsize=(10, 5), x='index', y='total_recovered', color='green', grid=True,
                          title="Trend of {}".format(countryName[k]), marker = '^', ax=ax)

    ax.set_xlabel("Since {} ~ today".format(startDate))
    ax.set_ylabel("Number of CoViD cases")

    ax.legend(['Total Cases today: {0} [**one month before: {1}**]'.format(tc, tc_onemonthbefore),
               'Total Deaths today: {0} [**one month before: {1}**] --> Corr. cases vs. deaths: {2}'.format(td, td_onemonthbefore, corr_tctd),
               'Total Recovery today: {0} [**one month before: {1}**] --> Corr. cases vs. recovery: {2}'.format(tr, tr_onemonthbefore, corr_tctr)],
                fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='upper left')

    plt.suptitle(today)
    plt.show()
    k += 1