'''
Find a specific header index and conditionally change the values in some columns, using loc() method
e.g. we'll change 'Legendary' value of all 'Rock' pokemon to True
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

#Modify 'Legendary' value of all 'Rock' pokemon to True
df.loc[df['Type 1'] == 'Rock', ['Legendary']] = 'GREAT!'
print(df.tail)