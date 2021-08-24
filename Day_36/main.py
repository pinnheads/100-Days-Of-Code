import requests
import datetime as dt
from os import environ
from twilio.rest import Client

account_sid = environ.get("TWILIO_ACC_SID")
auth_token = environ.get("TWILIO_AUTH_TOKEN")
my_number = environ.get("MY_PHONE_NO")

stock_base_url = "https://www.alphavantage.co/query"
stock_api_key = environ.get("ALPHA_STOCK_API_KEY")

news_base_url = "https://newsapi.org/v2/everything"
news_api_key = environ.get("NEWS_API_KEY")
top_3_articles = []

MSG = ""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENT_INC = 0


def format_msg():
    global MSG
    if PERCENT_INC < 0:
        MSG = f"{STOCK}: 🔺{PERCENT_INC}%\n"
        for article in top_3_articles:
            MSG += f"Headline: {article['title']}\nBrief: {article['content']}\n\n"
    else:
        MSG = f"{STOCK}: 🔺{PERCENT_INC}%\n"
        for article in top_3_articles:
            MSG += f"Headline: {article['title']}\nBrief: {article['content']}\n\n"

    print(MSG)


yesterday = dt.datetime.now() - dt.timedelta(days=1)
yest_weekday = yesterday.strftime("%A")
yesterday = yesterday.strftime("%Y-%m-%d")

day_before_yesterday = ""

if yest_weekday == "Monday":
    day_before_yesterday = (dt.datetime.now() - dt.timedelta(days=4)).strftime(
        "%Y-%m-%d"
    )
else:
    day_before_yesterday = (dt.datetime.now() - dt.timedelta(days=2)).strftime(
        "%Y-%m-%d"
    )

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key,
    "pageSize": 3,
    "page": 1,
    "sortBy": "relevancy",
    "from": day_before_yesterday,
    "to": yesterday,
}


def send_msg():
    global MSG
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=MSG,
        from_="+15625488293",
        to=my_number,
    )
    print(message.status)


def calculate_inc_dec(dby_stock, y_stock):
    global PERCENT_INC
    increase = y_stock - dby_stock
    percent_inc = round((increase / dby_stock) * 100)
    print(f"Percentage Increase: {percent_inc}")
    PERCENT_INC = percent_inc
    if percent_inc > 0 or percent_inc < 0:
        get_news(req_url=news_base_url, parameters=news_parameters)
        format_msg()
        send_msg()


def get_stock(parameters, req_url):
    response = requests.get(url=req_url, params=parameters)
    response.raise_for_status()

    data = response.json()
    yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    dby_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
    calculate_inc_dec(dby_stock=dby_close, y_stock=yesterday_close)


def get_news(req_url, parameters):
    response = requests.get(url=req_url, params=parameters)
    response.raise_for_status()
    data = response.json()
    news_articles = data["articles"][:3]
    for article in range(3):
        new_article = {
            "title": news_articles[article]["title"],
            "content": news_articles[article]["description"],
        }
        top_3_articles.append(new_article)


get_stock(req_url=stock_base_url, parameters=stock_parameters)
