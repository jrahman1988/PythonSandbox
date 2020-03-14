'''
Functions are reusable pieces of programs. They allow us to give a name to a block of statements, allowing us to run that block
using the specified name anywhere in your program and any number of times. This is known as calling the function.
'''
def addTwoNumbers(x:int, y:int):
    z = x + y
    print("Addition of ", x, "and", y, " = ", z)

#Call the functions by passing parameters
addTwoNumbers(5,6)
addTwoNumbers(100, 200)