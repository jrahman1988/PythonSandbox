'''
Webscraping to GET the html response, then PARSE and fetch the content, FIND the tables, CONSTRUCT a DF
We'll use here the pandas.read_html(), which returns a list of data frames. According to the PANDAS doc:
"This function searches for <table> elements and only for <tr> and <th> rows and <td> elements within
each <tr> or <th> element in the table. <td> stands for “table data”.
Document URL: https://en.wikipedia.org/wiki/Deployment_of_COVID-19_vaccines#covid-19-pandemic-vaccination
'''
import datetime
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

#List of the countries data to be processed
countryList:list = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan", "Sri Lanka", "Maldives", "Japan"]
# countryList:list = ["USA", "Canada", "UK", "France", "Germany", "Italy", "Japan"]

#Format the date time to present on the graph
dt = datetime.datetime.now()
today = dt.strftime("%A, %d %B %Y, %H:%M:%S")
todayDate = dt.strftime("%A, %d %B %Y")

'''
==============================================================================================================
Function implemenattion: plothHorizontalBarChart()
What it does:
1. Takes parameters of barTitle, barXLabel, barYLabel, barXRotation, listOfXData, listOfYData, barColour
2. Plot side by side horizontal bar chart
==============================================================================================================
'''
def plotHorizontalBarChart(countryList, vaccinatonList, remainingPoulationList, TotalCaseList, TotalRecoveredList, TotalDeathList):

    plt.barh(countryList, vaccinatonList, color="#f3e151")
    # careful: notice "bottom" parameter became "left"
    plt.barh(countryList, remainingPoulationList, left=vaccinatonList, color="#6c3376")

    # we also need to switch the labels
    plt.xlabel('Population')
    plt.ylabel('Countries')

    plt.show()
'''
==============================================================================================================
Function implemenattion: plotPieChart()
What it does:
1. Takes parameters of barTitle, barXLabel, barYLabel, barXRotation, listOfXData, listOfYData, barColour
2. Plot side by side pie chart
==============================================================================================================
'''
def plotPieChart(countryName, TotalPopulation, TotalActiveCases, TotalRecovered, TotalDeaths, TotalVaccinated, populationToBeVaccinated):

    # Pie chart plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    explode1 = (0.04, 0.08, 0.4)
    sizes1 = [TotalRecovered, TotalActiveCases, TotalDeaths]
    labels1 = 'Total \nRecovered', 'Active \nCases', 'Total \nDeaths'
    colours1 = ['greenyellow', 'orange', 'silver']

    explode2 = (0.04, 0.1)
    # TotalRemaining = (TotalPopulation - TotalVaccinated)
    sizes2 = [populationToBeVaccinated, TotalVaccinated]
    labels2 = 'Population \nRemaining', 'Population \nVaccinated'
    colours2 = ['pink', 'greenyellow']

    # Creating autopct arguments to be called form lambda function
    def func(pct, allvalues):
        absolute = int(pct / 100. * np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)

    ax1.pie(sizes1, explode=explode1, labels=labels1, colors=colours1, autopct= lambda pct: func(pct, sizes1), shadow=True, startangle=60)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set(aspect="equal", title='{}: CoViD 19 stats \nDate: {}'.format(countryName, todayDate, TotalActiveCases))

    ax2.pie(sizes2, explode=explode2, labels=labels2, colors=colours2, autopct= lambda pct: func(pct, sizes2), shadow=True, startangle=60)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set(aspect="equal", title='{}: Vaccination stats \nDate: {}'.format(countryName, todayDate, TotalVaccinated))

    saveDir = "/home/jamil/Desktop/Learning/Sandbox/PythonSandbox/vaccinationProgress/"
    plt.savefig('{}{}.png'.format(saveDir, countryName))

    print("{} Remaining to be vaccinated {}".format(countryName, populationToBeVaccinated))
    print("{} Total vaccinated {}\n".format(countryName, TotalVaccinated))
    plt.show()
'''
==============================================================================================================
'''

'''
==============================================================================================================
Function implemenattion: plotBarChart()
What it does:
1. Takes parameters of barTitle, barXLabel, barYLabel, barXRotation, listOfXData, listOfYtotalCaseData,
                       listOfYtotalDeathData, listOfYvaccinatedData
2. Plot the bar chart
==============================================================================================================
'''
def plotBarChart(barTitle, barXLabel, barYLabel, barXRotation, listOfXData, listOfYtotalCaseData, listOfYtotalDeathData, listOfYvaccinatedData):
    # Configuration of the plot parameters
    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=barXRotation)
    plt.grid(True)

    # This is the location for the annotated text
    i = 1.0
    j = 1
    for i in range(len(listOfXData)):
        plt.annotate(round(listOfYvaccinatedData[i]/j), (-0.25 + i, listOfYvaccinatedData[i] + j))

    x = np.arange(len(listOfXData))
    y1 = listOfYtotalDeathData
    y2 = listOfYtotalCaseData
    y3 = listOfYvaccinatedData
    width = 0.2

    # plot data in grouped manner of bar type
    plt.bar(x - 0.2, y1, width, color='cyan')
    plt.bar(x, y2, width, color='orange')
    plt.bar(x + 0.2, y3, width, color='green')
    plt.xticks(x, listOfXData)
    plt.title(barTitle)
    plt.xlabel(barXLabel)
    plt.ylabel(barYLabel)
    plt.legend(["Population", "Total Cases", "Vaccinated"])

    # Plotting
    plt.show()
'''
==============================================================================================================
'''

# GET country by country population table and convert it to a Pandas DF
#<<--response from the web page using requests library, response = a list of tables-->>
populationResponse = requests.get("https://www.worldometers.info/world-population/population-by-country/")
#<<--extract the html tag content from the response-->>
populationPage = BeautifulSoup(populationResponse.content, 'html.parser')
#<<--find the first table which has the table id="example2"-->>
populationTable = populationPage.find_all('table', id="example2")[0]
#<<--create a pandas DF from the table-->>
populationDF = pd.read_html(str(populationTable), displayed_only=False)[0]
#<--rename the column 'Country (or dependency)' to 'Country'
populationDF = populationDF.rename(columns={'Country (or dependency)':'Country'})
#<--rename the column 'Population (2020)' to 'Population'
populationDF = populationDF.rename(columns={'Population (2020)':'Population'})
#<--change the names of 'United States', 'United Arab Emirates' and 'United Kingdom' to 'USA', 'UAE' and 'UK' under Country column
populationDF.loc[populationDF.Country == 'United States', 'Country'] = 'USA'
populationDF.loc[populationDF.Country == 'United Arab Emirates', 'Country'] = 'UAE'
populationDF.loc[populationDF.Country == 'United Kingdom', 'Country'] = 'UK'

# print and check the content of the DF populationDF
# print(type(populationDF))
# print(populationDF.info())
# print(populationDF.head(10))
# print(populationDF.tail(10))

# save the populationDF in a CSV file
populationDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/populationData.csv", index=False)


# GET the country by country corona virus cases table and convert it to a Pandas DF
#<<--response from the web page using requests library, response = a list of tables-->>
coronaResponse = requests.get("https://www.worldometers.info/coronavirus/")
#<<--extract the html tag content from the response-->>
coronaPage = BeautifulSoup(coronaResponse.content, 'html.parser')
#<<--find the first table which has the table id = "main_table_countries_today"-->>
coronaTable = coronaPage.find_all('table', id="main_table_countries_today")[0]
#<<--create a pandas DF from the table-->>
coronaDF = pd.read_html(str(coronaTable), displayed_only=False)[0]
#<--rename the column 'Country,Other' to 'Country'
coronaDF = coronaDF.rename(columns={'Country,Other':'Country'})
#<--remove any leading or trailing white spaces from Country names-->
coronaDF['Country'] = coronaDF['Country'].str.strip()
#<<--drop all unnecessary columns-->>
coronaDF = coronaDF.drop(columns=['#', 'NewCases', 'NewDeaths', 'NewRecovered', 'Serious,Critical',\
                                  'Tot Cases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/ 1M pop',\
                                  'Population', 'Continent', '1 Caseevery X ppl',	'1 Deathevery X ppl',\
                                  '1 Testevery X ppl'])
#<--get rid of the rows with value 'Total:' under 'Country' column-->
coronaDF = coronaDF[coronaDF.Country != 'Total:']
#<--drop a row where the 'Country' column contains a value 'Diamond Princess'-->
coronaDF = coronaDF[coronaDF.Country != "Diamond Princess"]
#<--get rid of the rows starting from index 0 to 7 under 'Country' column-->
coronaDF = coronaDF.drop(labels=range(0, 8), axis=0, inplace=False)
#<--fill all NaN values with 0-->
coronaDF = coronaDF.fillna(0)
#<--convert all values to type int-->
coronaDF = coronaDF.astype({'TotalCases': 'int', 'TotalDeaths': 'int', 'TotalRecovered': 'int', 'ActiveCases': 'int'})
#<--reset the index-->
coronaDF = coronaDF.reset_index(drop=True)

# print and check the content of the DF coronaDF
# print(type(coronaDF))
# print(coronaDF.info())
# print(coronaDF.head(10))
# print(coronaDF.tail(10))
# save the coronaDF in a CSV file
coronaDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/globalCoronaCasesData.csv", index=False)


# GET country by country vaccination stats table and convert it to a Pandas DF
#<<--response from the web page using requests library, response = a list of tables-->>
vaccineResponse = requests.get("https://en.wikipedia.org/wiki/Deployment_of_COVID-19_vaccines#covid-19-pandemic-vaccination")
#<<--extract the html tag content from the response-->>
vaccinePage = BeautifulSoup(vaccineResponse.content, 'html.parser')
#<<--find the first table which has the table id = "thetable"-->>
vaccineTable = vaccinePage.find_all('table', id="thetable")[0]
#<<--create a pandas DF from the table-->>
vaccineDF = pd.read_html(str(vaccineTable), displayed_only=False)[0]
#<--remove any '[*]' chars attached to a country's name-->>
vaccineDF.Location = vaccineDF.Location.str.replace(r"\[.*\]$", "", regex=True)
#<--get rid of the row with value 'World' under 'Location' column-->
vaccineDF = vaccineDF[vaccineDF.Location != "World"]
#<--get rid of the row with value 'EU' under 'Location' column-->
vaccineDF = vaccineDF[vaccineDF.Location != "EU"]
#<--get rid of the column named '% of pop.[c][d]'-->
vaccineDF = vaccineDF.drop(columns=['% of pop.[c][d]'])
#<--rename the columns 'Country,Other' to 'Country' and 'Vaccinated[b]' to 'Vaccinated'
vaccineDF = vaccineDF.rename(columns={'Location':'Country', 'Vaccinated[b]':'Vaccinated'})
#<--get rid of the column named Unnamed: 3-->
vaccineDF = vaccineDF.drop(columns=['Unnamed: 3'])
#<--drop the empty rows under 'Country' and 'Vaccinated' columns-->
vaccineDF = vaccineDF.dropna(subset=['Country', 'Vaccinated'])
#<--drop the row containing 'Sources' under 'Country' column-->
vaccineDF = vaccineDF[~vaccineDF.Country.str.contains('Sources')]
#<--change the names of 'United States', 'United Arab Emirates' and 'United Kingdom' to 'USA', 'UAE' and 'UK' under Country column
vaccineDF.loc[vaccineDF.Country == 'United States', 'Country'] = 'USA'
vaccineDF.loc[vaccineDF.Country == 'United Arab Emirates', 'Country'] = 'UAE'
vaccineDF.loc[vaccineDF.Country == 'United Kingdom', 'Country'] = 'UK'
#<--convert all values to type int-->
vaccineDF = vaccineDF.astype({'Vaccinated': 'int'})
#<--reset the index-->
vaccineDF = vaccineDF.reset_index(drop=True)

# print and check the content of the DF vaccineDF
# print(type(vaccineDF))
# print(vaccineDF.info())
# print(vaccineDF.head(10))
# print(vaccineDF.tail(10))
# save the vaccineDF in a CSV file
vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/vaccineProgressData.csv", index=False)

'''
==============================================================================================================
Extract corresponding 'Population', 'Vaccinated', 'TotalCases', 'TotalDeaths' data of countries in the list of
'countryList' and put them in lists 
Syntax:
1. Declare the list variables, 'populationList', 'vaccinatonList', 'TotalCaseList', 'TotalRecoveredList', 'TotalDeathList'
2. Fill in each list with the corresponding values of each country from the related DFs
==============================================================================================================
'''
populationList:list = []
vaccinatonList:list = []
TotalCaseList:list = []
TotalRecoveredList:list = []
TotalDeathList:list = []
TotalActiveCaseList:list = []
remainingPoulationList:list = []

j=0
for i in countryList:
    populationList.append(populationDF.loc[populationDF.Country == i, 'Population'].tolist()[0])
    vaccinatonList.append(vaccineDF.loc[vaccineDF.Country == i, 'Vaccinated'].tolist()[0])
    TotalCaseList.append(coronaDF.loc[coronaDF.Country == i, 'TotalCases'].tolist()[0])
    TotalRecoveredList.append(coronaDF.loc[coronaDF.Country == i, 'TotalRecovered'].tolist()[0])
    TotalDeathList.append(coronaDF.loc[coronaDF.Country == i, 'TotalDeaths'].tolist()[0])
    TotalActiveCaseList.append(coronaDF.loc[coronaDF.Country == i, 'ActiveCases'].tolist()[0])
    remainingPoulationList.append(populationList[j] - vaccinatonList[j])
    j=j+1

#<--add new columns 'Population', 'Vaccinated', 'TotalCases', 'TotalDeaths' in the 'countryDF' and fill in with the data of list above lists
# countryDF['Population'] = populationList
# countryDF['Vaccinated'] = vaccinatonList
# countryDF['TotalCases'] = TotalCaseList
# countryDF['TotalRecovered'] = TotalRecoveredList
# countryDF['TotalDeaths'] = TotalDeathList
# print('\n New DF countryDF: \n' , countryDF)
'''
==============================================================================================================
Prepare the parmaters and pass them to plotBarChart() method
==============================================================================================================
'''
barTitle="Country wise total vaccination done as of today"
barXLabel="Countries"
barYLabel="Population in Million (x 1000000)"
barXRotation=0
listOfXData=countryList
listOfYpopulationData=populationList
listOfYtotalCaseData=TotalCaseList
listOfYvaccinatedData=vaccinatonList
listOfYtotalDeathData=TotalDeathList
# plotBarChart(barTitle, barXLabel, barYLabel, barXRotation, listOfXData, listOfYtotalCaseData, listOfYtotalDeathData, listOfYvaccinatedData)

'''
==============================================================================================================
Prepare the parmaters and pass them to plotPieChart() method
==============================================================================================================
'''
k=0
for i in countryList:
 populationToBeVaccinated = (int)(populationList[k]) - (int)(vaccinatonList[k])
 print("{} population = {}".format(i, populationList[k]))
 print("{} Total cases = {}".format(i, TotalCaseList[k]))
 print("{} Total recovered = {}".format(i, TotalRecoveredList[k]))
 print("{} Total deaths = {}".format(i, TotalDeathList[k]))
 print("{} Active cases = {}".format(i, TotalActiveCaseList[k]))
 print("{} Total vaccinated = {}".format(i, vaccinatonList[k]))
 print('populationList = {}'.format(populationList))
 print('Remaining population List  = {}'.format(remainingPoulationList))
 print("{} Remaining population to be vaccinated = {}\n".format(i, populationToBeVaccinated))

 plotPieChart(i, populationList[k], TotalActiveCaseList[k], TotalRecoveredList[k], TotalDeathList[k], vaccinatonList[k], populationToBeVaccinated)
 k=k+1

plotHorizontalBarChart(countryList, vaccinatonList, remainingPoulationList, TotalCaseList, TotalRecoveredList, TotalDeathList)