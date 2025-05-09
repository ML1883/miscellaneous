"""
Created in 2018 and might not work anymore

This is a web-crawler program that uses a Chrome driver to grab
google trends data and consequently download it to a folder of choice.

Note that the frequency of the data will thus depend on the dates that you give as
inputs.

In the current setup, the dates will return a monthly pattern

The ticker file should be a simple .txt file with a ticker on each line (or another phrase you want the data for)

@author: ML1883
"""

from selenium import webdriver
import time
import numpy as np
import os

TICKER_LIST_LOCATION = ""
PREFERRED_DOWNLOAD_LOCATION = ""
START_DATE = "2004-02-01"
END_DATE = "2017-12-31"

#Open our file with ticker names and consequently put them into a list
#Then remove the /n at the end of each element caused by our enters in the
#text file.
with open(TICKER_LIST_LOCATION) as tickerFile:
    searchTerms = tickerFile.readlines()
searchTerms = list(map(lambda s: s.strip(),searchTerms))


#Configure our download folder for Chrome
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : PREFERRED_DOWNLOAD_LOCATION}
chromeOptions.add_experimental_option("prefs",prefs)

#Create a for loop to go through all the search terms
for i in range(0, len(searchTerms)):
    print(i)
    #Initiate our webbrowser with out new options
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    #Load the webpage, click the first button with the CSS identifier
    #We are lucky enough that the first button on the page is button that we actually want
    driver.get("https://trends.google.com/trends/explore?date=" + START_DATE + "%20" + END_DATE + "&q=" + searchTerms[i])
    time.sleep(1)
    button = driver.find_element_by_css_selector('button.widget-actions-item.export')
    button.click()

    #Wait a couple of seconds so the CSV can download, then close down the browser
    time.sleep(4)
    driver.quit()
    
    #Rename the file so it is named after the ticker.
    os.rename(PREFERRED_DOWNLOAD_LOCATION + "multiTimeline.csv", PREFERRED_DOWNLOAD_LOCATION + searchTerms[i] + " (" + str(i) + ")" + ".csv")

    #Make us not get throttled by waiting a random amount of time
    time.sleep(np.random.normal(4, np.random.random_sample())) 
