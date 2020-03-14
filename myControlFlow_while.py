'''
The while statement allows you to repeatedly execute a block of statements as long as a condition is true.
A while statement is an example of what is called a looping statement. A while statement can have an optional else clause.
'''

#Modifying the values using while loop in a list
l1: list = [1,2,3,4,5,6,7,8,9,10]
print("The original list: " , l1)

i=0
while (i < len(l1)):
    l1[i] = l1[i] + 100
    i=i+1
print("The modified new list is: ", l1)

#Guessing game using while-else loop
number = 23

while True:
    guess = int(input('Enter an integer : ')) #input statement to enter data from console
    if guess == number:
        print('Congratulations, you guessed it.')
        break
    elif guess < number:
        print('No, it is a little higher than that.')
        continue
    else:
        print('No, it is a little lower than that.')
        continue

# Do anything else you want to do here
print('Done')
