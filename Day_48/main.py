from selenium import webdriver

chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Firefox(executable_path=geckodriver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

search = driver.find_element_by_name("q")
print(search.get_attribute("placeholder"))

link = driver.find_element_by_xpath(
    "/html/body/div/footer/div[2]/div/ul/li[3]/a"
)
print(link.get_attribute("href"))

# driver.close()
driver.quit()
