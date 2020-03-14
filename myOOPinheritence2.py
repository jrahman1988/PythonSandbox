'''
In this program we'll explore Inherience of class in python.
The parent class is 'Mail', which has two class methods 'postage()' and 'destination()'.
Three inherited classes, 'LetterMail', 'Parcel' and 'AdMail' will be created from 'Mail'
'''
class Mail():

    '''Intialize method'''
    def __init__(self, type: str, destination: str):
        self.type = type
        self.destination = destination
        print("Initialized Mail type = {}, destination = ()".format(self.type, self.destination))

    def detailOfMail(self):
        print("Mail type = {}, Destination to = {} ".format(self.type, self.destination, end=""))

class LetterMail(Mail):
    def __init__(self, type: str, destination: str, postage: int):
        Mail.__init__(self, type, destination)
        self.postage = postage
        print("Initialized LetterMail")

class Parcel(Mail):
    def __init__(self, type: str, destination: str, size: int):
        Mail.__init__(self, type, destination)
        self.size = size
        print("Initialized Parcel")

class AdMail(Mail):
    def __init__(self, type: str, destination: str, count: int):
        Mail.__init__(self, type, destination)
        self.count = count
        print("Initialized Parcel")

#Crate objects
lm = LetterMail("Letter", "Toronto", 5)
pa = Parcel("Parcel", "San Francisco", 1000)
am = AdMail("Ad Mail", "Kanata North", 5000)

lm.detailOfMail()
pa.detailOfMail()
am.detailOfMail()
