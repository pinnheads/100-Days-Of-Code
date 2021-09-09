from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


class InstagramFollowerBot:
    def __init__(self, driver_path, similar_account, username, password):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.account_to_follow = similar_account
        self.user_name = username
        self.pass_word = password

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(3)
        username = self.driver.find_element_by_name("username")
        username.send_keys(self.user_name)

        password = self.driver.find_element_by_name("password")
        password.send_keys(self.pass_word)
        sleep(5)
        password.send_keys(Keys.ENTER)

    def find_account(self):
        sleep(10)
        self.driver.get(f"https://www.instagram.com/{self.account_to_follow}")
        sleep(4)
        followers_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers_btn.click()
        sleep(3)
        modal = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div[2]"
        )
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal
            )
            self.follow()
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                sleep(3)
                cancel_button = self.driver.find_element_by_xpath(
                    "/html/body/div[7]/div/div/div/div[3]/button[2]"
                )
                cancel_button.click()
