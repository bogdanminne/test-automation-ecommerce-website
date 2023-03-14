#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Initializing website get and driver
website = 'http://127.0.0.1:8000/'
driver = webdriver.Chrome()
driver.get(website)




#Closing session
driver.quit()
