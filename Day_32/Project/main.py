import smtplib
import pandas as pd
import datetime as dt
from random import randint

MY_EMAIL = ""
MY_PASSWORD = ""
MESSAGE = []

csv_data = pd.read_csv("./birthdays.csv", sep=",")
records = len(csv_data)

now = dt.datetime.now()
day_today = now.day
month_today = now.month


def send_mail(senders_addrs, receivers_addrs, msg_to_send):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("-------------Connection Established--------------")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        print(f"--------------Login done with {MY_EMAIL} : {MY_PASSWORD}---------")
        connection.sendmail(
            from_addr=senders_addrs, to_addrs=receivers_addrs, msg=msg_to_send
        )
        print(
            f"-----------------------------------\nFrom: {senders_addrs}\nTo: {receivers_addrs}\n\n{msg_to_send}"
        )
        print("----------Mail has been sent.----------")


def get_mail_body(name):
    msg_str = ""
    file_no = randint(1, 3)
    file_path = f"./letter_templates/letter_{file_no}.txt"
    with open(file_path) as letter:
        lines = letter.readlines()
        MESSAGE = [line.replace("[NAME]", name) for line in lines]
    for text in MESSAGE:
        msg_str += text
    return msg_str


for record in range(0, records):
    if (
        day_today == csv_data.loc[record, "day"]
        and month_today == csv_data.loc[record, "month"]
    ):
        bd_name = csv_data.loc[record, "name"]
        bd_email = csv_data.loc[record, "email"]
        mail_body = get_mail_body(bd_name)
        subject_line = f"Happy Birthday {bd_name}"
        msg_txt = f"Subject:{subject_line}\n\n{mail_body}"
        send_mail(senders_addrs=MY_EMAIL, receivers_addrs=bd_email, msg_to_send=msg_txt)
    else:
        continue
