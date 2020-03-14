'''
The Series and DataFrame class of Pandas has an instance method called to_csv() which allows to write the DF to a file
either in .xlsx, .txt or .csv format
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df.columns)

#Now add a column named 'Total by adding all the columns value containg numeric values
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print("\nOutput the tail of the file with newly added column: \n",df.tail())

#Now write the new DF into a csv file with the added column + the index on first column
df = df.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/modified_withIndex.csv")

###------------------------------------------------------------------------------------###

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df1 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df1.columns)

#Now add a column named 'Total by adding all the columns value containg numeric values
df1['Total'] = df1['HP'] + df1['Attack'] + df1['Defense'] + df1['Sp. Atk'] + df1['Sp. Def'] + df1['Speed']
print("\nOutput the tail of the file with newly added column: \n",df1.tail())

#Now write the new DF into a csv file with the added column with no index on first column
df1 = df1.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/modified_withoutIndex.csv", index=False)

###------------------------------------------------------------------------------------###

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df2 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df2.columns)

#Now add a column named 'Total by adding all the columns value containg numeric values
df2['Total'] = df2['HP'] + df2['Attack'] + df2['Defense'] + df2['Sp. Atk'] + df2['Sp. Def'] + df2['Speed']
print("\nOutput the tail of the file with newly added column: \n",df2.tail())

#Now write the new DF into a xlsx file with the added column with no index on first column
df2 = df2.to_excel("~/Desktop/Learning/Sandbox/PythonSandbox/Data/modified_withoutIndex.xlsx", index=False)

###------------------------------------------------------------------------------------###

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df3 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df3.columns)

#Now add a column named 'Total by adding all the columns value containg numeric values
df3['Total'] = df3['HP'] + df3['Attack'] + df3['Defense'] + df3['Sp. Atk'] + df3['Sp. Def'] + df3['Speed']
print("\nOutput the tail of the file with newly added column: \n",df3.tail())

#Now write the new DF into a xlsx file with the added column with no index on first column
df3 = df3.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/modified_withoutIndex.txt", index=False, sep='\t')