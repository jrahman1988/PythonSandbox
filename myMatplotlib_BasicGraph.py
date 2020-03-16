'''
Using Matplotlib module of Python, draw a linear graphs
'''
from matplotlib import pyplot as plt
import numpy as np

#X axis values
x = np.arange(1,11)
print("\nData for x-axis: \n", x)

#Y axis values
y = 3*x
print("\nData for y-axis: \n", y)

#Plot a linear line graph from the data (x,y)
plt.plot(x,y)
plt.show()