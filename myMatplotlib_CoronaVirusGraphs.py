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

dataSize = 9

desired_width=360
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',120)

dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")

#Read the coronoa_virus.csv from the file system and transform into a DataFrame using read_csv() method
cv = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/corona_virus.csv")
cv = cv.iloc[:-1] #<-- Here we drop the last row of the dataframe (last row holds the total of all rows)
cv = cv[cv.Country != 'Diamond Princess'] #<-Here we drop a row where the 'Country' column contains a value 'Diamond Princess'-

#Sorting the data based on a single column in a file and output using sort_values() method (descending order - ascending=False)
cv_TotalCases = cv.sort_values('Total cases', ascending=False)
cv_TotalRecovered = cv.sort_values('Total recovered', ascending=False)
cv_TotalCasesPerMillion = cv.sort_values('Total cases per 1M pop.', ascending=False)
cv_TotalDeaths = cv.sort_values('Total deaths', ascending=False)
cv_NewCases = cv.sort_values('New cases', ascending=False)
cv_NewDeaths = cv.sort_values('New deaths', ascending=False)
print("\nOutput sorted data based on the column named 'Total cases' in descending order: \n", cv_TotalCases.head(10))
print("\nOutput sorted data based on the column named 'Total recovered' in descending order: \n", cv_TotalRecovered.head(10))
print("\nOutput sorted data based on the column named 'Total cases per 1M pop.' in descending order: \n", cv_TotalCasesPerMillion.head(10))
print("\nOutput sorted data based on the column named 'Total deaths' in descending order: \n", cv_TotalDeaths.head(10))
print("\nOutput sorted data based on the column named 'New cases' in descending order: \n", cv_NewCases.head(10))
print("\nOutput sorted data based on the column named 'New deaths' in descending order: \n", cv_NewDeaths.head(10))

#Graph of top 10 'Total cases'
x = cv_TotalCases.head(10)
x1 = x["Country"]
y1 = x["Total cases"]
print(x1)
print(y1)
plt.figure(1,figsize=(12,5))
plt.title("Top 10 countries based on Total cases")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases")
plt.bar(x1,y1, color="Red")
plt.grid(True)
plt.show()

#Graph of top 10 'Total recovered'
x = cv_TotalRecovered.head(10)
x1 = x["Country"]
y1 = x["Total recovered"]
print(x1)
print(y1)
plt.figure(2,figsize=(12,5))
plt.title("Top 10 countries based on Total recovered")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total recovered")
plt.bar(x1,y1, color="limegreen")
plt.grid(True)
plt.show()

#Graph of top 10 'Total cases per 1M pop.'
x = cv_TotalCasesPerMillion.head(10)
x1 = x["Country"]
y1 = (x["Total cases per 1M pop."])
print(x1)
print(y1)
plt.figure(3,figsize=(12,5))
plt.title("Top 10 countries based on Total cases per million pop.")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total cases per million pop.")
plt.bar(x1,y1, color="cornflowerblue")
plt.grid(True)
plt.show()

#Graph of top 10 'Total deaths'
x = cv_TotalDeaths.head(10)
x1 = x["Country"]
y1 = (x["Total deaths"])
print(x1)
print(y1)
plt.figure(4,figsize=(12,5))
plt.title("Top 10 countries based on Total deaths")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("Total deaths")
plt.bar(x1,y1, color="dimgray")
plt.grid(True)
plt.show()

#Graph of top 10 'New cases'
x = cv_NewCases.head(10)
x1 = x["Country"]
y1 = (x["New cases"])
print(x1)
print(y1)
plt.figure(5,figsize=(12,5))
plt.title("Top 10 countries based on New cases")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New cases")
plt.bar(x1,y1, color="lightcoral")
plt.grid(True)
plt.show()

#Graph of top 10 'New deaths'
x = cv_NewDeaths.head(10)
x1 = x["Country"]
y1 = (x["New deaths"])
print(x1)
print(y1)
plt.figure(6,figsize=(12,5))
plt.title("Top 10 countries based on New deaths")
plt.suptitle(today)
plt.xlabel("Countries")
plt.ylabel("New deaths")
plt.bar(x1,y1, color="dimgrey")
plt.grid(True)
plt.show()