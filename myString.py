import string

s1: str = "I work for Innovalost since 2007"
s2: str = """I started at Newbridge in 1997
             then I moved to NOKIA in 1999 
             then I worked briefly at Mitel for 6 months
             then I joined Ademco Video (Honeywell) as a consultant
             then I went to Toronto to work for ATI in 2003
             then I returned back to Ottawa to start with Edgewater Systems in 2005
             then I worked for Nakina Systems as consultant until November 2007
             then started at Innovapost in December 2007"""

#Print the character at a certain position
print(s1[5])

#Print the range from 5 to 12
print (s1[5:12])

#Print length of a string
print (len(s1))

#Convert and print full string to UPPER case
print(s1.upper())

#Convert and print full string to lower case
print(s1.lower())

#Count the number of lines in multi lines string s2
print(len(s2))

#Convert and print full string s2 to UPPER case
print(s2.upper())

#Convert and print full string s2 to lower case
print(s2.lower())

#Convert and print full string s2 to title type
print(s2.title())