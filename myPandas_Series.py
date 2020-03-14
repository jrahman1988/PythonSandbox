'''
Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
The axis labels are collectively called index.
'''
import pandas as pd
import numpy as np

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Simpale Series data
s1=pd.Series([1,2,3,4,5])
print("\n",s1)

#Create an array() in numpy and use with Series() in Pandas
a1 = np.array(['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(a1)
print("\nThe created array by numpy is \n {} ".format(a1))
print("\nThe transformed Series from numpy is \n {} ".format(s2))

#Create Series() in Pandas from a dictionary()
d1 = {"key1":"Item1","key2":"Item2","key3":"Item3","key4":"Item4","key5":"Item1"}
s3 = pd.Series(d1)
print("\nThe dictionary is \n {} ".format(d1))
print("\nThe transformed Series from numpy is \n {} ".format(s3))