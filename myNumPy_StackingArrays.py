'''
Transforming multiple arrays by stacking elements vertically using vstack(), horizontally using hstack(), and cloum_stack()
'''
import numpy as np

#Create two one diemtional array of size 3 elements in each
a1 = np.array([10,20,30,40,50])
a2 = np.array([50,40,30,20,10])
a3 = np.array([10,10,10,10,10])

#Transforming to a new array by stacking vertically using vstack()
v = np.vstack([a1,a2,a3])
print ("\n The verically stacked array is \n {} ".format(v))

#Transforming to a new array by stacking horizontally using hstack()
h = np.hstack([a1,a2,a3])
print ("\n The horizontally stacked array is \n {} ".format(h))

#Transforming to a new array by columns stacking using column_stack()
cs = np.column_stack([a1,a2,a3])
print ("\n The column stacked array is \n {} ".format(cs))