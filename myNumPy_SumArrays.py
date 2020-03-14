'''
Adding the arrays using sum() method of numpy module
'''
import numpy as np

#Create two one diemtional array of size 3 elements in each
a1 = np.array([10,20,30,40,50])
a2 = np.array([50,40,30,20,10])

#Now perform addition of all the elements of both arrays
b1 = np.sum([a1,a2])
print ("Sum of all vertical elements (axis=0) are \n{} :".format(b1))

#Now perform addition of vertical elements of each array using sum() method and axis=0 (which adds the veritical elements)
b2 = np.sum((a1,a2), axis=0)
print ("Sum of all vertical elements (axis=0) are \n{} :".format(b2))

#Now perform addition of horizontal elements of each array using sum() method and axis=1 (which adds the veritical elements)
b3 = np.sum((a1,a2), axis=1)
print ("Sum of all vertical elements (axis=0) are \n{} :".format(b3))