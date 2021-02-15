'''
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
'''
#define the lambda function
sentence = "I bought a bike, from a bile store, she bought a bike amazon, they bought a bike from bike stores"
myLambdaFunction = lambda argument: argument.count("bike")

#here we are calling the lambda function: passing the 'sentence' as parameter and lamda function is taking it as an 'argument'
print("Total number of 'bike' word appeared = ", myLambdaFunction(sentence))