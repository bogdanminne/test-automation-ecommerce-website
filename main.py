#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#Initializing website get and driver
website = 'http://127.0.0.1:8000/'
driver = webdriver.Chrome()
driver.get(website)

#Test case 1 - Check customer login with invalid data
signin = driver.find_element(By.XPATH,'//a[contains(@href,"account/signin")]')
signin.click()
username = driver.find_element(By.NAME, 'username')
username.send_keys('testing2')
password = driver.find_element(By.NAME, 'password')
password.send_keys('testinginvalid')
signin_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.col-12.col-sm-12.col-md-12.col-lg-6.bg-light > div > form > button')
signin_button.click()
driver.save_screenshot('Testcase1.jpg')

#Test case 2 - 



#Closing session
driver.quit()
