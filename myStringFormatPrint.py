#Ways to format and print

age: int = 20
name: str = "Shelley"

#Style 1 where format uses indexed parameters
print('{0} was graduated from Wayne State University in Michigan USA when she was {1}'.format(name,age))

#Style 2 where 'f' is used as f-string
print(f'{name} was graduated from Wayne State University in Michigan USA when she was {age}')

#Style 3 where format's parameters can mbe changed as local variable
print('{someOne} was graduated from Wayne State University in Michigan USA when she was {someAge}'.format(someOne=name,someAge=age))