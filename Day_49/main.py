import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

my_email = os.environ["EMAIL"]
my_pass = os.environ["PASSWORD"]

# set driver paths
chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Firefox(executable_path=geckodriver_path)


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WRA=true&geoId=102713980&keywords=python%20developer&location=India&sortBy=R"
)
time.sleep(5)

# Sign In
sign_in_btn = driver.find_element_by_partial_link_text("Sign in")
sign_in_btn.click()

username = driver.find_element_by_name("session_key")
username.send_keys(my_email)

password = driver.find_element_by_name("session_password")
password.send_keys(my_pass)

password.send_keys(Keys.ENTER)
time.sleep(3)
# Handle extra verification
if not check_exists_by_xpath("//*[@id='ember33']"):
    time.sleep(30)


jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(3)
    save_btn = driver.find_element_by_class_name("jobs-save-button")
    save_btn.click()
    time.sleep(3)
