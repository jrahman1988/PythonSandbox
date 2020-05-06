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

date_1 = datetime.datetime.strptime(endDate, "%Y"+"-"+"%m"+"-"+"%d")
fourteenDaysfromToday = (date_1 + datetime.timedelta(days=14)).strftime("%Y"+"-"+"%m"+"-"+"%d")
# print(fourteenDaysfromToday)

startDate="2020-03-01"
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")
fileNameDate = dt.strftime("%b%d%Y")
# print(todayDate)

#Web scrape the data for selected countries startDate = 2020-03-01 and endDate=today and save to country specific .csv files
k=0
for i in cc:
    url="http://api.coronatracker.com/v3/analytics/trend/country?countryCode={}&startDate={}&endDate={}".format(i, startDate, endDate)
    r = requests.get(url)
    df = pd.DataFrame.from_dict(r.json())
    df["last_updated"] = pd.to_datetime(df.last_updated).dt.date
    df.to_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(i), index=True)

    cv = pd.read_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(i))
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

# More work TBD start here..........................

# To find the correlation among the columns using pearson method
# print(cv.info())
# print(cv.describe())
# print(cv.corr(method ='pearson'))
# print(cv.head(10))
# print(cv.tail(10))

#Reset the index with reset_index() so that we can add index as a column
# cv.index = cv.index + 1
# cv.reset_index().plot.scatter(x='index', y='total_confirmed')

# ax= df.plot(kind='line', figsize=(10,5), x='lastUpdated', y='totalConfirmed', grid=True, title="Corona effect on global commercial flights", ax=ax)
# plt.show()

# fig, ax = plt.subplots()
# ax3 = ax.twinx()
# rspine = ax3.spines['right']
# rspine.set_position(('axes', 1.05))
# ax3.set_frame_on(True)
# ax3.patch.set_visible(False)
# fig.subplots_adjust(right=0.8)

# tc= cv["total_confirmed"].iloc[0]
# tr= cv["total_recovered"].iloc[0]
# td= cv["total_deaths"].iloc[0]

# cv.reset_index().plot(kind='scatter', figsize=(10,5), x='index', y='total_confirmed', color='red', grid=True, title="Corona effect on global commercial flights", ax=ax)
# cv.reset_index().plot(kind='scatter', figsize=(10,5), x='index', y='total_deaths', color='black',  grid=True, title="Corona effect on global commercial flights", ax=ax)
# cv.reset_index().plot(kind='scatter', figsize=(10,5), x='index', y='total_recovered', color='green',  grid=True, title="Corona effect on global commercial flights", ax=ax)

# ax.set_xlabel("Since January 16, 2020 ~ today")
# ax.set_ylabel("Global totals of CoViD cases")
# ax3.set_ylabel("Number of commercial flights")
# plt.suptitle(today)

# ax.legend(['Total Cases {}'.format(tc), 'Total Deaths {}'.format(td), 'Total Recovers {}'.format(tr)], fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='lower left')
# ax3.legend(['No. of Flights today {}'.format(nf)], fancybox=True, framealpha=1, shadow=True, borderpad=1, loc='center left')
# plt.show()

'''
#Now read the country specific file and plot the line graph
tc_list:list = []
tr_list:list = []
td_list:list = []
k=0
for j in cc:
    fig, ax = plt.subplots()
    cv = pd.read_csv("~/Desktop/Learning/DataScience/TestData/TrendData_{}.csv".format(j))

    #Data for Linear Regression:
    cvtc_y = cv.total_confirmed
    pd.to_numeric(cvtc_y)
    cvtr_y = cv.total_recovered
    pd.to_numeric(cvtr_y)
    cvtd_y = cv.total_deaths
    pd.to_numeric(cvtd_y)
    cv_X = cv[['last_updated']]
    print(cvtc_y)
    print(cvtr_y)
    print(cvtd_y)
    print(cv_X)


    reg = linear_model.LinearRegression()
    fit_cvtr_y = reg.fit(cv_X, cvtr_y) ###<---- fix this (ValueError: could not convert string to float: '2020-04-01')
    fit_cvtd_y = reg.fit(cv_X, cvtd_y)
    fit_cvtc_y = reg.fit(cv_X, cvtc_y)

    predicted_amount = np.around(reg.predict([[fourteenDaysfromToday]]), decimals=2)
    print("Predicted cases for {0} and todta cases: {1}".format(j, predicted_amount))

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

    ax = cv.plot(kind='bar', x='last_updated', y=['total_confirmed', 'total_deaths', 'total_recovered'] , rot=12, figsize=(16,6), grid=True, title="Trend of {}".format(countryName[k]), ax=ax)
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


##LINEAR REGRESSION MODEL:
##1. Create a Linear Regression model using linear_model class of sklearn lib

df_X:int = df[['Year']]
df_y = df.Amount_MkWh
print(df_X)
print(df_y)

reg = linear_model.LinearRegression()
reg.fit(df_X, df_y)

plt.xlabel('Year')
plt.ylabel('Trillion kWH')
plt.scatter(df_X, df_y, color='red', marker='+')
plt.plot(df_X, reg.predict(df[['Amount_MkWh']]), color='blue')
plt.show()


##PREDICTION WITH LINEAR REGRESSION MODEL:

predicted_amount = np.around(reg.predict([[2020]]), decimals=2)
print("The projected generated amount of year 2020 is: {} MkWh".format(predicted_amount))
'''