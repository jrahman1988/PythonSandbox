'''
This plots Trend charts of selected countries starting from April 01, 2020 until today.
Webscraping to GET JSON formatted response, then convert into DF
'''
import pandas as pd
import requests
import datetime
from matplotlib import pyplot as plt

# cc:list = ["BD"]
# countryName:list = ["Bangladesh"]

cc:list = ["BD", "CA", "US", "RU", "IN", "PK", "IL", "PS"]
countryName:list = ["Bangladesh", "Canada", "USA", "Russia", "India", "Pakistan", "Israel", "Palestine"]

#Format the date time to present on the graph
dt = datetime.datetime.now()
endDate = dt.strftime("%Y"+"-"+"%m"+"-"+"%d")
startDate="2020-04-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")

#Web scrape the data for selected countries startDate = 2020-04-01 and endDate=today and save to country specific .csv files
for i in cc:
    url="http://api.coronatracker.com/v3/analytics/trend/country?countryCode={}&startDate={}&endDate={}".format(i, startDate, endDate)
    r = requests.get(url)
    df = pd.DataFrame.from_dict(r.json())
    df["last_updated"] = pd.to_datetime(df.last_updated).dt.date
    df.to_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(i), index=True)

#Now read the country specific file and plot the line graph
tc_list:list = []
tr_list:list = []
td_list:list = []
k=0
for j in cc:
    fig, ax = plt.subplots()
    cv = pd.read_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(j))

    #Read the last row for today's data from the country specific list
    tc= cv["total_confirmed"].iloc[-1]
    tr= cv["total_recovered"].iloc[-1]
    td= cv["total_deaths"].iloc[-1]

    #Read the last row for today's data from the country specific list
    tc_sevendaysbefore= cv["total_confirmed"].iloc[-7]
    tr_sevendaysbefore= cv["total_recovered"].iloc[-7]
    td_sevendaysbefore= cv["total_deaths"].iloc[-7]

    #Save country specific data in a list where each element will be each country's data (tobe used in PIE plot)
    tc_list.append(tc)
    tr_list.append(tr)
    td_list.append(td)

    recovery_rate = round((tr/tc * 100),1)
    death_rate = round((td/tc * 100),1)

    tc_deltasincelastweek = (tc - tc_sevendaysbefore)
    tr_deltasincelastweek = (tr - tr_sevendaysbefore)
    td_deltasincelastweek = (td - td_sevendaysbefore)

    tc_percentChangesincelastweek:float = round ((tc_deltasincelastweek/tc_sevendaysbefore *100),1)
    tr_percentChangesincelastweek:float = round ((tr_deltasincelastweek/tr_sevendaysbefore *100),1)
    td_percentChangesincelastweek:float = round ((td_deltasincelastweek/td_sevendaysbefore *100),1)

    ax = cv.plot(kind='hist', x='last_updated', y=['total_confirmed', 'total_deaths', 'total_recovered'] , rot=15, figsize=(16,6), grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
    ax.set_xlabel("Trend from April 01, 2020 until today")
    ax.set_ylabel("Number of cases")
    plt.suptitle(today)
    ax.legend(['Total Cases {0} --> Change from last week: {1}=(+{2}%)'.format(tc, tc_deltasincelastweek, tc_percentChangesincelastweek),
               'Total Deaths {0} [{1}% of total cases] --> Change from last week: {2}=(+{3}%)' .format(td, death_rate, td_deltasincelastweek, td_percentChangesincelastweek),
               'Total Recovers {0} [{1}% of total cases] --> Change from last week: {2}=(+{3}%)'.format(tr, recovery_rate, tr_deltasincelastweek, tr_percentChangesincelastweek)],
              fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()
    k += 1

#Sum up all countries total cases which will be used for PIE char plotting
k=0
tclist_total:int = 0
trlist_total:int = 0
tdlist_total:int = 0
for i in countryName:
    tclist_total = tclist_total + tc_list[k]
    trlist_total = trlist_total + tr_list[k]
    tdlist_total = tdlist_total + td_list[k]
    k += 1

# Pie chart parameters setup
labels = countryName
tcsizes = tc_list
trsizes = tr_list
tdsizes = td_list
tccolours = ['pink', 'gold', 'indianred', 'khaki', 'cyan', 'green']
trcolours = ['limegreen', 'tomato', 'orange', 'aqua', 'salmon', 'plum']
tdcolours = ['silver', 'grey', 'lightsalmon', 'slategray', 'tan', 'darkgray']

# Pie chart for plotting: Total cases
fig2, ax2 = plt.subplots()
ax2.pie(tcsizes, labels=labels, colors=tccolours, autopct='%1.f%%', shadow=True, startangle=100)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set(aspect="equal", title='Total Cases in AG Countries as of {} = {}'.format(todayDate, tclist_total))
plt.show()

# Pie chart for plotting: Total recoveries
fig3, ax2 = plt.subplots()
ax2.pie(trsizes, labels=labels, colors=trcolours, autopct='%1.f%%', shadow=True, startangle=100)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set(aspect="equal", title='Total Recoveries in AG Countries as of {} = {}'.format(todayDate, trlist_total))
plt.show()

# Pie chart for plotting: Total deaths
fig4, ax2 = plt.subplots()
ax2.pie(tdsizes, labels=labels, colors=tdcolours, autopct='%1.f%%', shadow=True, startangle=100)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set(aspect="equal", title='Total Deaths in AG Countries as of {} = {}'.format(todayDate, tdlist_total))
plt.show()