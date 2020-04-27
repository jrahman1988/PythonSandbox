'''
This plots Trend charts of selected countries strting from January 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")
startDate="2020-01-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")

#Web scrape the data for selected countries startDate = 2020-01-01 and endDate=today and save to country specific .csv files
url="https://api.coronatracker.com/v3/stats/worldometer/totalTrendingCases"
r = requests.get(url)
df = pd.DataFrame.from_dict(r.json())
# print(df.info())
df["lastUpdated"] = pd.to_datetime(df.lastUpdated).dt.date
df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/GlobalTestData.csv", index=True)

#Data from flightradar24.com
cv = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/commercial_flightsApr262020.csv")
cv["DateTime"] = pd.to_datetime(cv.DateTime).dt.date
# print(cv.info())

fig, ax = plt.subplots()
ax3 = ax.twinx()
rspine = ax3.spines['right']
rspine.set_position(('axes', 1.05))
ax3.set_frame_on(True)
ax3.patch.set_visible(False)
fig.subplots_adjust(right=0.8)

tc= df["totalConfirmed"].iloc[0]
tr= df["totalRecovered"].iloc[0]
td= df["totalDeaths"].iloc[0]
nf= cv["Number of flights"].iloc[-1]

ax3= cv.plot(kind='line', figsize=(10,5), x='DateTime', y='Number of flights', color='red', linewidth=1.5, grid=True, title="Corona effect on global commercial flights", ax=ax3)

ax= df.plot(kind='line', figsize=(10,5), x='lastUpdated', y='totalConfirmed', grid=True, title="Corona effect on global commercial flights", ax=ax)
ax= df.plot(kind='line', figsize=(10,5), x='lastUpdated', y='totalDeaths', color='black',  grid=True, title="Corona effect on global commercial flights", ax=ax)
ax= df.plot(kind='line', figsize=(10,5), x='lastUpdated', y='totalRecovered', style='g-', grid=True, title="Corona effect on global commercial flights", ax=ax)
ax.set_xlabel("Since January 16, 2020 ~ today")
ax.set_ylabel("Global totals of CoViD cases")
ax3.set_ylabel("Number of commercial flights")
plt.suptitle(today)

ax.legend(['Total Cases {}'.format(tc), 'Total Deaths {}'.format(td), 'Total Recovers {}'.format(tr)], fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='lower left')
ax3.legend(['No. of Flights today {}'.format(nf)], fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='center left')
plt.show()
