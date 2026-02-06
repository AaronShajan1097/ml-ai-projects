import datetime as dt
import pandas
import random
import smtplib

my_email = "aaron@gmail.com"
my_pass = "vsvsdoiaoigowigoaiga"

data = pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data)

now = dt.datetime.now().date()
day = now.day
month = now.month

for (index,row) in df.iterrows():
    birth_day = row.day
    birth_month = row.month
    name = row['name']
    email = row['email']

    if birth_day == day and birth_month == month:
        letter = open(f"/letter_templates/letter_{random.randint(1,3)}.txt").read()
        changed_letter = letter.replace("[NAME]", name)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=email,
        msg=f"Subject: Happy Birthday\n\n{changed_letter}"
    )