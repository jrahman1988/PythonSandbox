'''
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
Features of DataFrame:
    Potentially columns are of different types
    Size – Mutable
    Labeled axes (rows and columns)
    Can Perform Arithmetic operations on rows and columns

Create a DataFrame from Dict of ndarrays / Lists
All the ndarrays must be of same length. If index is passed, then the length of the index should equal to the length of the arrays.
If no index is passed, then by default, index will be range(n), where n is the array length.
'''
import pandas as pd

#Create DataFrame from a ndarray dictionary
data = {"Name":['Roshan', 'Hossam', 'Bala', 'Marcel', 'Deepak'], "Membership Due":[100, 200, 300, 400, 500]}
df = pd.DataFrame(data)
print("\n Here is the Data Frame created form a dictionary \n {}".format(df))