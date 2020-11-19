'''
The Pandas I/O API is a set of top level reader functions accessed like pd.read_csv() that generally return a Pandas object.

The two workhorse functions for reading text files (or the flat files) are read_csv() and read_table().
They both use the same parsing code to intelligently convert tabular data into a DataFrame object
'''
import pandas as pd
from matplotlib import pyplot as plt

# Some house keeping rules to keep the data presentaion tidy
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

'''
==============================================================================================================
Read the data and present without any change (JUST to check data integrity after converted to data frame
==============================================================================================================
'''
#Read the Border_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Learning Together/BorderData/Border_Crossing_Entry_Data.csv")
print("\n=========================================")
print("Output the full file in DF format \n", df)
print("=========================================\n")
print("\nOutput the header of the file in DF format \n", df.head())
print("\nOutput the tail of the file in DF format \n", df.tail())
print("\n=========================================")
print("Total rows in raw data = ", len(df.index) , "<--*** performance wise this is faster")
print("Total rows in raw data using shape[0] = ", df.shape[0])
beforeDroppingZeroes = len(df.index)
print("=========================================")

'''
==============================================================================================================
Get rid off all data rows with '0' values under Value column, we access to the column named 'Value' of DF and
reconstruct the DF by reading only the 'non-zero' rows
==============================================================================================================
'''
df1 = df[df.Value != 0]
print("\n===================== after removing all '0' from Value column ================================")
print("Output the full file in DF format", df1)
print("=========================================")
afterDroppingZeroes = len(df1.index)
print("Total rows after dropping all zeroes data = ", afterDroppingZeroes)
print("Total dropped rows which contained '0' under 'Value' column = ", (beforeDroppingZeroes-afterDroppingZeroes))
print("=========================================\n")

'''
==============================================================================================================
Get rid off all data rows with 'US-Mexico Border' values under Border column, we access to the column named 'Border'
of DF and reconstruct the DF by reading only the 'US-Canada Border' rows
==============================================================================================================
'''
df2 = df1[df1.Border != "US-Mexico Border"]
print("\n========================================= Only US-Canada Border data ================================")
print("Output the full file in DF format \n", df2)
print("=========================================")
afterDroppingMexico = len(df2.index)
print("Total rows after dropping all US-Mexico Border data = ", afterDroppingMexico)
print("Total dropped rows which contained 'US-Mexico Border' under 'Value' column = ", (beforeDroppingZeroes-afterDroppingMexico))
print("=========================================\n")

'''
==============================================================================================================
We need to correct some erroneous State data, those don't make any borders with US-Canada
Get rid off all data rows with 'AZ', 'CA' and 'TX' values under State
==============================================================================================================
'''
df3 = df2[(df2.State != "AZ") & (df2.State != "TX") & (df2.State != "CA")]
print("\n========================================= Only US-Canada Border data ================================")
print("Output the full file in DF format \n", df3)
print("=========================================")
afterDroppingAZandCAandTX = len(df3.index)
print("Total rows after dropping 'AZ', 'CA' and 'TX' State data = ", afterDroppingAZandCAandTX)
print("Total dropped rows which contained 'AZ', 'CA' and 'TX' State data = ", (beforeDroppingZeroes-afterDroppingAZandCAandTX))
df3.to_csv("~/Desktop/Learning/Learning Together/BorderData/StateWiseData/PedestrianExcudedAZCATX.csv", index=True)
print("=========================================\n")

'''
==============================================================================================================
Find out total number of Pedestrians crossed US-Canada border since 1996
Syntax:
1. Construct a filtered DF which will contain only pedestrians data (pedestrianDF=(df2[df2.Measure == Pedestrians])
2. Sort the pedestrianDF by column 'Value' in ascending order
3. Get the total of 'Value' column
==============================================================================================================
'''
pedestrianDF=df3[df3.Measure == "Pedestrians"]
pedestrianDF=pedestrianDF.sort_values('Value', ascending=False)
print("\nOutput first 100 header data of the pedestrianDF \n", pedestrianDF.head(100))
totalPedestrians=pedestrianDF['Value'].sum()
print("Total pedestrians crossed US-Canada border since 1996 = ", totalPedestrians, "\n")

'''
==============================================================================================================
Find out state wise total number of Pedestrians crossed US-Canada border since 1996
Syntax:
1. Construct state wise filtered DF which will contain only pedestrians data for that specific state (using for-loop)
2. Calculate the state wise total of pedestrians crossed the border
3. Put the total of each state in a list
==============================================================================================================
'''
listOfTotalPedestriansByState: list = []
stateList: list = ["AK", "ID", "ME", "MI", "MN", "MT", "ND", "NY", "VT", "WA"]
for i in stateList:
    stateWisePedestrianDF=pedestrianDF[pedestrianDF.State == i]
    stateWisePedestrianDF.to_csv("~/Desktop/Learning/Learning Together/BorderData/StateWiseData/Pedestrian{}.csv".format(i), index=True)
    totalPedestrianCrossed=stateWisePedestrianDF['Value'].sum()
    print("Total pedestrians crossed US-Canada border since 1996 in state {} = ".format(i), totalPedestrianCrossed)

    # Put the total in a a list
    listOfTotalPedestriansByState.append(totalPedestrianCrossed)

print("\nList of the State wise pedestrians = ", listOfTotalPedestriansByState, "\n")
'''

==============================================================================================================
Plot a bar chart showing pedestrians of each state using matplotlib of pyplot
==============================================================================================================
'''
# Configuration of the plot parameters
plt.figure(figsize=(12, 6))
plt.title("State wise pedestrian crossed since 1996")
plt.xlabel("States")
plt.ylabel("Number of Pedestrians")
plt.xticks(rotation=0)
plt.grid(False)
plt.bar(stateList, listOfTotalPedestriansByState,  color="salmon")

# This is the location for the annotated text
i = 1.0
j = 1000
for i in range(len(stateList)):
    plt.annotate(listOfTotalPedestriansByState[i], (-0.25 + i, listOfTotalPedestriansByState[i] + j))

# Plotting
plt.show()

'''
==============================================================================================================
Find out year wise total number of Pedestrians crossed US-Canada border since 1996
Syntax:
1. Construct year wise filtered DF which will contain only pedestrians data for that specific year (using for-loop)
2. Calculate the year wise total of pedestrians crossed the border
3. Put the total of each year in a list
==============================================================================================================
'''
listOfTotalPedestriansByYear: list = []
listOfYear: list = []
pedestrianDF.Date = pd.to_datetime(pedestrianDF.Date)
for i in range(1996,2021,1):
    yearWisePedestrianDF = pedestrianDF[pedestrianDF.Date.dt.year.eq(i)]
    yearwiseTotalPedestrianCrossed = yearWisePedestrianDF['Value'].sum()
    yearWisePedestrianDF.to_csv("~/Desktop/Learning/Learning Together/BorderData/YearWiseData/YearwisePedestrian{}.csv".format(i), index=True)
    print("Total pedestrians for the year {}".format(i), yearwiseTotalPedestrianCrossed)

    # Put the total in a list
    listOfTotalPedestriansByYear.append(yearwiseTotalPedestrianCrossed)
    listOfYear.append(i)

print("\nList of the State wise pedestrians = ", listOfTotalPedestriansByYear, "\n")

'''
==============================================================================================================
Plot a bar chart showing pedestrians of each year using matplotlib of pyplot
==============================================================================================================
'''
# Configuration of the plot parameters
plt.figure(figsize=(12, 6))
plt.title("Year wise pedestrian crossed since 1996")
plt.xlabel("Year")
plt.ylabel("Number of Pedestrians")
plt.xticks(rotation=0)
plt.grid(False)
plt.bar(listOfYear, listOfTotalPedestriansByYear, color="orange")

# This is the location for the annotated text
i = 1.0
j = 1000
for i in range(len(listOfYear)):
    plt.annotate(listOfTotalPedestriansByYear[i], (-0.25 + i, listOfTotalPedestriansByYear[i] + j))

# Plotting
plt.show()

'''
==============================================================================================================
Function implementation: findPresidencyWiseTotal()
What it does:
1. Take the DF 'pedestrianDF' of the pedestrians crossed US-Canada border as the master data
2. Now filter out the data for the range of start and end year of each presidency term
3. Calculate the total pedestrians crossed during that presidency term
4. Save data for each presidency term in .CSV format
==============================================================================================================
'''
def findPresidencyWiseTotal(presTerm:str, presStartYr:int, presEndYear:int):
    presidencyWisePedestrianDF = pedestrianDF[pedestrianDF.Date.dt.year.isin(range(presStartYr, presEndYear))]
    presidencyWiseTotalPedestrianCrossed = presidencyWisePedestrianDF['Value'].sum()
    presidencyWisePedestrianDF.to_csv("~/Desktop/Learning/Learning Together/BorderData/PresidencyWiseData/presidencyWisePedestrian{}.csv".format(presTerm), index=True)
    print("Total pedestrians for the presidency {}".format(presTerm), presidencyWiseTotalPedestrianCrossed)

    # Put the total in a list
    listOfTotalPedestriansByPresidency.append(presidencyWiseTotalPedestrianCrossed)

'''
==============================================================================================================
Find out total pedestrians crossed during different presidency
Syntax:
1. Create a list of the presidency terms
2. Create a list of start year of each presidency
3. Create a list of end year of each presidency
4. Call a function in a loop by passing the name of the presidency terms, start year and end year
5. Print the list of total pedestrians crossed in each presidency
==============================================================================================================
'''
listOfTotalPedestriansByPresidency: list = []
presidencyTermList: list = ["BC_Term1-(1996-00)", "GWB_Term1-(2001-04)", "GWB_Term2-(2005-08)", "BO_Term1-(2009-12)", "BO_Term2-(2013-16)", "DT_Term1-(2017-20)"]
presidencyStartYear: list = [1996, 2001, 2005, 2009, 2013, 2017]
presidencyEndYear: list = [2001, 2005, 2009, 2013, 2017, 2021]
for i in range(6):
    presTerm=presidencyTermList[i]
    presStartYr=presidencyStartYear[i]
    presEndYear=presidencyEndYear[i]

    findPresidencyWiseTotal(presTerm, presStartYr, presEndYear)

print("\nList of the Presidency wise pedestrians = ", listOfTotalPedestriansByPresidency, "\n")

'''
==============================================================================================================
Plot a bar chart showing pedestrians of each presidency term using matplotlib of pyplot
==============================================================================================================
'''
# Configuration of the plot parameters
plt.figure(figsize=(16, 6))
plt.title("Presidency wise pedestrian crossed since 1996")
plt.xlabel("US Presidency Term")
plt.ylabel("Number of Pedestrians")
plt.xticks(rotation=0)
plt.grid(False)
plt.bar(presidencyTermList, listOfTotalPedestriansByPresidency, color="lightgreen")

# This is the location for the annotated text
i = 1.0
j = 1000
for i in range(len(presidencyTermList)):
    plt.annotate(listOfTotalPedestriansByPresidency[i], (-0.25 + i, listOfTotalPedestriansByPresidency[i] + j))

# Plotting
plt.show()
