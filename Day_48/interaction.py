from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set driver paths
chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Firefox(executable_path=geckodriver_path)

# Open page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

search = driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# driver.quit()
