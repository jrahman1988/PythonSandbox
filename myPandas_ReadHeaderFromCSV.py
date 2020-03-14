'''
Read the columns of the CSV file and present as DF index list
Read all items under a specific column name (e.g. 'Name'
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the list of the columns of the fie in the CSV file in DF format ", df.columns)
print('\n')

#Output all items under a specific column using df.['name of the column']
print("\nOutput all items under 'Name' column of the CSV file ", df.Name)
print("\nOutput all items under 'Name' column of the CSV file ", df['Name'])
print("\nOutput all items under 'Name' column of the CSV file ", df[['Name','Type 1','HP']])

#Output all items under a specific row using df.iloc[index value or range]
print("\nOutput all items under row with index '0' of the CSV file ", df.iloc[0])
print("\nOutput all items under rows from index '1' to '5' of the CSV file ", df.iloc[1:5])
# print("\nOutput all items under 'Name' column of the CSV file ", df[['Name','Type 1','HP']])

#Output all items of a specific row and column location using df.iloc[R.C]
print("\nOutput all items of a specific row=0 and column =5 location of the CSV file = ", df.iloc[0,5])
print("\nOutput all items of a specific row=555 and column =1 location of the CSV file = ", df.iloc[555,1])