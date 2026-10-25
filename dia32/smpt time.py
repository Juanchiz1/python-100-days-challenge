import os
import random
import smtplib

from django.db import connection

my_email = "sonymusicmx@gmail.com"
password = os.environ.get("EMAIL_APP_PASSWORD")

#with smtplib.SMTP('smtp.gmail.com') as connection:
#  connection.starttls()
#   connection.login(user=my_email,password=password)
#    connection.sendmail(from_addr=my_email,
#    to_addrs="juandinegrete2006@outlook.com",
#    msg="Subject:Today \n\n This is the body of my email")


import  datetime

now = datetime.datetime.now()

date_of_birth = datetime.datetime(year=2006,month=7,day=3,hour=20)
print(date_of_birth)

now=datetime.datetime.now()
weekday=now.weekday()

if weekday==2:
    with open("quotes.txt") as file:
        all_quotes=file.readlines()
        quoute=random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,
                            message=f"This is your today quote!\n{quoute}")
