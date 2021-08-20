# # SMTP - Simple Mail Transfer Protocol
import smtplib

my_email = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    print("Connection Established")
    connection.starttls()
    connection.login(user=my_email, password=password)
    print(f"Login done with {my_email} : {password}")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Subject:Hello World\n\nThis is the testing of SMTP module in python.",
    )
    print("Mail has been sent. Check your inbox...")

import datetime as dt

# get the current date time
now = dt.datetime.now()
print(now.year)

# set a datetime
date_of_birth = dt.datetime(year=2000, month=12, day=15)
print(date_of_birth)
