import smtplib
import pandas
import datetime as dt
import random

data = pandas.read_csv("birthdays.csv")
b_days = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = "example@emailprovider.com"
password = "12345678"

if today_tuple in b_days:
    b_day_person = b_days[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", b_day_person["name"])

    with smtplib.SMTP("email provider smtp server address") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=b_day_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )






