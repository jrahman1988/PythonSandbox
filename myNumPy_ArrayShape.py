'''
shape() class method of NumPy module returns the shape of an array type
'''
import numpy as np

#Create a 2x4 array
a1 = np.array([[10,20,30,40], [50,60,70,80]])
print("Size of the array = ", a1.shape)

#Create a single diemtional array
a2 = np.arange(10,100,5)
print("Shape of the array created is {} and the array is {} ".format(a2.shape, a2))

#Create a multi diemtional array of size 5x4 and fill with 6 using full()
a3 = np.full((5,4),6)
print("Shape of the array created is {} and the array is: \n {}".format(a3.shape, a3))

#Now change the matrix of the above array from 5x4 to 4x5
a4 = a3
a4.shape = (4,5)
print("Now the shape of the array a3 is transformed to {} and the array is: \n {}".format(a4.shape, a4))