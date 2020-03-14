'''
Drop an existing column from a DataFrame using iloc() method
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

#Add a new column by using iloc() method. Note that, we should use sum(axis=1) to add horizontally
df['Total'] = df.iloc[:,4:10].sum(axis=1)
print(df.columns)
print(df.head())