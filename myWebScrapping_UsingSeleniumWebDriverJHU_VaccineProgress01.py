'''
Based on the solution someone suggested to my questions at SOF:
https://stackoverflow.com/questions/67145023/how-to-grab-a-complete-table-hidden-beyond-show-all-by-web-scraping-in-python?noredirect=1#comment118687563_67145023
'''
import pandas as pd
import time
from selenium import webdriver  # This module helps to fetch data and on-click event purpose
#
# Create 'FireFox' Webdriver Object
driver = webdriver.Firefox()
#
# Get Website of Vaccination table
driver.get("https://coronavirus.jhu.edu/vaccines/international")
#
# Find 'International' Button Using 'XPath'
international_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[11]/div[1]/div/div[2]")
time.sleep(2)
# Click to select the International table
international_button.click()
time.sleep(2)
#
# Find 'Show all' Button Using 'XPath'
show_all_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[11]/div[2]/div/div/div[2]/button")
time.sleep(5)
# Click 'Show all' Button to expand the table to the end
show_all_button.click()
time.sleep(5)
#
# Get 'HTML' Content of Page then quit the web page
html_data = driver.page_source
driver.quit()
#
# Convert the table to Pandas DF
vaccineDF = pd.read_html(html_data)[0]
#
# Print Whole Dataset
vaccineDF = vaccineDF.reset_index(drop=True)
# print(type(vaccineDF))
# print(vaccineDF.info())
# print(vaccineDF.head(100))
# print(vaccineDF.tail(100))
vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFmJHU.csv", index=True)