import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Chrome(executable_path=chromedriver_path)

my_email = os.environ["EMAIL"]
my_pass = os.environ["PASS"]

driver.get("https://tinder.com/app/recs")

login_btn = driver.find_element_by_class_name("button")
login_btn.click()

time.sleep(10)

fb_login = driver.find_element_by_xpath(
    '//*[@id="q545960529"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]'
)
fb_login.click()

# Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(my_email)
password.send_keys(my_pass)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

# Delay by 5 seconds to allow page to load.
time.sleep(5)

# Allow location
allow_location_button = driver.find_element_by_xpath(
    '//*[@id="q545960529"]/div/div/div/div/div[3]/button[1]/span'
)
allow_location_button.click()

time.sleep(7)
# Disallow notifications
notifications_button = driver.find_element_by_xpath(
    '//*[@id="q545960529"]/div/div/div/div/div[3]/button[2]/span'
)
notifications_button.click()

tinder_button = driver.find_element_by_xpath(
    "//*[@id='q-2020625691']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button"
)
for i in range(101):
    tinder_button.click()
    print("Swiping Right")
    time.sleep(5)
