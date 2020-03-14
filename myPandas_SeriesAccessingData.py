'''
Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
The axis labels are collectively called index.
The data in a Series can be retrieved using index
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Create Series() in Pandas from a dictionary()
d1 = {"key1":"Item1","key2":"Item2","key3":"Item3","key4":"Item4","key5":"Item1"}
s3 = pd.Series(d1)
print("\nThe dictionary is \n {} ".format(d1))
print("\nThe transformed 4, Series from numpy is \n {} ".format(s3))

#Now reverse the index for each items in the Series
s4 = pd.Series(d1, index=['key5','key4','key3','key2','key1'])
print("\nThe original Series s3 from numpy was \n {} ".format(s3))
print("\nThe transformed Series with customized index \n {} ".format(s4))