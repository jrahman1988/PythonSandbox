'''
Here we map the categorical variables to numerical values using pandas.get_dummies()
'''
import pandas as pd

s = pd.Series(list('abcdabcde'))
s_dummy = pd.get_dummies(s)
print(s_dummy)

d = pd.Series(list({'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}))
d_dummy = pd.get_dummies(d, dummy_na=False)
print(d_dummy)

d = pd.Series(list({'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}))
d_dummy = pd.get_dummies(d, dummy_na=True)
print(d_dummy)