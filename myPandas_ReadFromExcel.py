'''
Read an Excel file using read_excel() method of Pandas
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_excel("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.xlsx")
print("\nOutput the full file in DF format \n",df)
print("\nOutput the header of the file in DF format \n",df.head())
print("\nThe tail of the file in DF format \n",df.tail())