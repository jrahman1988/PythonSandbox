'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
'''
#define the lambda function
sentence = "I bought a bike, from a bike store, she bought a bike from amazon, they bought a bike from bike stores"
myLambdaFunction = lambda argument: argument.count("bike")

#here we are calling the lambda function: passing the 'sentence' as parameter and lamda function is taking it as an 'argument'
print("Total number of 'bike' word appeared = ", myLambdaFunction(sentence))

# filePath = "~/Desktop/Learning/Sandbox/PythonSandbox/Data/README.md"
# readFile=open('~/Desktop/Learning/Sandbox/PythonSandbox/Data/README.md', 'r')
with open('/home/jamil/Desktop/Learning/Sandbox/PythonSandbox/Data/README.md') as f:
    readFile = f.readlines()

print (readFile)
print(readFile.count("Spark"))
sparkAppeared = lambda s: s.count("Spark")
apacheAppeared = lambda s: s.count("Apache")
hadoopAppeared = lambda s: s.count("Hadoop")

print("Spark word appeared = ", sparkAppeared(readFile))
print("Apache word appeared = ", apacheAppeared(readFile))
print("Hadoop word appeared = ", hadoopAppeared(readFile))