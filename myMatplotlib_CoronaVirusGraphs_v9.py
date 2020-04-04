'''
Using Matplotlib module of Python, draw different graphs, capture data thru web scraping technique:
GET (using requests lib) -> PARSE (using BeautifulSoup lib) -> CONSTRUCT DF (using PANDAS lib)
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime
import requests
import http.client
import mimetypes
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#Read data from a GET R

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
fileNameDate = dt.strftime("%b%d%Y")

##---Web data scrapimg and then constructing a DF then save it to today.csv file--##
req = requests.get("https://www.worldometers.info/coronavirus/")
df = pd.read_html(req.content)[0]
df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/today.csv", index=False)
##----------------End of web scrapping and contruction of DF-----------------------##

#METHOD to plot the bar graphs
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

##--START: Data read, write and preparation---------------------------##
#Read from a local CSV file, which was created earlier thru web scraping
cv = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/today.csv")
# print(cv.info())

#Rename the columns for better readability
cv = cv.rename(columns={'Country,Other':'Country',                  #type: object
                        'TotalCases': 'Total cases',                #type: int64
                        'TotalDeaths': 'Total deaths',              #type: object
                        'TotalRecovered': 'Total recovered',        #type: float64
                        'NewCases': 'New cases',                    #type: float64
                        'NewDeaths': 'New deaths',                  #type: float64
                        'ActiveCases': 'Active cases',              #type: int64
                        'Serious,Critical': 'Critical cases',       #type: float64
                        'Tot Cases/1M pop': 'Cases per 1M pop.',    #type: float64
                        'Deaths/1M pop': 'Deaths per 1M pop.',      #type: float64
                        'TotalTests': 'Total tests done',           #type: float64
                        'Tests/ 1M pop': 'Tests per 1M pop.'})      #type: float64

#Remove any leading or trailing white spaces from Country names
cv['Country'] = cv['Country'].str.strip()

#Drop a row where the 'Country' column contains a row of 'World'
cv = cv[cv.Country != "World"]

#Drop a row where the 'Country' column contains a value 'Diamond Princess'
cv = cv[cv.Country != "Diamond Princess"]

#Drop a row where the 'Country' column contains a value 'Total:'
cv = cv[cv.Country != "Total:"]

#Fill all NaN values with 0
cv = cv.fillna(0)

#Convert all columns type to int
cv['Total deaths'] = cv['Total deaths'].astype(int)
cv['Total recovered'] = cv['Total recovered'].astype(int)
cv['New cases'] = cv['New cases'].astype(int)
cv['New deaths'] = cv['New deaths'].astype(int)
cv['Critical cases'] = cv['Critical cases'].astype(int)
cv['Cases per 1M pop.'] = cv['Cases per 1M pop.'].astype(int)
cv['Deaths per 1M pop.'] = cv['Deaths per 1M pop.'].astype(int)
cv['Total tests done'] = cv['Total tests done'].astype(int)
cv['Tests per 1M pop.'] = cv['Tests per 1M pop.'].astype(int)

#Summing up 'Total cases' + 'New cases' and create a new column named: 'Gross Total cases'
cv["Gross Total cases"] = cv["Total cases"] + cv["New cases"]

#Summing up 'Total deaths' + 'New deaths' and create a new column named: 'Gross Total deaths'
cv["Gross Total deaths"] = cv["Total deaths"] + cv["New deaths"]

#Save a data record for today in a .csv file
cv.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus-{}.csv".format(fileNameDate), index=False)

# print(cv.head())
# ##--ENDS: Data read, write and preparation---------------------------##


##--WORLD data plotting--------------------##
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
cv_CasesPerMillion = cv.sort_values('Cases per 1M pop.', ascending=False)
cv_TotalDeaths = cv.sort_values('Gross Total deaths', ascending=False)
cv_NewCases = cv.sort_values('New cases', ascending=False)
cv_NewDeaths = cv.sort_values('New deaths', ascending=False)
cv_DeathsPerMillion = cv.sort_values('Deaths per 1M pop.', ascending=False)
cv_TestsPerMilion = cv.sort_values('Tests per 1M pop.', ascending=False)

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

#Graph of top 'Cases per 1M pop.'
x = cv_CasesPerMillion.head(topCountryNum)
rowcategory = "Country"
columncategory = "Cases per 1M pop."
figureNum = 3
graphColor = "cornflowerblue"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Gross Total deaths'
x = cv_TotalDeaths.head(topCountryNum)
rowcategory = "Country"
columncategory = "Gross Total deaths"
figureNum = 4
graphColor = "black"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Deaths per million population'
x = cv_DeathsPerMillion.head(topCountryNum)
rowcategory = "Country"
columncategory = "Deaths per 1M pop."
figureNum = 5
graphColor = "dimgrey"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top 'Tests per 1M pop.'
x = cv_TestsPerMilion.head(topCountryNum)
rowcategory = "Country"
columncategory = "Tests per 1M pop."
figureNum = 6
graphColor = "lightseagreen"
titlestring = "Top {} countries based on: ".format(topCountryNum)
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)


##--SAARC data plotting--------------------##
cv1 = cv.loc[(cv["Country"] == 'Bangladesh')|
              (cv["Country"] == 'Bhutan')|
              (cv["Country"] == 'India')|
              (cv["Country"] == 'Maldives')|
              (cv["Country"] == 'Nepal')|
              (cv["Country"] == 'Pakistan')|
              (cv["Country"] == 'Sri Lanka')]

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
cv1_CasesPerMillion = cv1.sort_values('Cases per 1M pop.', ascending=False)
cv1_TotalDeaths = cv1.sort_values('Gross Total deaths', ascending=False)
cv1_NewCases = cv1.sort_values('New cases', ascending=False)
cv1_NewDeaths = cv1.sort_values('New deaths', ascending=False)
cv1_DeathsPerMillion = cv1.sort_values('Deaths per 1M pop.', ascending=False)
cv1_TestsPerMilion = cv1.sort_values('Tests per 1M pop.', ascending=False)

#Graph of SAARC 'Total cases'
x = cv1_TotalCases.head(7)
rowcategory = "Country"
columncategory = "Gross Total cases"
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

#Graph of top SAARC 'Total deaths'
x = cv1_TotalDeaths.head(7)
rowcategory = "Country"
columncategory = "Gross Total deaths"
figureNum = 9
graphColor = "black"
titlestring = "SAARC countries compare based on: "
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

# #Graph of top SAARC 'Deaths per million population'
# x = cv1_DeathsPerMillion.head(7)
# rowcategory = "Country"
# columncategory = "Deaths per 1M pop."
# figureNum = 10
# graphColor = "dimgrey"
# titlestring = "SAARC countries compare based on: "
# plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)

#Graph of top SAARC 'Tests per 1M pop.'
x = cv1_TestsPerMilion.head(7)
rowcategory = "Country"
columncategory = "Tests per 1M pop."
figureNum = 11
graphColor = "lightseagreen"
titlestring = "SAARC countries compare based on:"
plotGraph(x, rowcategory, columncategory, figureNum, graphColor, titlestring)