from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InternetSpeedTwitterBot:
    def __init__(self, driver_path, email, password):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.email = email
        self.password = password
        self.down = 100
        self.up = 100
        self.test_down = 0
        self.test_up = 0
        self.ping = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        speed_test_btn = self.driver.find_element_by_class_name("js-start-test")
        speed_test_btn.click()
        sleep(45)

        results = self.driver.find_elements_by_class_name("result-data-large")
        self.ping = results[0].text
        self.test_down = results[1].text
        self.test_up = results[2].text

    def tweet_at_provider(self):
        if float(self.test_down) < self.down:
            self.driver.get("https://twitter.com/home")
            sleep(4)

            email_field = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
            )
            email_field.send_keys(self.email)

            password_field = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
            )
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.ENTER)
            sleep(2)

            tweet = f"Hey Internet Provider, Why is my internet speed {self.test_down} down/ {self.test_up} up when I pay for {self.down}down/{self.up}up??"

            tweet_field = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
            )
            tweet_field.click()
            tweet_field.send_keys(tweet)
            sleep(4)

            tweet_btn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span'
            )
            tweet_btn.click()
        else:
            print("Speed is okay!")
            pass
