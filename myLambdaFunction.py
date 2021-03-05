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

logFile = "/mnt/sda/Spark/spark-3.0.1-bin-hadoop3.2/README.md"

pythonAppeared = lambda s: s.count("Saprk")
hadoopAppeared = lambda s: s.count("Hadoop")
berkeleyAppeared = lambda s: s.count("Berkeley")

print("Python word appeared = ", pythonAppeared(logFile))
print("Hadoop word appeared = ", hadoopAppeared(logFile))
print("Berkeley word appeared = ", berkeleyAppeared(logFile))