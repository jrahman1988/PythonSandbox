'''
There is way of organizing a software program which is to combine data and functionality and wrap it inside something called an object.
This is called the object oriented programming paradigm.

In this program we'll explore Class, behaviour and attributes of a class
'''
#Declaring a class named Mail and its methods (behaviours). All methods of a class must have a default parameter 'self'
class Mail():

    #Class variable to count 'how many' types of Mail instances created
    numberOfObjectsCreated = 0

    #Init method to create an instance (object) by passing an object name
    def __init__(self, name):
        """Initilializes the data"""
        self.name = name
        print("Initializing an {}".format(self.name))
        Mail.numberOfObjectsCreated +=1

    def destinationOfMail(self, type: str):
        self.type = type

    def costOfMail(self, cost: int):
        self.cost = cost

    def sizeOfmail(self, size: int):
        self.size = size

    def getDescription(self):
        print("The type of the mail is ", self.type)
        print("The cost of the mail is ", self.cost)
        print("The size of the mail is ", self.size)

    @classmethod
    def countOfMail(count):
        """Prints number of Mail objects"""
        print("Created objects of Mail class are = {}".format(count.numberOfObjectsCreated))

#Create an object of the class Mail named domesticMail
dMail = Mail("domesticMail")
dMail.destinationOfMail("Domestic")
dMail.costOfMail(10)
dMail.sizeOfmail("Large")
dMail.getDescription()

#Create an object of the class Mail named internationalMail
iMail = Mail("internationalMail")
iMail.destinationOfMail("International")
iMail.costOfMail(99)
iMail.sizeOfmail("Small")
iMail.getDescription()

#How many Mail objects were created (here we are using class variable 'numberOfObjectsCreated'
print("Total Mail objects created = {} ".format(Mail.numberOfObjectsCreated))

#How many Mail objects were created (here we are using class method 'countOfMail()'
Mail.countOfMail()