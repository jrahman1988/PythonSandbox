'''
Conditional filtering of the data of a DF
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\n",df.head(3))

#Extract all rows where all 'HP' values are greater than 50
df1 = df["HP"] > 50
print("\n",df1.head(10))

#Extract all rows where all 'HP' values are greater than 50 and 'Type 1' = Rock and 'Speed' > 50
df2 = df[(df["HP"] > 50) & (df["Type 1"] == "Rock") & (df["Speed"] > 80)]
print("\n",df2.head(10))
