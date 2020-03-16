'''
Using Matplotlib module of Python, draw a linear graphs
'''
from matplotlib import pyplot as plt
import numpy as np

#X axis values
x = np.arange(1,11)
print("\nData for x-axis: \n", x)

#Y axis values
y1 = 3*x
y2 = 4*x
print("\nData for y1-axis: \n", y1)
print("\nData for y2-axis: \n", y2)

#Plot a linear line graph from the data (x,y) with color attribute and titles of the axes and linewidth() and linestyle() and grid()
plt.title("Some Graph")
plt.xlabel("x-axis values")
plt.ylabel("y-axis values")
plt.plot(x,y1, color="Orange", linewidth=2, linestyle=':')
plt.plot(x,y2, color="Green", linewidth=2, linestyle=':')
plt.grid(True)
plt.show()