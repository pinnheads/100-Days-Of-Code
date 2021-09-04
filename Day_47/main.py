import requests
from bs4 import BeautifulSoup
import smtplib
import os

my_email = os.environ["MY_EMAIL"]
smtp_email = os.environ["MY_SMTP_EMAIL"]
password = os.environ["MY_SMTP_PASSWORD"]


def email(price):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("Connection Established")
        connection.starttls()
        connection.login(user=smtp_email, password=password)
        connection.sendmail(
            from_addr=smtp_email,
            to_addrs=my_email,
            msg=f"Price({price}) for the product has dropped below the target price! Buy Now!",
        )


url = "https://www.amazon.in/LG-inch-55cm-LCD-Monitor/dp/B01IBM5V66/ref=sr_1_5?dchild=1&keywords=monitor&qid=1630727661&sr=8-5"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Request Line": "GET / HTTP/1.1",
}

response = requests.get(url=url, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
price_data = soup.find(name="span", id="priceblock_ourprice")
price = float(((price_data.string).split("₹")[-1]).replace(",", ""))
print(price)

if price <= 11199.0:
    email(price)
