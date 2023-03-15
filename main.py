# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Initializing website get and driver
website = 'http://127.0.0.1:8000/'
driver = webdriver.Chrome()
driver.get(website)


# Test case 1 - Check customer login with invalid data
signin = driver.find_element(By.XPATH,'//a[contains(@href,"account/signin")]')
signin.click()

username = driver.find_element(By.NAME, 'username')
username.send_keys('testing2')
password = driver.find_element(By.NAME, 'password')
password.send_keys('testinginvalid')
signin_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.col-12.col-sm-12.col-md-12.col-lg-6.bg-light > div > form > button')
signin_button.click()


driver.save_screenshot('Testcase1-LoginInvalid.jpg')
# sleep(2)


# Test case 2 - Check customer register with invalid data
signup = driver.find_element(By.XPATH,'//a[contains(@href,"account/create")]')
signup.click()

signup_firstname = driver.find_element(By.NAME, 'first_name')
signup_lastname = driver.find_element(By.NAME, 'last_name')
signup_username = driver.find_element(By.NAME, 'username')
signup_password1 = driver.find_element(By.NAME, 'password1')
signup_password2 = driver.find_element(By.NAME, 'password2')
signup_email = driver.find_element(By.NAME, 'email')

signup_firstname.send_keys('Bogdan')
signup_lastname.send_keys('H')
signup_username.send_keys('Tester1')
signup_password1.send_keys('Tester1')
signup_password2.send_keys('Tester1')
signup_email.send_keys('tiendadesalamancaguanajuato@gmail.com')

# sleep(2)
signup_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > form > button')
signup_button.click()
driver.execute_script("window.scrollBy(0, 200);")
# sleep(2)

driver.save_screenshot('Testcase2-RegisterInvalid.jpg')


# Test case 3 - Check customer register with valid data
signup = driver.find_element(By.XPATH,'//a[contains(@href,"account/create")]')
signup.click()

signup_firstname = driver.find_element(By.NAME, 'first_name')
signup_lastname = driver.find_element(By.NAME, 'last_name')
signup_username = driver.find_element(By.NAME, 'username')
signup_password1 = driver.find_element(By.NAME, 'password1')
signup_password2 = driver.find_element(By.NAME, 'password2')
signup_email = driver.find_element(By.NAME, 'email')

signup_firstname.send_keys('Bogdan')
signup_lastname.send_keys('H')
signup_username.send_keys('Tester1')
signup_password1.send_keys('MattSmith11!')
signup_password2.send_keys('MattSmith11!')
signup_email.send_keys('tiendadesalamancaguanajuato@gmail.com')

# sleep(2)
signup_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > form > button')
signup_button.click()
# sleep(2)

driver.save_screenshot('Testcase3-RegisterValid.jpg')


# Test case 4 - Check customer login with valid data

signin = driver.find_element(By.XPATH,'//a[contains(@href,"account/signin")]')
signin.click()

username = driver.find_element(By.NAME, 'username')
username.send_keys('Tester1')
password = driver.find_element(By.NAME, 'password')
password.send_keys('MattSmith11!')
signin_button = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div.col-12.col-sm-12.col-md-12.col-lg-6.bg-light > div > form > button')
signin_button.click()


driver.save_screenshot('Testcase4-LoginValid.jpg')
# sleep(2)


# Test case 5 - Products - verify catalogue is displayed

driver.execute_script("window.scrollBy(0, 300);")

driver.save_screenshot('Testcase5-ProductsDisplay.jpg')
# sleep(2)


# Test case 6 - Products - verify individual product

product = driver.find_element(By.CSS_SELECTOR, 'body > div.container > div > div:nth-child(6)')
product.click()

driver.save_screenshot('Testcase6-IndividualProduct.jpg')
# sleep(2)


# Test case 7 - Verify product search functionality

search = driver.find_element(By.NAME, 'title')
search.send_keys('agua de horchata')
search.send_keys(Keys.RETURN)
driver.execute_script("window.scrollBy(0, 100);")

driver.save_screenshot('Testcase7-SearchFunction.jpg')
# sleep(2)


# Test case 8 - Verify category filtering

category_dropdown = driver.find_element(By.CSS_SELECTOR, '#nav > ul > li.nav-item.dropdown > a')
category_dropdown.click()
drinks = driver.find_element(By.CSS_SELECTOR, '#nav > ul > li.nav-item.dropdown.show > div > a:nth-child(2)')
drinks.click()

driver.save_screenshot('Testcase8-CategoryFiltering.jpg')
# sleep(2)


# Test case 9 - Verify user can add product to cart

home_button = driver.find_element(By.CLASS_NAME, 'navbar-brand')
home_button.click()
product = driver.find_element(By.XPATH,'//a[contains(@href,"/food/aguacate")]')
product.click()
add_to_cart = driver.find_element(By.XPATH,'//a[contains(@href,"/cart/add")]')
add_to_cart.click()

driver.save_screenshot('Testcase9-AddToCart.jpg')
# sleep(2)


# Test case 10 - Verify user can checkout
pay_with_card = driver.find_element(By.CSS_SELECTOR, 'body > div.row.mx-auto > div:nth-child(2) > div > form > button > span')
pay_with_card.click()


wait = WebDriverWait(driver, 10)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'stripe_checkout_app')))


email = driver.find_element(By.CSS_SELECTOR, '#email')
name = driver.find_element(By.CSS_SELECTOR, '#shipping-name')
address = driver.find_element(By.CSS_SELECTOR, '#shipping-street')
postcode = driver.find_element(By.CSS_SELECTOR, '#shipping-zip')
city = driver.find_element(By.CSS_SELECTOR, '#shipping-city')
country = driver.find_element(By.CSS_SELECTOR, '#shipping-country')
payment_info_button = driver.find_element(By.CLASS_NAME, 'iconContinue')

email.send_keys('tiendadesalamancaguanajuato@gmail.com')
name.send_keys('Bogdan')
address.send_keys('Cipres Tropical')
postcode.send_keys('900394')
city.send_keys('Salamanca')
country.click()
country.send_keys('Mexico')
country.send_keys(Keys.RETURN)
payment_info_button.click()

sleep(2)

card_number = driver.find_element(By.CSS_SELECTOR, '#card_number')
card_expires = driver.find_element(By.CSS_SELECTOR, '#cc-exp')
card_cvc = driver.find_element(By.CSS_SELECTOR, '#cc-csc')
pay = driver.find_element(By.CSS_SELECTOR, '#submitButton > span > span')

card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')
card_number.send_keys('4')
card_number.send_keys('2')

sleep(1)
card_expires.send_keys('11')
card_expires.send_keys('23')
sleep(1)
card_cvc.send_keys('123')

sleep(2)

pay.click()

sleep(5)

driver.save_screenshot('Testcase10-VerifyUserCheckout.jpg')

sleep(1)




#Closing session
driver.quit()
