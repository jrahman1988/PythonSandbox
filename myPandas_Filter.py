'''
Output a DF after filtering the columns with certain values
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\nOutput the header index of the DF: \n", df.columns)
print ("\n",df.tail)

#Filter and output a certain value from a certain column (e.g. value = 'Rock' from column = 'Type 1')
df = df.loc[(df['Type 1'] == 'Rock') & (df['Type 2'] == 'Grass') ]
print ("\n",df.tail)

#Filter and output a certain value from a certain column (e.g. value = 'Rock' from column = 'Type 1')
df = df.loc[(df['Type 1'] == 'Rock') & (df['Type 2'] == 'Grass')  & (df['HP'] > 70) ]
print ("\n",df.tail)

