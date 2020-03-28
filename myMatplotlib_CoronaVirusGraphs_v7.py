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
    plt.xticks(rotation=15)
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
cv['Country'] = cv['Country'].str.strip() #<-Here we have to strip off all leading and trailing white spaces from Conuntry names
cv = cv[cv.Country != "Diamond Princess"] #<-Here we drop a row where the 'Country' column contains a value 'Diamond Princess'

cv = cv.iloc[:-1] #<-- Here we drop the last row of the dataframe (last row holds the total of all rows)
cv = cv.fillna(0) #<-- Fill all NaN values with 0
cv["Gross Total cases"] = cv["Total cases"] + cv["New cases"] #<-Summing up 'Total cases' + 'New cases'
cv["Gross Total deaths"] = cv["Total deaths"] + cv["New deaths"] #<-Summing up 'Total deaths' + 'New deaths'

# cv.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus_experimental.csv", index = False)


#Plot the pie chart for World Data ('Gross Total cases', 'Total recovered', 'Gross Total deaths', 'Active cases')
s = cv.sum(axis=0) #<--Add all columns and create a series
grossTotalCase = int(s['Gross Total cases'])
totalRecovered = s['Total recovered']
totalActiveCases = s['Active cases']
grossTotalDeaths = int(s['Gross Total deaths'])

# Pie chart plotting
labels = 'Total Recovered', 'Active Cases', 'Gross Total Deaths'
sizes = [totalRecovered, totalActiveCases, grossTotalDeaths]
colours = ['green', 'yellow', 'gray']
explode = (0.04, 0.04, 0.1)  # only "explode" the 3rd slice (i.e. 'Gross Total Deaths')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colours, autopct='%1.f%%',
        shadow=True, startangle=60)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set(aspect="equal", title='Total Global Cases as of {} = {}'.format(todayDate, grossTotalCase))
plt.show()

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv_TotalCases = cv.sort_values('Gross Total cases', ascending=False)
cv_TotalRecovered = cv.sort_values('Total recovered', ascending=False)
cv_TotalCasesPerMillion = cv.sort_values('Total cases per 1M pop.', ascending=False)
cv_TotalDeathsPerMillion = cv.sort_values('Total deaths per 1M pop.', ascending=False)
cv_TotalDeaths = cv.sort_values('Gross Total deaths', ascending=False)
cv_NewCases = cv.sort_values('New cases', ascending=False)
cv_NewDeaths = cv.sort_values('New deaths', ascending=False)

#Graph of top 'Gross Total cases'
x = cv_TotalCases.head(topCountryNum)
rowcategory = "Country"
columncategory = "Gross Total cases"
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

#Graph of top 'Total deaths per 1M pop.'
x = cv_TotalDeathsPerMillion.head(topCountryNum)
rowcategory = "Country"
columncategory = "Total deaths per 1M pop."
figureNum = 4
graphColor = "gray"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Gross Total deaths'
x = cv_TotalDeaths.head(topCountryNum)
rowcategory = "Country"
columncategory = "Gross Total deaths"
figureNum = 5
graphColor = "black"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)


#----SAARC DATA----#
cv1 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus.csv")
cv1['Country'] = cv1['Country'].str.strip() #<-Here we have to strip off all leading and trailing white spaces from Conuntry names
cv1 = cv1.fillna(0)
cv1 = cv1.loc[(cv1["Country"] == 'Bangladesh')|
              (cv1["Country"] == 'Bhutan')|
              (cv1["Country"] == 'India')|
              (cv1["Country"] == 'Maldives')|
              (cv1["Country"] == 'Nepal')|
              (cv1["Country"] == 'Pakistan')|
              (cv1["Country"] == 'Sri Lanka')]

cv1["Gross Total cases"] = cv1["Total cases"] + cv1["New cases"] #<-Summing up 'Total cases' + 'New cases'
cv1["Gross Total deaths"] = cv1["Total deaths"] + cv1["New deaths"] #<-Summing up 'Total deaths' + 'New deaths'

#Plot the pie chart for SAARC countries ('Total cases')
#Extract country specific sub-df
cv1_Bangladesh = cv1.loc[(cv1["Country"] == 'Bangladesh')]
cv1_Bhutan = cv1.loc[(cv1["Country"] == 'Bhutan')]
cv1_India = cv1.loc[(cv1["Country"] == 'India')]
cv1_Maldives = cv1.loc[(cv1["Country"] == 'Maldives')]
cv1_Nepal = cv1.loc[(cv1["Country"] == 'Nepal')]
cv1_Pakistan = cv1.loc[(cv1["Country"] == 'Pakistan')]
cv1_SriLanka = cv1.loc[(cv1["Country"] == 'Sri Lanka')]

#Now extract country specific 'Total cases'
tc_Bangladesh = int(cv1_Bangladesh['Gross Total cases'])
tc_Bhutan = int(cv1_Bhutan['Gross Total cases'])
tc_India = int(cv1_India['Gross Total cases'])
tc_Maldives = int(cv1_Maldives['Gross Total cases'])
tc_Nepal = int(cv1_Nepal['Gross Total cases'])
tc_Pakistan = int(cv1_Pakistan['Gross Total cases'])
tc_SriLanka = int(cv1_SriLanka['Gross Total cases'])

# totalSAARCCases = int(tc_Bangladesh)+int(tc_Bhutan)+int(tc_India)+int(tc_Maldives)+int(tc_Nepal)+int(tc_Pakistan)+int(tc_SriLanka)
totalSAARCCases = tc_Bangladesh+tc_Bhutan+tc_India+tc_Maldives+tc_Nepal+tc_Pakistan+tc_SriLanka
# print(totalSAARCCases)

# Pie chart plotting
labels = 'Bangladesh', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Bhutan', 'Sri Lanka'
sizes = [tc_Bangladesh,  tc_India, tc_Maldives, tc_Nepal, tc_Pakistan, tc_Bhutan, tc_SriLanka]
explode = (0.2, 0.05, 0.1, 0.5, 0.05, 0.2, 0.2)

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.f%%', shadow=False, startangle=45)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set(aspect="equal", title='Total SAARC Cases as of {} = {}'.format(todayDate, totalSAARCCases))
plt.show()

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv1_TotalCases = cv1.sort_values('Gross Total cases', ascending=False)
cv1_TotalRecovered = cv1.sort_values('Total recovered', ascending=False)
cv1_TotalCasesPerMillion = cv1.sort_values('Total cases per 1M pop.', ascending=False)
cv1_TotalDeaths = cv1.sort_values('Gross Total deaths', ascending=False)
cv1_NewCases = cv1.sort_values('New cases', ascending=False)
cv1_NewDeaths = cv1.sort_values('New deaths', ascending=False)

#Graph of SAARC 'Total cases'
x = cv1_TotalCases.head(7)
rowcategory = "Country"
columncategory = "Gross Total cases"
figureNum = 6
graphColor = "Red"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top SAARC 'Total recovered'
x = cv1_TotalRecovered.head(7)
rowcategory = "Country"
columncategory = "Total recovered"
figureNum = 7
graphColor = "lime"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top SAARC 'Total deaths'
x = cv1_TotalDeaths.head(7)
rowcategory = "Country"
columncategory = "Gross Total deaths"
figureNum = 8
graphColor = "black"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)