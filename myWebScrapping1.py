'''
Webscrapping
'''
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#Set the url to the website and access the site with our requests library
url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
print(response)

#Parse the html with BeautifulSoup so that we can work with a nicer, nested BeautifulSoup data structure.
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

#Use the method .findAll() to locate all of our <a> tags
#This code gives us every line of code that has an <a> tag.
# The information that we are interested in starts on line 36.
# Not all links are relevant to what we want, but most of it is, so we can easily slice from line 36
# To download the whole data set, let's do a for loop through all a tags
# print(soup.findAll('a'))
line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 38: #code for text files starts at line 36
        link = one_a_tag['href']
        print(link)
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1

#TO BE Continued....