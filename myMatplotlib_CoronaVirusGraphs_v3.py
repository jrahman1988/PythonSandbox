'''
Using Matplotlib module of Python, draw different graphs, using data read (corona_virus.csv)
Note that, here we do the followings to fine tune the dataframe:
1. Read the raw data file corona_virus.csv from file system and create a dataframe
2. Drop the last row so that 'Total' is not considered in any calculations using: cv = cv.iloc[:-1]
3. Drop the 'Diamond Princess' row as a country using cv = cv[cv.Country != 'Diamond Princess']
4. Draw the bar plot
5. Draw the pie plot
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime

#Number of top countries to be reported
topCountryNum:int = 20

#Graph size matters
desired_width=360
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',120)

#Format the date time to present on the graph
dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")

#Local method to plot the bar graph
def plotGraph(dfname, rowname, colname, fignum, graphcolor, titlestr):
    x1 = dfname[rowname]
    y1 = dfname[colname]
    plt.figure(fignum, figsize=(16, 6))
    plt.title(titlestr + r"$\bf{" + colname + "}$" + ' - [Total countries effected as of today = {}]'.format(cv.shape[0]))
    plt.suptitle(today)
    plt.xlabel("Countries")
    plt.ylabel(colname)
    plt.xticks(rotation=18)
    barplot = plt.bar(x1, y1, color=graphcolor)
    plt.grid(True)
    for bar in barplot:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, int(yval), va='bottom')  # va: vertical alignment y positional argument
    plt.show()
    return()

#----WORLD DATA----#
#Read the coronoa_virus.csv from the file system and transform into a DataFrame using read_csv() method
cv = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus.csv")
cv = cv.iloc[:-1] #<-- Here we drop the last row of the dataframe (last row holds the total of all rows)
cv = cv[cv.Country != 'Diamond Princess'] #<-Here we drop a row where the 'Country' column contains a value 'Diamond Princess'
cv = cv.fillna(0) #<-- Fill all NaN values with 0

#Plot the pie chart for World Data ('Total cases', 'Total recovered', 'Total deaths', 'Active cases')
s = cv.sum(axis=0) #<--Add all columns and create a series
totalCase = s['Total cases']
totalRecovered = s['Total recovered']
totalActiveCases = s['Active cases']
totalDeaths = s['Total deaths']

# Pie chart plotting
labels = 'Total Recovered', 'Active Cases', 'Total Deaths'
sizes = [totalRecovered, totalActiveCases, totalDeaths]
explode = (0.0, 0.0, 0.3)  # only "explode" the 3rd slice (i.e. 'Total Deaths')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%',
        shadow=True, startangle=50)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set(aspect="equal", title='Total Global Cases as of {} = {}'.format(todayDate, totalCase))
plt.show()

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv_TotalCases = cv.sort_values('Total cases', ascending=False)
cv_TotalRecovered = cv.sort_values('Total recovered', ascending=False)
cv_TotalCasesPerMillion = cv.sort_values('Total cases per 1M pop.', ascending=False)
cv_TotalDeaths = cv.sort_values('Total deaths', ascending=False)
cv_NewCases = cv.sort_values('New cases', ascending=False)
cv_NewDeaths = cv.sort_values('New deaths', ascending=False)

#Graph of top 'Total cases'
x = cv_TotalCases.head(topCountryNum)
rowcategory = "Country"
columncategory = "Total cases"
figureNum = 1
graphColor = "Red"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Total recovered'
x = cv_TotalRecovered.head(topCountryNum)
rowcategory = "Country"
columncategory = "Total recovered"
figureNum = 2
graphColor = "limegreen"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Total cases per 1M pop.'
x = cv_TotalCasesPerMillion.head(topCountryNum)
rowcategory = "Country"
columncategory = "Total cases per 1M pop."
figureNum = 3
graphColor = "cornflowerblue"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Total deaths'
x = cv_TotalDeaths.head(topCountryNum)
rowcategory = "Country"
columncategory = "Total deaths"
figureNum = 4
graphColor = "dimgray"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)
#
# #Graph of top 'New cases'
# x = cv_NewCases.head(topCountryNum)
# rowcategory = "Country"
# columncategory = "New cases"
# figureNum = 5
# graphColor = "lightcoral"
# titlestring = "Top {} countries based on: ".format(topCountryNum)
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)
#
# #Graph of top 'New deaths'
# x = cv_NewDeaths.head(topCountryNum)
# rowcategory = "Country"
# columncategory = "New deaths"
# figureNum = 6
# graphColor = "dimgrey"
# titlestring = "Top {} countries based on: ".format(topCountryNum)
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)


#----SAARC DATA----#
cv1 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus.csv")
cv1 = cv1.fillna(0)
cv1 = cv1.loc[(cv1["Country"] == 'Bangladesh')|
              (cv1["Country"] == 'Bhutan')|
              (cv1["Country"] == 'India')|
              (cv1["Country"] == 'Maldives')|
              (cv1["Country"] == 'Nepal')|
              (cv1["Country"] == 'Pakistan')|
              (cv1["Country"] == 'Sri Lanka')]

#Plot the pie chart for SAARC countries ('Total cases')
#Extract country specific sub-df
cv1_Bangladesh = cv1.loc[(cv1["Country"] == 'Bangladesh')]
cv1_Bhutan = cv1.loc[(cv1["Country"] == 'Bhutan')]
cv1_India = cv1.loc[(cv1["Country"] == 'India')]
cv1_Malvives = cv1.loc[(cv1["Country"] == 'Maldives')]
cv1_Nepal = cv1.loc[(cv1["Country"] == 'Nepal')]
cv1_Pakistan = cv1.loc[(cv1["Country"] == 'Pakistan')]
cv1_SriLanka = cv1.loc[(cv1["Country"] == 'Sri Lanka')]

#Now extract country specific 'Total cases'
tc_Bangladesh = cv1_Bangladesh['Total cases']
tc_Bhutan = cv1_Bhutan['Total cases']
tc_India = cv1_India['Total cases']
tc_Maldives = cv1_Malvives['Total cases']
tc_Nepal = cv1_Nepal['Total cases']
tc_Pakistan = cv1_Pakistan['Total cases']
tc_SriLanka = cv1_SriLanka['Total cases']

#Get rid off the stupid df index
tc_Bangladesh=tc_Bangladesh.to_string(index=False)
tc_Bhutan=tc_Bhutan.to_string(index=False)
tc_India=tc_India.to_string(index=False)
tc_Maldives=tc_Maldives.to_string(index=False)
tc_Nepal=tc_Nepal.to_string(index=False)
tc_Pakistan=tc_Pakistan.to_string(index=False)
tc_SriLanka=tc_SriLanka.to_string(index=False)

totalSAARCCases = int(tc_Bangladesh)+int(tc_Bhutan)+int(tc_India)+int(tc_Maldives)+int(tc_Nepal)+int(tc_Pakistan)+int(tc_SriLanka)

# Pie chart plotting
labels = 'Bangladesh', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Bhutan', 'Sri Lanka'
sizes = [tc_Bangladesh,  tc_India, tc_Maldives, tc_Nepal, tc_Pakistan, tc_Bhutan, tc_SriLanka]
explode = (0.2, 0.0, 0.2, 0.1, 0.1, 0.3, 0.0)

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%', shadow=False, startangle=45)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set(aspect="equal", title='Total SAARC Cases as of {} = {}'.format(todayDate, totalSAARCCases))
plt.show()

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv1_TotalCases = cv1.sort_values('Total cases', ascending=False)
cv1_TotalRecovered = cv1.sort_values('Total recovered', ascending=False)
cv1_TotalCasesPerMillion = cv1.sort_values('Total cases per 1M pop.', ascending=False)
cv1_TotalDeaths = cv1.sort_values('Total deaths', ascending=False)
cv1_NewCases = cv1.sort_values('New cases', ascending=False)
cv1_NewDeaths = cv1.sort_values('New deaths', ascending=False)

#Graph of SAARC 'Total cases'
x = cv1_TotalCases.head(7)
rowcategory = "Country"
columncategory = "Total cases"
figureNum = 7
graphColor = "Red"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top SAARC 'Total recovered'
x = cv1_TotalRecovered.head(7)
rowcategory = "Country"
columncategory = "Total recovered"
figureNum = 8
graphColor = "lime"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

# #Graph of top SAARC 'Total cases per 1M pop.'
# x = cv1_TotalCasesPerMillion.head(7)
# rowcategory = "Country"
# columncategory = "Total cases per 1M pop."
# figureNum = 9
# graphColor = "aqua"
# titlestring = "SAARC countries compare based on: "
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top SAARC 'Total deaths'
x = cv1_TotalDeaths.head(7)
rowcategory = "Country"
columncategory = "Total deaths"
figureNum = 10
graphColor = "black"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)
#
# #Graph of top SAARC 'New cases'
# x = cv1_NewCases.head(7)
# rowcategory = "Country"
# columncategory = "New cases"
# figureNum = 11
# graphColor = "orangered"
# titlestring = "SAARC countries reported: "
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)
#
# #Graph of top SAARC 'New deaths'
# x = cv1_NewDeaths.head(7)
# rowcategory = "Country"
# columncategory = "New deaths"
# figureNum = 12
# graphColor = "gray"
# titlestring = "SAARC countries reported: "
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)