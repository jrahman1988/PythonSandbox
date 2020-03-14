'''
Functions are reusable pieces of programs. They allow us to give a name to a block of statements, allowing us to run that block
using the specified name anywhere in your program and any number of times. This is known as calling the function.
'''
def printMultipleTimes(message:str, time:int):
    print(message * time)

#Call the functions by passing parameters
printMultipleTimes("Hello ",2)
printMultipleTimes("Hello ",5)