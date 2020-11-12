'''
The Pandas I/O API is a set of top level reader functions accessed like pd.read_csv() that generally return a Pandas object.

The two workhorse functions for reading text files (or the flat files) are read_csv() and read_table().
They both use the same parsing code to intelligently convert tabular data into a DataFrame object
'''
import pandas as pd

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
Find out total number of Pedestrians crossed US-Canada border since 1996
Syntax:
1. Construct a filtered DF which will contain only pedestrians data (pedestrianDF=(df2[df2.Measure == Pedestrians])
2. Sort the pedestrianDF by column 'Value' in ascending order
3. Get the total of 'Value' column
'''
pedestrianDF=df2[df2.Measure == "Pedestrians"]
pedestrianDF=pedestrianDF.sort_values('Value', ascending=False)
print("\nOutput first 100 header data of the pedestrianDF \n", pedestrianDF.head(100))
totalPedestrians=pedestrianDF['Value'].sum()
print("Total pedestrians crossed US-Canada border since 1996 = ", totalPedestrians)
