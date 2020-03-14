'''
Read the rows of the CSV file and present as DF index list
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")

#Reading all rows using df.iterrows() method <-- not a pretty format
for index, row in df.iterrows():
    print ("\n", index, row)

#Reading all rows using df.iterrows() method using specific column index
for index, row in df.iterrows():
    print (index, row['Name'])

#Find and output all rows contain a specific value in a specific column
df.loc[df['Name'] == "Crustle"]