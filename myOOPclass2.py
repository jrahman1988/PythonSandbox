'''
There is way of organizing a software program which is to combine data and functionality and wrap it inside something called an object.
This is called the object oriented programming paradigm.

In this program we'll explore Class, behaviour and attributes of a class
'''
#Declaring a class named Mail and its methods (behaviours). All methods of a class must have a default parameter 'self'
class Mail():

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


#Create an object of that class
m = Mail()
print (m)

#Create an object of the class Mail named domesticMail
domesticMail = Mail()
domesticMail.destinationOfMail("Domestic")
domesticMail.costOfMail(10)
domesticMail.sizeOfmail("Large")
domesticMail.getDescription()

#Create an object of the class Mail named internationalMail
internationalMail = Mail()
internationalMail.destinationOfMail("International")
internationalMail.costOfMail(99)
internationalMail.sizeOfmail("Small")
internationalMail.getDescription()