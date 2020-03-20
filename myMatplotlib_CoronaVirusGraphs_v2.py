'''
Using Matplotlib module of Python, draw a different graphs, data read from (corona_virus.csv)
Note that, here we do the followings to fine tune the dataframe:
1. Read the data file corona_virus.csv from file system and create a dataframe
2. Delete the last row so that 'Total' is not considered in any calculations using: cv = cv.iloc[:-1]
3. Drop the 'Diamond Princess' row as a country usincv = cv[cv.Country != 'Diamond Princess']g:
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime

#This is for how many data will be read
dataSize = 9

desired_width=360
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',120)

dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")

#----WORLD DATA----#
#Read the coronoa_virus.csv from the file system and transform into a DataFrame using read_csv() method
cv = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus.csv")
cv = cv.iloc[:-1] #<-- Here we drop the last row of the dataframe (last row holds the total of all rows)
cv = cv[cv.Country != 'Diamond Princess'] #<-Here we drop a row where the 'Country' column contains a value 'Diamond Princess'
cv = cv.fillna(0) #<-- Fill all NaN values with 0

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv_TotalCases = cv.sort_values('Total cases', ascending=False)
cv_TotalRecovered = cv.sort_values('Total recovered', ascending=False)
cv_TotalCasesPerMillion = cv.sort_values('Total cases per 1M pop.', ascending=False)
cv_TotalDeaths = cv.sort_values('Total deaths', ascending=False)
cv_NewCases = cv.sort_values('New cases', ascending=False)
cv_NewDeaths = cv.sort_values('New deaths', ascending=False)

#Graph of top 10 'Total cases'
x = cv_TotalCases.head(10)
x1 = x["Country"]
y1 = x["Total cases"]
plt.figure(1,figsize=(12,5))
plt.title('Top 10 countries based on Total cases - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases")
barplot = plt.bar(x1,y1, color="Red")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top 10 'Total recovered'
x = cv_TotalRecovered.head(10)
x1 = x["Country"]
y1 = x["Total recovered"]
plt.figure(2,figsize=(12,5))
plt.title('Top 10 countries based on Total recovered - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total recovered")
barplot = plt.bar(x1,y1, color="limegreen")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top 10 'Total cases per 1M pop.'
x = cv_TotalCasesPerMillion.head(10)
x1 = x["Country"]
y1 = (x["Total cases per 1M pop."])
plt.figure(3,figsize=(12,5))
plt.title('Top 10 countries based on Total cases per million pop. - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases per million pop.")
barplot = plt.bar(x1,y1, color="cornflowerblue")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top 10 'Total deaths'
x = cv_TotalDeaths.head(10)
x1 = x["Country"]
y1 = (x["Total deaths"])
plt.figure(4,figsize=(12,5))
plt.title('Top 10 countries based on Total deaths - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total deaths")
barplot = plt.bar(x1,y1, color="dimgray")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top 10 'New cases'
x = cv_NewCases.head(10)
x1 = x["Country"]
y1 = (x["New cases"])
plt.figure(5,figsize=(12,5))
plt.title('Top 10 countries based on New cases - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New cases")
barplot = plt.bar(x1,y1, color="lightcoral")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top 10 'New deaths'
x = cv_NewDeaths.head(10)
x1 = x["Country"]
y1 = (x["New deaths"])
plt.figure(6,figsize=(12,5))
plt.title('Top 10 countries based on New deaths - [Total countries effected as of today = {}]'.format(cv.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New deaths")
barplot = plt.bar(x1,y1, color="dimgrey")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

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
print("SAARC countries \n ", cv1)

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv1_TotalCases = cv1.sort_values('Total cases', ascending=False)
cv1_TotalRecovered = cv1.sort_values('Total recovered', ascending=False)
cv1_TotalCasesPerMillion = cv1.sort_values('Total cases per 1M pop.', ascending=False)
cv1_TotalDeaths = cv1.sort_values('Total deaths', ascending=False)
cv1_NewCases = cv1.sort_values('New cases', ascending=False)
cv1_NewDeaths = cv1.sort_values('New deaths', ascending=False)

#Graph of top SAARC 'Total cases'
x = cv1_TotalCases.head(7)
x1 = x["Country"]
y1 = x["Total cases"]
plt.figure(7,figsize=(12,5))
plt.title('SAARC countries compare based on Total cases - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases")
barplot = plt.bar(x1,y1, color="m")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top SAARC 'Total recovered'
x = cv1_TotalRecovered.head(7)
x1 = x["Country"]
y1 = x["Total recovered"]
plt.figure(8,figsize=(12,5))
plt.title('SAARC countries compare based on Total recovered - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total recovered")
barplot = plt.bar(x1,y1, color="lime")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top SAARC 'Total cases per 1M pop.'
x = cv1_TotalCasesPerMillion.head(7)
x1 = x["Country"]
y1 = (x["Total cases per 1M pop."])
plt.figure(9,figsize=(12,5))
plt.title('SAARC countries compare based on Total cases per million pop. - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases per million pop.")
barplot = plt.bar(x1,y1, color="aqua")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top SAARC 'Total deaths'
x = cv1_TotalDeaths.head(7)
x1 = x["Country"]
y1 = (x["Total deaths"])
plt.figure(10,figsize=(12,5))
plt.title('SAARC countries compare based on Total deaths - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total deaths")
barplot = plt.bar(x1,y1, color="black")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top SAARC 'New cases'
x = cv1_NewCases.head(7)
x1 = x["Country"]
y1 = (x["New cases"])
plt.figure(11,figsize=(12,5))
plt.title('SAARC countries compare based on New cases - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New cases")
barplot = plt.bar(x1,y1, color="orangered")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()

#Graph of top SAARC 'New deaths'
x = cv1_NewDeaths.head(7)
x1 = x["Country"]
y1 = (x["New deaths"])
plt.figure(12,figsize=(12,5))
plt.title('SAARC countries compare based on New deaths - [Total countries effected as of today = {}]'.format(cv1.shape[0]))
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New deaths")
barplot = plt.bar(x1,y1, color="gray")
plt.grid(True)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
plt.show()