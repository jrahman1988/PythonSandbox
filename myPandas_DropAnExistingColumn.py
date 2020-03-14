'''
Drop an existing column from a DataFrame
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")

#Output the data frame
print("\nOutput the df: \n", df)

#Output column names of the data frame
print("Output the column names: ", df.columns)

#Add a new column 'Total' which will hold the summation values of columns ''HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed'
df['Total'] = df['HP'] + df['Attack'] + df['Defense']+ df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.columns)

#Add second new column 'Grand Total' which will hold the summation values of columns ''HP', 'Attack', 'Defense', 'Sp. Atk','Sp. Def', 'Speed', 'Total'
df['Grand Total'] = df['HP'] + df['Attack'] + df['Defense']+ df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] + df['Total']
print(df.columns)
print(df.head())

#Drop the Legendary column from the data frame
df = df.drop(columns='Legendary')
print(df.columns)
print("Output the df: \n", df)