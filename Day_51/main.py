import os
from twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = os.environ["EMAIL"]
TWITTER_PASS = os.environ["PASSWORD"]


chromedriver_path = "/home/pinnheads/Dev/chromedriver"
geckodriver_path = "/home/pinnheads/Dev/geckodriver"

bot = InternetSpeedTwitterBot(
    chromedriver_path, email=TWITTER_EMAIL, password=TWITTER_PASS
)
bot.get_internet_speed()
bot.tweet_at_provider()
