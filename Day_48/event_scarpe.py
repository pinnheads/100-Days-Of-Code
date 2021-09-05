from selenium import webdriver

# set driver paths
chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Create a new events dictionary
events_dict = {}

# Open the page
driver.get("https://www.python.org/")

# Get all required tags
time_tags = driver.find_elements_by_xpath(
    "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/time"
)
a_tags = driver.find_elements_by_xpath(
    "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li/a"
)

# Create and add all new events
for event in range(len(time_tags)):
    new_event = {
        "time": (time_tags[event].get_attribute("datetime")).split("T")[0],
        "name": a_tags[event].text,
        "event_link": a_tags[event].get_attribute("href"),
    }
    events_dict[event] = new_event

# Print the events dictionary
print(events_dict)

# quit driver
driver.quit()
