'''
This program will be as a module by another program, by importing module [import timesTable
A module can be imported by another program to make use of its functionality. This is how we can use the Python standard
library as well.
'''
def doTimes(x:int):
    i = 1
    print("Times table of ", x)
    while (i <= 10):
        print(x, "*", i, "=", x*i)
        i=i+1

__version__ = '1.0'