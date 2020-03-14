'''
The Pandas I/O API is a set of top level reader functions accessed like pd.read_csv() that generally return a Pandas object.

The two workhorse functions for reading text files (or the flat files) are read_csv() and read_table().
They both use the same parsing code to intelligently convert tabular data into a DataFrame object
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the full file in DF format \n", df)
print("\nOutput the header of the file in DF format \n", df.head())
print("\nOutput the tail of the file in DF format \n", df.tail())