'''
A large number of methods collectively compute descriptive statistics and other related operations on DataFrame.
Most of these are aggregations like sum(), mean(), but some of them, like sumsum(), produce an object of the same size.
Generally speaking, these methods take an axis argument, just like ndarray.{sum, std, ...}, but the axis can be specified by name or integer
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Read the pokemon_data.csv from the file system and transform into a DataFrame using read_csv() method
df = pd.read_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/pokemon_data.csv")

#Output statistics of all data in the file using describe() method
print("\nOutput all basic statistics using describe(): \n", df.describe())

#Sort output using sort_values() method (default is ascending order)
print("\nOutput sorted data based on the column named 'Name': \n", df.sort_values('Name'))

#Sorting based on a single column in a file and output using sort_values() method (descending order - ascending=false)
print("\nOutput sorted data based on the column named 'Name' in descending order: \n", df.sort_values('Name', ascending=False))

#Sorting based on a multiple columns in a file and output using sort_values() method ('Name' column in ascending order and 'HP' column in descending order)
print("\nOutput sorted data based multiple columns 'Name' and 'HP' one in ascending and other in descending order: \n", df.sort_values(['Name', 'HP'], ascending=[1,0]))

#Summing the values in the columns of a DF using sum(axis) where axis = 0 is vertical and 1= horizontal
print("\nSum of the values in column with index 1 of the DF :\n", df.sum(1))