'''
Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
The axis labels are collectively called index.
The index of the data item in a Series can be customized
'''
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',100)

#Create Series() in Pandas from a dictionary()
d1 = {'Item1':'Banana','Item2':'Kiwi','Item3':'Egg','Item4':'Butter','Item5':'Bread','Item6': 75.05, 'Item7':100}
s1 = pd.Series(d1)
print("\nThe dictionary is \n {} ".format(d1))
print("\nThe transformed 4, Series from numpy is \n {} ".format(s1))

#Accessing Series data using a specific index label, in this example 'Item6'
print("\nThe item in the dictionary with key 'Item6' is \n {} ".format(s1['Item6']))

#Accessing Series data using a range of index label (in this example, from start to index label, 'Item3'
print("\nThe item in the dictionary with key 'Item6' is \n {} ".format(s1[:'Item3']))