import datetime as dt
import smtplib
from random import choice

my_email = ""
password = ""

# Get current day
now = dt.datetime.now()
day_today = now.weekday()
print(f"---------------------{day_today}----------------------")
if day_today == 4:
    # Create Message
    with open("./quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = choice(all_quotes)
        print(quote)
        print("--------------------------------------------------")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("Connection Established")
        connection.starttls()
        connection.login(user=my_email, password=password)
        print(f"Login done with {my_email} : {password}")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="utsavdeep022@outlook.com",
            msg=f"Subject:Friday Motivational Quote\n\n{quote}",
        )
        print("Mail has been sent. Check your inbox...")
else:
    pass
