'''
Filtering the columns with certain values using regex functions
'''
import pandas as pd
import re

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df.columns)
print ("\n",df.tail)

#Find a certain value in a certain column using regex function with re.I(gnore) case to ignore the case
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
df = df.loc[(df['Type 1'].str.contains('rock|psychic',flags=re.I, regex=True))]
print ("\n",df.tail)

#Find a certain value beginning with a certain letters (e.g. ps) in a certain column using regex function with re.I(gnore) case to ignore the case
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
df = df.loc[(df['Type 1'].str.contains('^ro[a-z]*',flags=re.I, regex=True))]
print ("\n",df.tail)