'''
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
Features of DataFrame:
    Potentially columns are of different types
    Size – Mutable
    Labeled axes (rows and columns)
    Can Perform Arithmetic operations on rows and columns
'''
import pandas as pd

#Create DataFrame from a single list with only one column
data = [100,200,300,400,500]
df1 = pd.DataFrame(data)
print("\nCreated DataFrame = {} ".format(df1))

#Create DataFrame from a list of list with multiple columns
data = [['Alex',10],['Bob',12],['Clarke',13]]
df2 = pd.DataFrame(data, columns=['Name','Age'], dtype=float)
print ("\nThe DataFrame created from a 'list of list' is : \n{}".format(df2))