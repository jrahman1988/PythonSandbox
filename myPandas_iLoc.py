'''
Locate the data in a DF using 'iloc()' or index Locator
It takes two arguments, iloc(rows,columns)
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")
print("\n",df.head(3))

#Extract all rows and selective range of columns using iloc()
df1 = df.iloc[:, 4:7]
print("\n",df1.head(10))

#Extract selective range of rows and selective range of columns using iloc()
df2 = df.iloc[0:100, 4:7]
print("\n",df2.head(50))
