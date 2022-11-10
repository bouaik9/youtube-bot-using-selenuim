from selenium import webdriver
from selenium.webdriver.common.by import By
import time


topic = input("enter video title : ")
#getting our driver for edge that we have install before
Browser = webdriver.Edge()
#search for youtube website
Browser.get("https://youtube.com/")

#get the search bar
search_bare = Browser.find_element(By.NAME, "search_query")
#typing our topic
search_bare.send_keys(topic)
#click search button
search_bare.submit()

time.sleep(5)

#getting results
results = Browser.find_elements(By.XPATH, "//a[@id='video-title']")
#waiting 5 seconds and then click on the first video
Browser.implicitly_wait(5)
results[0].click()
time.sleep(100)
