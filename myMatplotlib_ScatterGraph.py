'''
Using Matplotlib module of Python, draw a scatter plot
'''
from matplotlib import pyplot as plt
import numpy as np

#X axis values
x = np.arange(1,11)
print("\nData for x-axis: \n", x)

#Y axis values
y = [5,3,6,7,8,9,6,2,4,8]
print("\nData for y-axis: \n", y)

#Plot a linear line graph from the data (x,y)
plt.scatter(x,y)
plt.title('A scatter graph')
plt.xlabel("Some value on X-axis")
plt.ylabel("Some value on Y-axis")
plt.grid(True)
plt.show()