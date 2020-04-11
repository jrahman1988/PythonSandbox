'''
This plots Trend charts of selected countries strting from January 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

#List of the countries to be ploted
cc:list = ["US", "CA", "IT", "FR", "GB", "DE", "JP", "KR", "SG", "IN", "BD", "PK", "NP", "LK", "BT", "MV", "NZ"]
countryName:list = ["USA", "Canada", "Italy", "France", "UK", "Germany", "Japan", "South Korea", "Singapore", "India",
                    "Bangladesh", "Pakistan", "Nepal", "Sri Lanka", "Bhutan", "Maldives", "New Zealand"]


#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")
startDate="2020-01-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")

# #Graph size matters
# desired_width=360
# pd.set_option('display.width', desired_width)
# pd.set_option('display.max_columns',120)

#Web scrape the data for selected countries startDate = 2020-01-01 and endDate=today and save to country specific .csv files
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
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_confirmed', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_deaths', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax= cv.plot(kind='line', figsize=(10,5), x='last_updated', y='total_recovered', grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax.set_xlabel("Trend from January 01, 2020 until today")
    ax.set_ylabel("Number of cases")
    plt.suptitle(today)
    plt.show()
    k += 1