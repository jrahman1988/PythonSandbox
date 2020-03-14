'''
Find and output all rows contain a specific value in a specific column using df.loc()
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")

#Locate and output all rows contain a specific value in a specific column
print(df.loc[df['Type 1'] == "Fire"])

#Locate and output all rows contain a specific value in a specific column
print("\n",df.loc[df['Name'] == "Charmander"])
