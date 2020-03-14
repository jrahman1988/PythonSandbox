'''
Read an Excel file using read_csv() method of Pandas
'''
import pandas as pd

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method -- without any delimiter
df1 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.txt")
print("\nOutput the full file in DF format ", df1)
print("\nOutput the header of the file in DF format ", df1.head())
print("The tail of the file in DF format ", df1.tail())

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method -- with delimiter= '\t'
df2 = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.txt", delimiter='\t')
print("\nOutput the full file in DF format ", df2)
print("\nOutput the header of the file in DF format ", df2.head())
print("The tail of the file in DF format ", df2.tail())