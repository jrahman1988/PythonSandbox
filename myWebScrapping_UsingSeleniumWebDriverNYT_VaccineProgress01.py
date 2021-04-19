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
driver.get("https://www.nytimes.com/interactive/2021/world/covid-vaccinations-tracker.html")
#
# Find 'Show all' Button Using 'XPath'
show_all_button = driver.find_element_by_xpath("/html/body/div[1]/main/article/section/div/div/div[4]/div[1]/div/table/tbody/tr[16]")
time.sleep(2)

# Click 'Show all' Button to expand the table to the end
show_all_button.click()
time.sleep(2)
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
vaccineDF.to_csv("~/Desktop/Learning/Sandbox/PythonSandbox/Data/VaccineDataFmNYTStackOFSolution.csv", index=True)