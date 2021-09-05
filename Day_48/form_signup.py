from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# set driver paths
chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Firefox(executable_path=geckodriver_path)


driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")


first_name.send_keys("Utsav")
first_name.send_keys(Keys.TAB)
time.sleep(1)
last_name.send_keys("Deep")
last_name.send_keys(Keys.TAB)
time.sleep(2)
email.send_keys("utsavdeep01@gmail.com")
time.sleep(3)
email.send_keys(Keys.ENTER)

time.sleep(3)
driver.quit()
