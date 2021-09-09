import os
from insta_bot import InstagramFollowerBot

INSTAGRAM_EMAIL = os.environ["EMAIL"]
INSTAGRAM_PASS = os.environ["PASSWORD"]
SIMILAR_ACCOUNT = "python.learning"

chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"

bot = InstagramFollowerBot(
    driver_path=chromedriver_path,
    similar_account=SIMILAR_ACCOUNT,
    username=INSTAGRAM_EMAIL,
    password=INSTAGRAM_PASS,
)

bot.login()
bot.find_account()
# bot.follow()
